# -*- coding: utf-8 -*-

import scrapy
import sqlite3 as sql
import random
from scrapinghub import ScrapinghubClient
from remercari.items import ItemInfo

class ItemInfoSpider(scrapy.Spider):
	name = "iteminfo"
	#global conn
	#global c
	#conn = sql.connect('item.db')
	#c = conn.cursor()

	#def __init__(self, *args, **kwargs):
	#	super(ItemInfoSpider, self).__init__(*args, **kwargs)
	#	self.conn = sql.connect('dataset/item.db')
	#	self.c = self.conn.cursor()
		#self.proxy_pool = ['202.9.104.10:80', \
		#                   '110.77.232.210:8080']

	def start_requests(self):
		#self.c.execute('DROP TABLE IF EXISTS iteminfos')
		#self.c.execute('CREATE TABLE IF NOT EXISTS iteminfos (item_id, item_main_type, item_mid_type, item_sub_type, item_price, area_id)')
		#self.conn.commit()
		#temp_conn = sql.connect('dataset/area.db')
		#temp_c = temp_conn.cursor()
		#temp_c.execute('DELETE FROM areainfos WHERE rowid NOT IN (SELECT min(rowid) FROM areainfos GROUP BY item_id,item_url,area_id)')
		#item_list = [row for row in temp_c.execute('SELECT * FROM areainfos ORDER BY area_id')]
		#temp_conn.commit()
		client = ScrapinghubClient('ec16b94bcf024d0bb502684368658d59')
		myproject = client.projects.get('254951')
		mystore = myproject.collections.get_store('area_info')
		value_num = mystore.count()
		#for item in item_list:
		for item in range(value_num):
			#url = item[1].encode()
			log_item = mystore.get(str(item))
			area_id = log_item['value']['area_id'][0]
			item_ids = log_item['value']['item_id']
			item_urls = log_item['value']['item_url']
			for i in range(len(item_ids)):
				#request = scrapy.Request(url=url,callback=self.parse)
				#request.meta['item_id'] = item[0]
				#request.meta['area_id'] = item[2]
				request = scrapy.Request(url=item_urls[i],callback=self.parse)
				request.meta['item_id'] = item_ids[i]
				request.meta['area_id'] = area_id
				yield request
		#self.conn.commit()

	def parse(self, response):
		#global conn
		#global c
		l = ItemLoader(item=ItemInfo(), response=response)
		category_contain = response.xpath(u'//tr[contains(.,"\u30ab\u30c6\u30b4\u30ea\u30fc")]//text()').extract()
		category_text = [_.strip() for _ in category_contain]
		category_text_uniq = [_ for _ in category_text if len(_)>0]
		if len(category_text_uniq)!=0:
			main_type = category_text_uniq[1] if len(category_text_uniq)>1 else u''
			mid_type = category_text_uniq[2] if len(category_text_uniq)>2 else u''
			sub_type = category_text_uniq[3] if len(category_text_uniq)>3 else u''
			price_text = response.xpath('//span[@class="item-price bold"]//text()').extract()
			price = int(price_text[0].strip(u'\xa5 ').replace(',',''))
			item_id = response.meta['item_id']
			area_id = response.meta['area_id']
			#record = (item_id, main_type, mid_type, sub_type, price, area_id)
			#self.c.execute('INSERT INTO iteminfos VALUES (?,?,?,?,?,?)', record)
			l.add_value('item_id',item_id)
			l.add_value('main_type',main_type)
			l.add_value('mid_type',mid_type)
			l.add_value('sub_type',sub_type)
			l.add_value('price_text',price_text)
			l.add_value('price',price)
			l.add_value('area_id',area_id)

			return l.load_item()
