import os
import shlex
import subprocess
from concurrent.futures import ThreadPoolExecutor as a

import baseUtils # can it do that ???

path_7z, command = None, None

def run_7z(webpageName, fileList, prefix=None):
	# global command#SINCE VALUE AINT CHANGING
	archiveName = "HTM--- " + webpageName + ".htmz"
	if not prefix == None:
		archiveName = prefix + archiveName
	temp = command % (path_7z, archiveName, '" "'.join(fileList))
	subprocess.run(shlex.split(temp))
	return

def incompleteCompress(baseFullPath):
	dirName = baseFullPath+"_files"
	run_7z(webpageName=baseFullPath, fileList=[dirName], prefix="(incomplete) ")
	subprocess.run('rd /s /q "%(dirName)s"' % locals())
	return

def completeCompress(baseFullPath, ext):
	dirName = baseFullPath+"_files"
	fileName = baseFullPath+ext
	run_7z(webpageName=baseFullPath, fileList=[fileName, dirName])
	subprocess.run('del /q "%(fileName)s"'% locals())
	subprocess.run('rd /s /q "%(dirName)s"' % locals())
	return

def decide_n_compress(aDir):
	# if os.path.isfile(aDir+".htm"):	completeCompress(aDir, ext=".htm")
	# elif os.path.isfile(aDir+".html"):	completeCompress(aDir, ext=".html")
	if os.path.isfile(aDir+".htm") or os.path.isfile(aDir+".html"):
		completeCompress(aDir, ext=".htm*")
	else:
		incompleteCompress(aDir)
	return

def silentClean(targetDir):
	global path_7z, command
	path_7z = baseUtils.get7zPath()
	command = baseUtils.CommandString.zip_7z
	targetDir = os.path.abspath(targetDir)
	for root, dirs, files in os.walk(targetDir,
	topdown=True, onerror=None, followlinks=False):
		dirs = [os.path.join(root, _) for _ in dirs]
		dirs = [_.replace("_files", "") for _ in dirs]
		with a(max_workers=5) as manyThreads:			# inside for loop to ensure recursive-ly found webpages are also cleaned
			manyThreads.map(decide_n_compress, dirs)
	return
