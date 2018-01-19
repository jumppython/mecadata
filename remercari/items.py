# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AreaList(scrapy.Item):
	area_name = scrapy.Field()
	area_url = scrapy.Field()

class ItemList(scrapy.Item):
	item_id = scrapy.Field()
	item_url = scrapy.Field()
	area_id = scrapy.Field()

class ItemInfo(scrapy.Item):
	item_id = scrapy.Field()
	main_type = scrapy.Field()
	mid_type = scrapy.Field()
	sub_type = scrapy.Field()
	price_text = scrapy.Field()
	price = scrapy.Field()
	area_id = scrapy.Field()
	user_url = scrapy.Field()
	user_name = scrapy.Field()
	item_state = scrapy.Field()
	delivery_charge_burden = scrapy.Field()
	delivery_method = scrapy.Field()
	shipment_date_criterion = scrapy.Field()
