# -*- coding: utf-8 -*-

import scrapy
import sqlite3 as sql
import csv

class AreaInitialSpider(scrapy.Spider):
	name =  "areainitial"
	savetowhere = "csv"

	def start_requests(self):
		urls = ['https://www.mercari.com/jp/area/']
		for url in urls:
			request = scrapy.Request(url=url, callback=self.parse)
			#request.meta['proxy'] = "202.9.104.10:80"
			yield request

	def parse(self, response):
		area_urls = response.xpath('//a[starts-with(@href, "/jp/area/")]/@href').extract()
		area_names = response.xpath('//a[starts-with(@href, "/jp/area/")]/text()').extract()
		
		if self.savetowhere == 'db':
			# Create areas Table to save couple of areanames and areaurls
			# Create a connection to database file
			conn = sql.connect('area.db')

		if self.savetowhere == 'csv':
			# Create areas File to save couple of areanames and areaurls
			conn = open('area.csv','w')
		
		self.saveto(conn, area_urls=area_urls, area_names=area_names)

	def saveto(self, conn, **items):
		area_urls = items['area_urls']
		area_names = items['area_names']
		if type(conn) == sql.Connection:
			c = conn.cursor()
			# Create Table
			c.execute('CREATE TABLE areas (area_id,area_name, area_url)')
			# Insert lots of area records
			records = [(int(area_urls[i].split('/')[3]),area_names[i],area_urls[i]) for i in range(len(area_urls))]
			c.executemany('INSERT INTO areas VALUES (?,?,?)',records)
			conn.commit()
			conn.close()
		elif type(conn) == file:
			c = csv.writer(conn)
			# Insert lots of area records
			records = [(int(area_urls[i].split('/')[3]), \
				       area_names[i].decode('utf-8'), \
				       area_urls[i].decode('utf-8')) for i in range(len(area_urls))]
			c.writerows(records)
			conn.close()



