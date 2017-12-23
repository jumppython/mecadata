import sys
from scrapinghub import ScrapinghubClient

def restore(job_id):
	APIKEY = 'ec16b94bcf024d0bb502684368658d59'
	PROJECTID = '254951'
	SPIDERID = '1'
	client = ScrapinghubClient(APIKEY)
 	myproject = client.get_project(PROJECTID)
 	if job_id == 0:
 		job_keys = [_['key'] for _ in myproject.jobs.iter()]
 		job_ids = [int(_.split('/')[2]) if _.split('/')[0]==myproject.key else '' for _ in job_keys]
 		myjob_id = sorted(job_ids)[-1]
 	else:
 		myjob_id = id
 	myjob = myproject.jobs.get('%s/%s/%d' % (PROJECTID,SPIDERID,myjob_id))
 	myitem = [_ for _ in myjob.items.iter()]
 	area_ids = [_['area_id'] for _ in myitem]
 	item_ids = [_['item_id'] for _ in myitem]
 	item_urls = [_['item_url'] for _ in myitem]
 	mycollection = myproject.collections.get_store('area_info')
 	item_num = len(myitem)
 	for item_i in range(item_num):
 		area_info_item = dict()
 		area_info_item['area_id'] = area_ids[item_i]
 		area_info_item['item_id'] = item_ids[item_i]
 		area_info_item['item_url'] = item_urls[item_i]
 		mycollection.set({'_key': str(item_i), 'value':area_info_item})


if __name__ == "__main__":
	try:
		print type(sys.argv[1])
		job_id = int(sys.argv[1])
	except(IndexError):
		job_id = 0
	finally:
		restore(job_id)