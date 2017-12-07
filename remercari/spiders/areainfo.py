# -*- coding: utf-8 -*-

import scrapy
import sqlite3 as sql
import random
from scrapy.loader import ItemLoader
from scrapinghub import ScrapinghubClient
from remercari.items import ItemList

class AreaInfoSpider(scrapy.Spider):
	name = "areainfo"

	def start_requests(self):
		client = ScrapinghubClient('ec16b94bcf024d0bb502684368658d59')
		myproject = client.projects.get('254951')
		mystore = myproject.collections.get_store('area_init')

		#self.c.execute('DROP TABLE IF EXISTS areainfos')
		#self.c.execute('CREATE TABLE IF NOT EXISTS areainfos (item_id, item_url, area_id)')
		#areas = [row for row in self.c.execute('SELECT * FROM areas ORDER BY area_id')]
		#self.conn.commit()
		#self.conn.close()
		#for area in areas:
		for item in mystore.iter():
			area = item['value']
			for page in range(1,51):
				url = 'https://www.mercari.com'+area[1]+'?page=%d' % page
				request = scrapy.Request(url=url,callback=self.parse)
				#if self.proxy_pool:
				#	request.meta['proxy'] = random.choice(self.proxy_pool)
				#request.meta['proxy'] = '202.9.104.10:80'
				request.meta['area_id'] = area[1].split('/')[3]
				yield request
		#self.conn.commit()

	def parse(self, response):
		#global conn
		#global c
		#item_urls = response.xpath('//a[starts-with(@href,"https://item.mercari.com/jp/")]/@href').extract()
		#item_ids = [_.split('/')[4].encode() for _ in item_urls]
		#area_id = response.meta['area_id']
		#records = [(item_ids[i], item_urls[i], area_id) for i in range(len(item_urls))]
		#self.c.executemany('INSERT INTO areainfos VALUES (?,?,?)', records)

		l = ItemLoader(item=ItemList(), response=response)
		l.add_xpath('item_url', '//a[starts-with(@href,"https://item.mercari.com/jp/")]/@href')
		item_urls = response.xpath('//a[starts-with(@href,"https://item.mercari.com/jp/")]/@href').extract()
		item_ids = [_.split('/')[4].encode() for _ in item_urls]
		for _ in item_ids:
			l.add_value('item_id', _)

		return l.load_item()
		
		
