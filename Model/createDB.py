"""
	If this is being run for the first time, then:
		create - .paths_to_scan file in a standard place
	If .paths_to_scan exists then call scan.py
	ALSO,
		make sure no subdirectories are present cuz that will break the rule of management i.e.
		C:/a/b/c/	OK
		D:/e/k/		OK
		D:/e/f/g/	OK
		D:/e/f/g/x	NOT OK
"""

import scan
import basicUtils
import View
from dirScanner import ?? as nextStep

import os
import sys
import platform


def firstRunQ(os_name):
	"""
	checks if .paths_to_scan exists in "standard place" in os specific manner
	if exists return the path else return none
	"""
	if os_name is "Linux":
		supposedPath = ?TO_DO?
	elif os_name is "Mac OS X":
		supposedPath = ?TO_DO?
	elif os_name is "BSD":
		supposedPath = ?TO_DO?
	elif os_name is "Windows":
		supposedPath = subprocess.check_output(["echo", "%appdata%"], shell=True).decode().strip()
	else:
		raise basicUtils.UnknownOS
	return supposedPath

def main():
	supposedPath = firstRunQ(basicUtils.detectOS())
	dirsFile = os.path.join(supposedPath, ".paths_to_scan")
	if os.path.isfile(dirsFile) is False:
		ch = View.CLI.get_input("This seems to be the first run as no `paths_to_scan` information is found, would you like that this app remembers paths to directories you track?")
		if ch in "yY":
			# create file pointed by dirsFile
		else:
			break # ask for dirPath list
	else:
		with open(dirsFile, mode="rt", encoding="UTF-8") as temp:
			dirs = temp.readlines()
		del temp
		View.CLI._print("Following directories will be scanned:")
		for _ in dirs:
			View.CLI._print(_)
	inData = View.CLI.get_input("Input, if any, list of directories you want to be scanned from now on else just press enter, directory list input method like so:")
	# View.CLI._print("\"path/to/dir1\", \"path/to/dir2\"")
	if inData == '':
		pass
	else:
		validPaths = list()
		for _ in inData.split(","):
			if os.path.isdir(_):	validPaths.append(_)
		with open(dirsFile, mode="at", encoding="UTF-8") as temp:
			temp.write("\n".join(validPaths))
	for _ in dirs+validPaths:	# variab;e undefinec error if no ELSE block is entered
		dirScanner.generateReport(_)
	return 0

if __name__ == '__main__':
	main()