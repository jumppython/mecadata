#-*- coding: utf-8 -*-
import glob
import os
from datetime import datetime

class DataFile:
	"""
	Defind the data file to be processed by:
	   prefix: String type. If it is datetime string, the value of 'prefix_is_datetime_str' should be set to True.
	   suffix: String type. If it is datetime string, the value of 'suffix_is_datetime_str' should be set to True.
	   extension: String type. Designation the extension of file. Default value is '.csv' means CSV file.
	"""

	def __init__(self, filepath, extension=None):
		self.__filepath = filepath
		self.__extension = extension
		if extension is not None:
			self.__allfiles = filter(os.path.isfile, glob.glob(filepath+'/*'+extension))
			self.__allfilenames = [os.path.basename(f) for f in self.__allfiles]
		else:
			self.__allfiles = filter(os.path.isfile, glob.glob(filepath+'/*'))
			self.__allfilenames = [os.path.basename(f) for f in self.__allfiles]

	def filepath(self):
		return self.__filepath

	def extension(self):
		return self.__extension

	def allfiles(self):
		return self.__allfiles

	def changeFilepath(self, filepath):
		return DataFile(filepath)

	def changeExtension(self, extension):
		return DataFile(self.__filepath, extension)

	# Filter files by prefix and suffix in folder except subfolder.
	# Designation sort, and by 'name', 'size' or 'date'
	def filterFiles(self, prefix='', suffix='', numlimit=1, ascending=True, bywhat='name'):
		if not bywhat in ['name','size','date']:
			raise ValueError("bywhat must be choosed only from 'name', 'size' and 'date'.")

		purefilenames = [os.path.splitext(f)[0] for f in self.__allfilenames]
		filtered_purefilenames = filterFilenameBySuffix(filterFilenameByPrefix(purefilenames, prefix), suffix)
		if bywhat == 'name':
			filtered_purefilenames.sort() 
		filtered_filenames = [f+self.__extension for f in filtered_purefilenames]
		filtered_files = [os.path.join(self.__filepath,f) for f in filtered_filenames]

		if bywhat == 'name':
			sorted_files = filtered_files
		if bywhat == 'size':
			sorted_files = sorted(filtered_files, key=lambda x: os.path.getsize(x))
		if bywhat == 'date':
			sorted_files = sorted(filtered_files, key=lambda x: os.path.getmtime(x))
		if not ascending:
			sorted_files = sorted_files[::-1]
		limited_files = sorted_files[:numlimit]

		return limited_files

def filterFilenameByPrefix(filelist, prefix):
	if not isinstance(filelist, list):
		raise TypeError("filelist must be a list")
	if not isinstance(prefix, str):
		raise TypeError("prefix must be a str")
	return [f for f in filelist if f.startswith(prefix)]

def filterFilenameBySuffix(filelist, suffix):
	if not isinstance(filelist, list):
		raise TypeError("filelist must be a list")
	if not isinstance(suffix, str):
		raise TypeError("suffix must be a str")
	return [f for f in filelist if f.endswith(suffix)]

if __name__ == '__main__':
	df = DataFile(os.path.join(os.path.expanduser('~'),"Scrapy","mecadata_iteminfos"),'.csv')
	filelist = df.filterFiles(numlimit=8,bywhat='date',ascending=False)
	print filelist
