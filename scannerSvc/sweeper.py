"""
	recursive, topdown, auto-compress webpages
	zip project folders
	be rude with text files, bring em out
"""

import os

import glueHTM
import projectZipper	# internally calls manage_textFiles.py if asked

def sweep(targetDir):
	glueHTM.silentClean(targetDir)	# recursive=True, topdown=obviously_True
	for r, d, f in os.walk(targetDir):
		if len(d) == 0:
			print("Congratulations!\n`%(targetDir)s` if found to be clean, \
			proceeding . . .")
			return True
		else:
			print("%d directories still found in `%s` after sanitizing \
			webpages and their associated folders" % (len(d), targetDir))
			print("launching Project Zipper utility")
			projectZipper.main(d)
			sweep(targetDir)	# ensure all directories have been removed
	return
