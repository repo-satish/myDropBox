"""
	what about local scan n universal scan?
"""


# import mongo	# how to ensure 'unique'
import sqlite3

class DB:

	# static vars

	@classmethod
	def init_DB(self, filePath):
		# self.
		return False

	@classmethod
	def is_unique(self, obfus_name):	
		"""? convert to kwargs"""
		# return true only if obfus_name doesn't exist in db already
		if True:
			return True
		return False

	@classmethod
	def insert(self, obfus_name, file_path):
		"""
		determines all other parameters by itself, yes it repeats the entire
		ensureFresh() process but that is good only """
		import json
		print(json.dumps(kwargs, sort_keys=True, indent=4))
		return True

	@classmethod
	def query(self, **kwargs):
		return

	@classmethod
	def close_DB(self):
		return False




"""
------------------C:\Users\z\Desktop\code\uploader\sa\Model\------------------
class Mongo():
class SQLite3():

from collections import namedtuple

FileObject = namedtuple("FileObject", [
		"",
	])
FileObject.__doc__ = "struct FileObject stores everything about a file"
		

def getCursor(column):
	"
	returns an iterable variable that contains/pointed-to by column name
	if column data type is array - it returns list of 0th element of each entry
	"
	return ??

def getElement(*args):
	if CONFLICTING INFO FOUND:	# like city="New York", country="Russia"
		raise FatalDBbackendError
	return
"""




class UploadJob:	# could be a namedtuple
	"""
	{"new":[filePath], "version/diff":[{"u_id":newVerPath/BSON}]}
	{
		"new": [filePath]
		"version|diff": [
			{}
		]
	}
	"""

	src_path = str()
	dest_path = str()	# both - the deeply nested directory and the obfuscated name

	def __init__(self):
		return self
