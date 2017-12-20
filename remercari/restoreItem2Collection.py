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
 	mycollection = myproject.collections.get_store('area_info')
 	


if __name__ == "__main__":
	try:
		print type(sys.argv[1])
		job_id = int(sys.argv[1])
	except(IndexError):
		job_id = 0
	finally:
		restore(job_id)