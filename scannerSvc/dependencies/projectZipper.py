"""
	+ open a folder x in explorer
	+ instruct user to move all files and directories that belong to a certain
	(one-and-only-one) PROJECT/COURSE i.e. files(and directories) which were
	an integral part of that project/course when it was downloaded (SUGGESTED:
	send notes seprately as a version) to a new sub-folder in ThisTopLevelDir
	with desired name starting with either '@PROJECT-- ' or '@COURSE-- '
	+ ask would you like to call 'manage_textFiles.py' before projectZippper starts?
	+ zipup all folders with name starting as mentioned above, with
	troubleshooted name i.e. ensuring OS_name_already_exists error when moving
	zipped file to "./..". Zipping is done at STORE	level compression
"""

import os
import sys
import shlex
import subprocess

import baseUtils # can it do that ???

path_7z, command, view = None, None, None

def do_it(dirList, dest):			# can be ThreadPoolExecutor-er multi-threaded but won't improve performance much . . .
	for r, d, f in os.walk(dest):	break
	f = [_.lower() for _ in f]		# fucking case-insenetive file systems
	for aDir in dirList:
		if aDir.startswith("@PROJECT-- ") or aDir.startswith("@COURSE-- "):
			if aDir.lower()+".zip" in f:
				print("Name clash would occour, kindly rename %(aDir)s and \
				press enter to continue" % locals())
				do_it(dirList, dest)
			temp = command % (path_7z, aDir+".zip", aDir)
		else:
			continue
		subprocess.run(shlex.split(temp))
		subprocess.run('move "%s" ..' % aDir+".zip")	# check return code???
		subprocess.run('rd /s /q "%(aDir)s"' % locals())
	return

def do(targetDir):
	instructions = """
	You must move all files and directories that belong to a certain
	(one-and-only-one) PROJECT or COURSE* to a new sub-folder created here
	itself (in %s).
	You may give it any desired name but it __must__ start with either '@PROJECT--
	' or '@COURSE-- ' depending upon the nature of content.

	*  i.e. files(and directories) which were an integral part of that project or
		course when it was downloaded**
	** SUGGESTED: send notes seprately as a version
	"""
	baseUtils.guiBox(instructions % targetDir, "Important instructions . . .")
	# proc = subprocess.Popen(shlex.split(view % targetDir))	# wait till previous pid is finished,, subprocess
	# while True:
	# 	proc.pid(6)
	waiter = input("Input 'done' when you are finished with the tasks . . .")
	if not waiter == "done":	# implement 'q' to quit program
		do(targetDir)
	for r, d, f in os.walk(targetDir):		break
	do_it(dirList=d, dest=os.path.join(targetDir, ".."))
	return

def main(dirList):
	global path_7z, command, view
	path_7z = baseUtils.get7zPath()
	command = baseUtils.CommandString.zip_7z
	view = baseUtils.CommandString.winFileManager
	for aDir in dirList:
		if os.path.isdir(aDir):
			do(targetDir)
		else:
			print("Bad path: `%(aDir)s`" % locals())
			continue
	return

if __name__ == '__main__':
	main(sys.argv[1:])
