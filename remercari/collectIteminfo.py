import time
from scrapinghub import ScrapinghubClient
import restoreItem2Collection as ri2c
import restoreItem2Local as ri2l

APIKEY = 'ec16b94bcf024d0bb502684368658d59'
PROJECTID = '254951'

client = ScrapinghubClient(APIKEY)
myproject = client.projects.get(PROJECTID)

spider = myproject.spiders.get('areainfo')
job = spider.jobs.run()
print "spider areainfo start ..."

while job.metadata.get('state')!='finished':
	time.sleep(30)

print "spider areainfo finished."

spider_id = int(spider.key.split('/')[1])
ri2c.restore(spider_id, 0, 'area_info', 'area_id', 'item_id', 'item_url')
print "item has been restore form spider [areainfo] to collection [area_info]."

spider = myproject.spiders.get('iteminfo')
job = spider.jobs.run()
print "spider iteminfo start ..."

while job.metadata.get('state')!='finished':
	time.sleep(30)

print "spider iteminfo finished."

spider_id = int(spider.key.split('/')[1])
ri2l.restore(spider_id, 0, 'area_id','item_id','main_type','mid_type','sub_type','price','price_text')
print "item has been restore from spider [iteminfo] to local folder [mecadata_iteminfos]."