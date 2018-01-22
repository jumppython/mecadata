#-*- coding: utf-8 -*-

class DataFile:
	# Defind the data file to be processed by:
	#   prefix: String type. If it is datetime string, the value of 'prefix_is_datetime_str' should be set to True.
	#   suffix: String type. If it is datetime string, the value of 'suffix_is_datetime_str' should be set to True.
	#   extension: String type. Designation the extension of file. Default value is '.csv' means CSV file.
	#   By attributes dictionary, other file attributions, such as size, created time, etc, can be declarated for files filter.

	def __init__(self, prefix='', prefix_is_datetime_str=False, suffix='', suffix_is_datetime_str=False, extension='.csv', **attributes):
		self.prefix = prefix
		self.suffix = suffix
		self.prefix_is_datetime_str = prefix_is_datetime_str
		self.suffix_is_datetime_str = suffix_is_datetime_str
		self.extension = extension
		self.attributes = attributes

	def 


def searchNFiles(fld, pattern, N, ascending=True, attribute)