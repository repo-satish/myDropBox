"""
	Runs on the assumption that perfect information is supplied by createDB i.e. dirPath exist and are reachable (no dirs are present)
"""


from Model import DBhandler
from Controller import guiPipe
import basicUtils

import os
from collections import namedtuple

op = os.path

FileParams.__doc__ = """Struct for storing present-state paramaters of a file"""
FileParams = namedtuple("FileParams", [
		"SHA1", "MD5",
		"Size", "Created", "Last_Modifiy", "Last_Access",
		"Name",	"Full_Path"
	])

def insert(fileParams):
	"""
	put values in db and intelligently derive the meaning of situation if data already exists in db
	interact if anamoly
	"""
	# only Created, Last_Access, Name or Full_Path could have changed
	if fileParams.SHA1 in DBhandler.getCursor(column="SHA1"):
		if fileParams.Name in DBhandler.getCursor(column="Name"):
			# ok, the file is internally AND name-eise identical
		else:
			# update db to reflect new name and put old name in array
		if fileParams.

	# new object, could be a modification of an old file or something else
	else:
		if fileParams.Name in DBhandler.getCursor(column="Name"):
			# this might be a revision iff Last_Modifiy mismatches
	return

def get_details_of(filePath):
	x = os.stat(filePath)
	f = FileParams	
	f.SHA1 = basicUtils.calcHash(filePath)
	f.MD5 = basicUtils.calcHash(filePath, algo="MD5")
	f.Name = op.basename(filePath)
	f.Full_Path = op.dirname(filePath)
	f.Size = x.st_size / 1024
	f.Created = x.st_ctime
	f.Last_Modifiy = x.st_mtime
	f.Last_Access = x.st_atime
	return f

def process(fileList):
	for _ in fileList:
		insert(
			get_details_of(_)
		)
	return

def main(dirPath):
	for r, d, f in os.walk(dirPath):
		if ".git" in d:
			d.remove(".git")
			guiPipe.alert_or_notification(type="code_repo", path=r)
		elif ".hg" in d:
			d.remove(".hg")
			guiPipe.alert_or_notification(type="code_repo", path=r)
		f = [op.abspath(op.join(r, _)) for _ in f]
		process(f)
	print("All files in %(dirPath)s scanned and suitably inserted in DataBase . . ." % locals())
	return
