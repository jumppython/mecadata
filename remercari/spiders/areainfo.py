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

		for item in mystore.iter():
			area = item['value']
			for page in range(1,3):
				url = 'https://www.mercari.com'+area[1]+'?page=%d' % page
				request = scrapy.Request(url=url,callback=self.parse)
				request.meta['area_id'] = area[1].split('/')[3]
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
		
		
