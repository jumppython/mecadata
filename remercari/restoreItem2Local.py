import sys
import os
import codecs
from datetime import datetime as dt
from scrapinghub import ScrapinghubClient
import restoreItem2Collection as ri2c

def restore(spider_id,job_id=0, *colname):
	APIKEY = 'ec16b94bcf024d0bb502684368658d59'
	PROJECTID = '254951'
	SPIDERID = spider_id
	client = ScrapinghubClient(APIKEY)
	myproject = client.projects.get(PROJECTID)

	if job_id == 0:
		myjob_id = ri2c.obtainLatestJobIDofSpider(APIKEY,PROJECTID,SPIDERID)
	else:
		myjob_id = job_id
	myjob = myproject.jobs.get('%s/%s/%s' % (PROJECTID,SPIDERID,myjob_id))
	myitem = [_ for _ in myjob.items.iter()]
	item_num = len(myitem)
	item_container = dict()
	for n in colname:
		item_container[n] = [_[n] for _ in myitem]

	time_stamp = dt.now().strftime('%Y%m%d%H%M')
	with codecs.open(os.path.join(os.path.expanduser('~'),'Scrapy','mecadata_iteminfos',time_stamp+'_iteminfo.csv'),'w','utf-8') as f:
		for rownum in range(item_num):
			rowcontext = ""
			for n in colname:
				item_context = item_container[n][rownum][0]
				item_context = str(item_context) if type(item_context)==int else item_context
				rowcontext += item_context
				rowcontext += ','
			f.write(rowcontext)
			f.write('\n')

if __name__ == "__main__":
	try:
		spider_id = int(sys.argv[1])
		job_id = int(sys.argv[2])
	except(IndexError):
		spider_id = 1
		job_id = 0
	finally:
		print "SPIDER: %d - JOB: %d" % (spider_id, job_id)
		print "KEYS:"
		print sys.argv[4:]
		restore(spider_id, job_id, *sys.argv[4:])