import numpy as np
import math

# ff=open("karate-harp.txt",'r')
# for line in ff:
# 	t=line.split()

# zro=[]
# hro=[]
# for i in range(0,128):
# 	zro.append(0)
# 	hro.append(0)

# cc=0
# Z=[]
# ff=open("karate-harp.txt",'r')
# for line in ff:
# 	cc+=1
# 	if cc==1:
# 		continue
# 	t=line.split()
# 	z=[]
# 	for i in range(1,len(t)):
# 		z.append(float(t[i]))
# 	Z.append(z)

# Za=np.array(Z)

# Zb=np.mean(Za,axis=0)
# Zv=np.var([Zb],axis=1)

# print Zb
# print Zv

import os
import glob
import sys
from datetime import datetime
startTime=datetime.now()

'''def parse(directory):
	#os.makedirs(directory+'temp/')
	for filename in os.listdir(directory):
		if filename.endswith("-RMap.txt"):
			print "Parsing for file",filename
			os.system("python main.py "+directory+str(filename)+" "+str(len(filename))+" "+str(len(directory))+" "+sys.argv[2])
			#os.system("mv "+directory+str(filename)+" dump/")
	directory=directory+'temp/'
	tifCounter = len(glob.glob1(directory,"*-RMap.txt"))
	if tifCounter>0:
		parse(directory)
	else:
		return'''

directory=sys.argv[1]

'''directory=sys.argv[1]
c=0

while len(os.listdir(directory))>0:
	directory=directory+'temp/'
	c+=1
	if os.path.isdir(directory)==False:
		break


print directory 
print c

directory=directory[:-5]
print directory

c=c-1'''
# c=0
# D={}
# alpha=1
# while len(os.listdir(directory))>0:
# 	for filename in os.listdir(directory):
# 		if filename.endswith("-RMap.txt"):
# 			print "Parsing for file",filename
# 			if c==0:
# 				f=open(directory+filename,'r')
# 				x = np.random.normal(Zb,Zv)
# 				for line in f:
# 					t=line.split()
# 					D[t[0]]=x.tolist()

# 			elif c==1:
# 				f=open(directory+filename,'r')
# 				x = np.random.normal(Zb,Zv)
# 				for line in f:
# 					t=line.split()
# 					D[t[0]]=x.tolist()
			
# 			else:
# 				f=open(directory+filename,'r')
# 				x = np.random.normal(Zb,Zv)
# 				for line in f:
# 					t=line.split()
# 					#print x
# 					y=x.tolist()
# 					z=[]
# 					for i in range(0,len(y)):
# 						z.append(alpha*y[i])
# 					for i in range(0,len(D[t[0]])):
# 						D[t[0]][i]+=z[i]
# 	c+=1
# 	if c>1:
# 		alpha=alpha*0.005
# 	directory=directory+'temp/'

# print "c=",c




c=0
D={}
alpha=1
while len(os.listdir(directory))>0:
	for filename in os.listdir(directory):
		if(filename.endswith("-MapDet.txt") and os.stat(directory+filename).st_size != 0):
			print "Parsing for file",filename
			filename1 = filename.split("MapDet.txt")[0]+"Map.txt"
			if c==0:
				f=open(directory+filename,'r')
				st="python node2vec/src/main.py --input "+directory+filename+" --output node2vec/embed.txt"
				os.system(st)
				f=open("node2vec/embed.txt",'r')
				f1=open(directory+filename1,'r')
				node_map={}
				for line in f1:
					t=line.split()
					node_map[int(t[1])]=int(t[0])
				cc=0
				for line in f:
					cc+=1
					if cc==1:
						continue
					t=line.split()
					z=[]
					for i in range(1,len(t)):
						z.append(float(t[i]))
					D[node_map[int(t[0])]]=z
			
			else:
				f=open(directory+filename,'r')
				st="python node2vec/src/main.py --input "+directory+filename+" --output node2vec/embed.txt"
				os.system(st)
				f=open("node2vec/embed.txt",'r')
				f1=open(directory+filename1,'r')
				node_map={}
				for line in f1:
					t=line.split()
					node_map[int(t[1])]=int(t[0])
				cc=0
				for line in f:
					cc+=1
					if cc==1:
						continue
					t=line.split()
					z=[]
					for i in range(1,len(t)):
						z.append(alpha*float(t[i]))
					for i in range(0,len(D[node_map[int(t[0])]])):
						D[node_map[int(t[0])]][i]+=z[i]
	c+=1
	if c>1:
		alpha=alpha*0.005
	directory=directory+'temp/'

