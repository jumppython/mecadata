#-*- coding: utf-8 -*-
import warnings
import os
from datetime import datetime

class DataFile:
	# Defind the data file to be processed by:
	#   prefix: String type. If it is datetime string, the value of 'prefix_is_datetime_str' should be set to True.
	#   suffix: String type. If it is datetime string, the value of 'suffix_is_datetime_str' should be set to True.
	#   extension: String type. Designation the extension of file. Default value is '.csv' means CSV file.
	#   By attributes dictionary, other file attributions, such as size, created time, etc, can be declarated for files filter.

	def __init__(self, filepath, prefix='', prefix_is_datetime_str=False, suffix='', suffix_is_datetime_str=False, extension='.csv', **attributes):
		self.__filepath = filepath
		self.__prefix = prefix
		self.__suffix = suffix
		self.__prefix_is_datetime_str = prefix_is_datetime_str
		self.__suffix_is_datetime_str = suffix_is_datetime_str
		self.__extension = extension
		self.__attributes = attributes

	def filepath(self):
		return self.__filepath

	def prefix(self):
		return self.__prefix

	def suffix(self):
		return self.__suffix

	def extension(self):
		return self.__extension

	def resetPrefixType(self):
		self.__prefix_is_datetime_str = False

	def resetSuffixType(self):
		self.__suffix_is_datetime_str = False

	def changeFilepath(self, filepath):
		oldone = self.__filepath
		self.__filepath = filepath
		return oldone, self.__filepath

	def changePrefix(self, prefix):
		oldone = self.__prefix
		if self.prefix_is_datetime_str == True:
			warnings.warn("Prefix was not changed, because the value of DataFile.prefix_is_datetime_str attribute is True. " + \
				          "Change prefix with type datetime.datetime, please through the DataFile.setPrefixByDatetime() method." + \
				          "Or please reset the value of DataFile.prefix_is_datetime_str through the DataFile.resetPrefixType() method.")
			return oldone, self.__prefix
		self.__prefix = prefix
		return oldone, self.__prefix

	def changeSuffix(self, suffix):
		oldone = self.__suffix
		if self.suffix_is_datetime_str == True:
			warnings.warn("Suffix was not changed, because the value of DataFile.suffix_is_datetime_str attribute is True. " + \
			              "Change suffix with type datetime.datetime, please through the DataFile.setSuffixByDatetime() method." + \
			              "Or please reset the value of DataFile.suffix_is_datetime_str througn the DataFile.resetSuffixType() method.")
			return oldone, self.__suffix
		self.__suffix = suffix
		return oldone, self.__suffix

	def setPrefixByDatetime(self, oDatetime, pattern):
		if not isinstance(oDatetime, datetime):
			raise TypeError("oDatetime must be a datetime.datetime")
		self.prefix_is_datetime_str = True
		oldone = self.__prefix
		self.__prefix = datetime.strftime(oDatetime, pattern)
		return oldone, self.__prefix

	def setSuffixByDatetime(self, oDatetime, pattern):
		if not isinstance(oDatetime, datetime):
			raise TypeError("oDatetime must be a datetime.datetime")
		self.suffix_is_datetime_str = True
		oldone = self.__suffix
		self.__suffix = datetime.strftime(oDatetime, pattern)
		return oldone, self.__prefix

	def countFiles(self, prefix=None, suffix=None, extension=None, **attributes):
		if prefix is None:
			prefix = self.__prefix
		if suffix is None:
			suffix = self.__suffix
		if extension is None:
			extension = self.__extension

		files = [f for f in os.listdir(self.__filepath) if os.path.isfile(os.path.join(self.__filepath,f))]
		filenames = [f[:-len(extension)] for f in files]
		fileappliedprefix = [f for f in filenames if f.startswith(prefix)]
		fileappliedsuffix = [f for f in fileappliedprefix if f.endswith(suffix)]

		return len(fileappliedsuffix)


def searchNFiles(fld, pattern, N, ascending=True, attribute)