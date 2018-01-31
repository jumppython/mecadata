# -*- coding: utf-8 -*-

import scrapy
import sqlite3 as sql
import random
from scrapy.loader import ItemLoader
from scrapinghub import ScrapinghubClient
from remercari.items import ItemList
from time import sleep

class AreaInfoSpider(scrapy.Spider):
	name = "areainfo"
	#download_delay = 5.0

	def start_requests(self):
		client = ScrapinghubClient('ec16b94bcf024d0bb502684368658d59')
		myproject = client.projects.get('254951')
		mystore = myproject.collections.get_store('area_init')

		for item in mystore.iter():
			elem = item['value']
			area = [_ for _ in elem['area_url']]
			for url_i in area:
				for page in range(1,3):
					url = 'https://www.mercari.com'+url_i+'?page=%d' % page
					request = scrapy.Request(url=url,callback=self.parse,errback=self.error_handler)
					request.meta['area_id'] = url_i.split('/')[3]
					yield request

	def parse(self, response):
		area_id = response.meta['area_id']
		l = ItemLoader(item=ItemList(), response=response)
		l.add_xpath('item_url', '//a[starts-with(@href,"https://item.mercari.com/jp/")]/@href')
		item_urls = response.xpath('//a[starts-with(@href,"https://item.mercari.com/jp/")]/@href').extract()
		item_ids = [_.split('/')[4].encode() for _ in item_urls]
		for _ in item_ids:
			l.add_value('item_id', _)
		l.add_value('area_id',area_id)

		return l.load_item()
		
	def error_handler(self, failure):
		sleep(30)
