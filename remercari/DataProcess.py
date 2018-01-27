#-*- coding: utf-8 -*-
import warnings
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
		self.__allfiles = [f for f in os.listdir(self.__filepath) if os.path.isfile(os.path.join(self.__filepath, f))]
		if extension is not None:
			self.__allfiles = [f for f in os.listdir(self.__filepath) if f.endswith(extension)]

	def filepath(self):
		return self.__filepath

	def extension(self):
		return self.__extension

	def changeFilepath(self, filepath):
		return DataFile(filepath)

	def changeExtension(self, extension):
		return DataFile(self.__filepath, extension)

	def filterFiles(self, prefix=None, suffix=None, extension=None):
		if extension is None:
			extension = self.__extension

		filenames = [f[:-len(extension)] for f in self.__allfiles]
		filteredfilenames = filterFilenameBySuffix(filterFilenameByPrefix(filenames, prefix), suffix)

		return filteredfilenames

	def searchNFiles(pattern, N, ascending=True, **attribute):



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
