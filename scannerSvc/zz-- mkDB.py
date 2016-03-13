import os
import sys
import random
import string
import sqlite3
import itertools

class DB:

	# cursor init#static
	"""INSERT @ +125th posn"""

	@classmethod
	def pseudo_insert(self, fp, **kwargs):
		for _ in kwargs.keys():
			# print("%s\t%s" % (_, kwargs[_]))
			fp.write("%s\t%s\n" % (_, kwargs[_]))
		return

POOL = [
	"abcdefghijklmnopqrstuvwxyz",
	"!#&'()+,-.=@[]_`{}~", #- "\\/:*?\"<>|" -"%$;^"
	"0123456789"	# no uppercase because the permutations were outrageous and... some FSes are case-insensitive :P
]

def init(fp):
	POINT_OF_CHANGE = 1814399//8
	r_int = random.randint
	randSel = lambda pool: pool[r_int(0, len(pool)-1)]
	pool = "".join([
		randSel(  POOL[r_int(0, 2)]  )
		for _ in range(10)
	])
	done = set()
	for aPerm in itertools.permutations(pool, 8):	# 1814399 possibilities
		if aPerm[0] in done:
			if inserts < 125:
				if not r_int(0, 1):	continue
				value = "".join(aPerm)
				DB.pseudo_insert(fp, obfus_code=value)
				inserts+= 1
			else:
				continue
		else:
			done.update(aPerm[0])
			inserts = 0
	return

def main():
	random.seed(a=os.urandom(100), version=2)
	with open("./abc.txt", mode="wt", encoding="UTF-8") as fp:
		init(fp)
	return

if __name__ == '__main__':
	main()
