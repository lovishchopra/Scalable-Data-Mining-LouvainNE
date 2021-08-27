'''import os
directory='dump-files/'
for filename in os.listdir(directory):
	print "Parsing for file",filename
	os.system("python main.py dump-files/"+str(filename))

os.mkdir('tempDir')'''

import os
import glob
import sys
from datetime import datetime
startTime=datetime.now()

def parse(directory):
	os.makedirs(directory+'temp/')
	for filename in os.listdir(directory):
		if filename.endswith("-RMap.txt"):
			print "Parsing for file",filename
			os.system("python main.py "+directory+str(filename)+" "+str(len(filename))+" "+str(len(directory))+" "+sys.argv[2])
			#os.system("mv "+directory+str(filename)+" dump/")
	directory=directory+'temp/'
	'''tifCounter = len(glob.glob1(directory,"*-RMap.txt"))
	if tifCounter == 0:
		return 1
	else:'''
	tifCounter = len(glob.glob1(directory,"*-RMap.txt"))
	if tifCounter>0:
		parse(directory)
	else:
		return

directory=sys.argv[1]
x=parse(directory)
print "parsed"

print "---Time---",datetime.now()-startTime