print "c=",c





# c=0
# D={}
# alpha=1
# while len(os.listdir(directory))>0:
# 	for filename in os.listdir(directory):
# 		if(filename.endswith("-MapDet.txt") and os.stat(directory+filename).st_size != 0):
# 			print(directory)
# 			print "Parsing for file",filename
# 			filename1 = filename.split("MapDet.txt")[0]+"Map.txt"
# 			if c==0:
# 				f=open(directory+filename,'r')
# 				# os.system("chmod +x deepwalk/deepwalk/__main__.py")
# 				st="python deepwalk/deepwalk/__main__.py --format edgelist --input "+directory+filename+" --output deepwalk/embed.txt"
# 				os.system(st)
# 				f=open("deepwalk/embed.txt",'r')
# 				f1=open(directory+filename1,'r')
# 				node_map={}
# 				for line in f1:
# 					t=line.split()
# 					node_map[int(t[1])]=int(t[0])
# 				cc=0
# 				for line in f:
# 					cc+=1
# 					if cc==1:
# 						continue
# 					t=line.split()
# 					z=[]
# 					for i in range(1,len(t)):
# 						z.append(float(t[i]))
# 					D[node_map[int(t[0])]]=z
			
# 			else:
# 				f=open(directory+filename,'r')
# 				# os.system("chmod +x deepwalk/deepwalk")
# 				st="python deepwalk/deepwalk/__main__.py --format edgelist --input "+directory+filename+" --output deepwalk/embed.txt"
# 				os.system(st)
# 				f=open("deepwalk/embed.txt",'r')
# 				f1=open(directory+filename1,'r')
# 				node_map={}
# 				for line in f1:
# 					t=line.split()
# 					node_map[int(t[1])]=int(t[0])
# 				cc=0
# 				for line in f:
# 					cc+=1
# 					if cc==1:
# 						continue
# 					t=line.split()
# 					z=[]
# 					for i in range(1,len(t)):
# 						z.append(alpha*float(t[i]))
# 					for i in range(0,len(D[node_map[int(t[0])]])):
# 						D[node_map[int(t[0])]][i]+=z[i]
# 	c+=1
# 	if c>1:
# 		alpha=alpha*0.005
# 	directory=directory+'temp/'

# print "c=",c




'''while c>0:
	if os.path.isdir(directory)==False:
		break
	print c
	for filename in os.listdir(directory):
		if filename.endswith("-RMap.txt"):
			l=[]
			f=open(directory+filename,'r')
			for line in f:
				t=line.split()
				if len(t)==0:
					break
				l.append(t[0])
				l.append(t[1])
			l=list(set(l))
			for x in l:
				for x1 in l:
					if x!=x1 and x1 not in DN[x]:
						DN[x].append(x1)

	c=c-1
	directory=directory[:-5]'''

print "---Time---",datetime.now()-startTime

f1=open(sys.argv[1][:-1]+"-emb_node2vec.txt",'w')
f1.write(str(len(D.keys())))
f1.write(" ")
f1.write(str(128))
for k in D.keys():
	f1.write("\n")
	f1.write(str(k))
	for i in range(0,len(D[k])):
		f1.write(" ")
		f1.write(str(D[k][i]))





