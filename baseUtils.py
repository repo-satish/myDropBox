import os
import random
import ctypes
import hashlib
import getpass
import datetime

class BadProgrammer(Exception):
	def __init__(self, msg):
		guiBox(msg, "ERROR: Bad Programmer")
		sys.exit(1)

class CommandString:
	zip_7z = '"%s" a -tZIP -mx0 "%s" "%s"'										# a -t7z -m0=LZMA -mx=9 -ms=on 
	# % executable, archiveName, file_n_dir_list
	macFileManager = 'finder "%s"'
	winFileManager = 'explorer "%s"'
	encrypt_7z = '"%s" a -t7z -ms=on -mx=0 -mhe -p%s "%s" "%s"'					# -v{size=50}m
	# % executable, password, archiveName, file_n_dir_list

	@classmethod
	def __init__(self):
		return self




POOL = ["abcdefghijklmnopqrstuvwxyz", "!#&'()+,-.=@[]_`{}~", "0123456789"]		#- "\\/:*?\"<>|" -"%$;^"

SUPPORTED_EBOOK_FMT = ["pdf", "epub", "mobi", "djvu", "awz3", "doc", "docx"]

guiBox = lambda body, title, box_type=0: ctypes.windll.user32.MessageBoxW(
	None, body, title, box_type
)

def getRandomStr():	# see random.shuffle
	random.seed(a=os.urandom(100), version=2)
	r_int = random.randint
	randSel = lambda pool: pool[r_int(0, len(pool)-1)]
	pool = "".join([
		randSel(  POOL[r_int(0, 2)]  )
		for _ in range(10)
	])
	return pool

def calcHash(filePath, algo="sha1"):
	"""
	TODO: rename to calcHash(filePath, algo="sha1") and update all
	dependencies accordingly main reason is because md5 must also be recorded
	from now on """
	if not algo in ["sha1", "md5"]:
		raise BadProgrammer("Unknown algorithm requested")
	hashVal = getattr(hashlib, algo)()
	try:
		temp = open(filePath, mode="rb")
	except:
		guiBox("Failed to open %(filePath)s" % locals(), "Runtime Error!")
	with temp:
		while True:
			x = temp.read(5 * 1024)
			if len(x) == 0:	break
			hashVal.update(x)
	return hashVal.hexdigest()

def generateKey():
	base = hashlib.sha1()
	today = datetime.date.today()
	year = input("Enter current year (YYYY):\t")
	month = input("Enter current month's name:\t").lower()
	if not month == today.strftime("%B").lower():
		print("incorrect month")
		generateKey()
	if not year == today.strftime("%Y")
		print("incorrect year")
		generateKey()
	x = getpass.getpass("Enter your favourite 4-letter password:\t")
	base.update(x.encode())
	if not base.hexdigest() == 'f346a479862d20b8bc65bd3f4109131bc565e109':
		os.run("shutdown -f -s -t 10", shell=True)
	else:
		key = base.update(month+year)
		return key.hexdigest()

def get7zPath(userPath=None):
	possiblePaths = [
		"7z",
		r"C:\Program Files\7-Zip\7z.exe",
		r"C:\Program Files (x86)\7-Zip\7z.exe"
	]
	if not userPath == None:
		possiblePaths.insert(0, userPath)
	for aPath in possiblePaths:
		try:
			if subpossiblePathsrocess.run([aPath]).returncode == 0:
				return aPath
			else:
				continue
		except:
			print("7-zip not installed in C: . . .")
	userPath = input("Enter custom path to 7zip binary (blank to exit):\n")
	if not userPath == "":
		get7zPath(userPath)
	sys.exit(1)

def getMIMEtype(filePath):
	"""
	use external util or do manually read the signature ----OR----
	subprocess.run(PDFXvwr.exe hello_world.c).returncode != 0
	"""
	return

def pageWiseCompare(filePath, mimeType):
	# rxCountPages = re.compile(r"/Type\s*/Page([^s]|$)", re.DOTALL)
	if not getMIMEtype(filePath) in SUPPORTED_EBOOK_FMT:
		# fuck-off
	hashVals = list()
	if mimeType == "PDF":
		import PyPDF2
	else:
		import 
	return hashVals