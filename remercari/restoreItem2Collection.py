import sys
from scrapinghub import ScrapinghubClient

def restore(spider_id, job_id=0, store_name='', *keys):
	APIKEY = 'ec16b94bcf024d0bb502684368658d59'
	PROJECTID = '254951'
	SPIDERID = spider_id
	client = ScrapinghubClient(APIKEY)
 	myproject = client.get_project(PROJECTID)

 	if job_id == 0:
 		myjob_id = obtainLatestJobIDofSpider(APIKEY,PROJECTID,SPIDERID)
 		#job_keys = [_['key'] for _ in myproject.jobs.iter()]
 		#job_ids = [int(_.split('/')[2]) if (_.split('/')[0]==myproject.key and _.split('/')[1]==SPIDERID) else '' for _ in job_keys]
 		#myjob_id = sorted(job_ids)[-1]
 	else:
 		myjob_id = id
 	myjob = myproject.jobs.get('%s/%s/%d' % (PROJECTID,SPIDERID,myjob_id))
 	myitem = [_ for _ in myjob.items.iter()]
 	item_num = len(myitem)
 	item_container = dict()
 	for key_i in keys:
 		item_container[key_i] = [_[key_i] for _ in myitem]
 	#area_ids = [_['area_id'] for _ in myitem]
 	#item_ids = [_['item_id'] for _ in myitem]
 	#item_urls = [_['item_url'] for _ in myitem]
 	mycollection = myproject.collections.get_store(store_name)
 	for item_i in range(item_num):
 		area_info_item = dict()
 		for key_i in keys:
	 		area_info_item[key_i] = item_container[key_i][item_i]
 		#area_info_item['area_id'] = area_ids[item_i]
 		#area_info_item['item_id'] = item_ids[item_i]
 		#area_info_item['item_url'] = item_urls[item_i]
 		mycollection.set({'_key': str(item_i), 'value':area_info_item})

def obtainLatestJobIDofSpider(apikey, project_id, spider_id):
 	client = ScrapinghubClient(apikey)
 	myproject = client.projects.get(project_id)
 	job_keys = [_['key'] for _ in myproject.jobs.iter()]
 	job_ids = [int(_.split('/')[2]) if (_.split('/')[0]==myproject.key and _.split('/')[1]==str(spider_id)) else '' for _ in job_keys]
 	job_ids = [_ if type(_) is int else 0 for _ in job_ids]
 	return int(sorted(job_ids)[-1])


if __name__ == "__main__":
	try:
		#print type(sys.argv[1])
		spider_id = int(sys.argv[1])
		job_id = int(sys.argv[2])
		store_name = sys.argv[3]
	except(IndexError):
		spider_id = 1
		job_id = 0
	finally:
		print "SPIDER: %d - JOB: %d - STORE: %s" % (spider_id, job_id, store_name)
		print "KEYS: "
		print sys.argv[4:]
		restore(spider_id, job_id, store_name, *sys.argv[4:])