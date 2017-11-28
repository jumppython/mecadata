# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from remercari.items import AreaList

class AreaInitialSpider(scrapy.Spider):
	name =  "areainitial"

	def start_requests(self):
		urls = ['https://www.mercari.com/jp/area/']
		for url in urls:
			request = scrapy.Request(url=url, callback=self.parse)
			#request.meta['proxy'] = "202.9.104.10:80"
			yield request

	def parse(self, response):
		l = ItemLoader(item=AreaList(), response=response)
		l.add_xpath('area_urls', '//a[starts-with(@href, "/jp/area/")]/@href')
		l.add_xpath('area_names', '//a[starts-with(@href, "/jp/area/")]/text()')

		return l.load_item()
