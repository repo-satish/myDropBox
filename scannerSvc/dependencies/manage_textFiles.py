"""
	recursively traverse given directory, if text files (check mime type of
	extensionless files) found in this directory, zip.STORE them /*inside
	zipfile("./content/") and add zipfile("./info.txt") which contains
	abspath, times etc. etc. for naming do*/
	"text_file_bundle(hhmmssyymmdd).zip"
"""

import os
import shlex
from concurrent.futures import ThreadPoolExecutor

import baseUtils # can it do that ???

path_7z, command = None, None

def _filterOut(fileList):
	answer = list()
	for _ in files:
		if baseUtils.getMIMEtype(_)=="txt":
			if _.endswith(".txt") or _.endswith(".text"):
				answer.append(_)
			else:
				continue
	return answer

def compress(archiveName, fileList):
	# global command#SINCE VALUE AINT CHANGING
	temp = command % (path_7z, archiveName, '" "'.join(fileList))
	input(temp)
	subprocess.run(shlex.split(temp))
	return

def main(targetDir):
	global path_7z, command
	path_7z = baseUtils.get7zPath()
	command = baseUtils.CommandString.zip_7z
	archiveNames, fileLists = list(), list()
	targetDir = os.path.abspath(targetDir)
	for root, dirs, files in os.walk(targetDir,
	topdown=True, onerror=None, followlinks=False):
		files = [os.path.join(root, _) for _ in files]
		files = _filterOut(files)
		if len(files) == 0:	continue
		archiveName = os.path.basename(root, files)
		fileLists.append(files)
		archiveNames.append(archiveName)
	with ThreadPoolExecutor(max_workers=6) as multi:
		multi.map(compress, archiveNames, fileLists)
	return
