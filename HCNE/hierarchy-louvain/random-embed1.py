import numpy as np
import math

zro=[]
hro=[]
for i in range(0,128):
	zro.append(0)
	hro.append(0)

cc=0
Z=[]
ff=open("fb-cmu-harp.txt",'r')
for line in ff:
	cc+=1
	if cc==1:
		continue
	t=line.split()
	z=[]
	for i in range(1,len(t)):
		z.append(float(t[i]))
	Z.append(z)

Za=np.array(Z)

Zb=np.mean(Za,axis=0)
Zv=np.var([Zb],axis=1)

print(Zb)
print(Zv)



import os
import glob
import sys
from datetime import datetime
startTime=datetime.now()


directory=sys.argv[1]

c=0
D={}
alpha=1
while len(os.listdir(directory))>0:
	for filename in os.listdir(directory):
		if filename.endswith("-RMap.txt"):
			print("Parsing for file "+filename)
			if c==0:
				f=open(directory+filename,'r')
				x = np.random.normal(Zb,Zv)
				for line in f:
					t=line.split()
					D[t[0]]=x.tolist()

			elif c==1:
				f=open(directory+filename,'r')
				x = np.random.normal(Zb,Zv)
				for line in f:
					t=line.split()
					D[t[0]]=x.tolist()
			
			else:
				f=open(directory+filename,'r')
				x = np.random.normal(Zb,Zv)
				for line in f:
					t=line.split()
					#print x
					y=x.tolist()
					z=[]
					for i in range(0,len(y)):
						z.append(alpha*y[i])
					for i in range(0,len(D[t[0]])):
						D[t[0]][i]+=z[i]
	c+=1
	if c>1:
		alpha=alpha*0.005
	directory=directory+'temp/'

# print("c="+str(c))




# c=0
# D={}
# alpha=1
# while len(os.listdir(directory))>0:
# 	for filename in os.listdir(directory):
# 		if(filename.endswith("-MapDet.txt") and os.stat(directory+filename).st_size != 0):
# 			print("Parsing for file "+filename)
# 			filename1 = filename.split("MapDet.txt")[0]+"Map.txt"
# 			if c==0:
# 				f=open(directory+filename,'r')
# 				st="python node2vec/src/main.py --input "+directory+filename+" --output node2vec/embed_penron.txt"
# 				os.system(st)
# 				f=open("node2vec/embed_penron.txt",'r')
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
# 				st="python node2vec/src/main.py --input "+directory+filename+" --output node2vec/embed_penron.txt"
# 				os.system(st)
# 				f=open("node2vec/embed_penron.txt",'r')
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

# print("c="+str(c))





# c=0
# D={}
# alpha=1
# while len(os.listdir(directory))>0:
# 	for filename in os.listdir(directory):
# 		if(filename.endswith("-MapDet.txt") and os.stat(directory+filename).st_size != 0):
# 			print(directory)
# 			print("Parsing for file "+filename)
# 			filename1 = filename.split("MapDet.txt")[0]+"Map.txt"
# 			if c==0:
# 				f=open(directory+filename,'r')
# 				# os.system("chmod +x deepwalk/deepwalk/__main__.py")
# 				st="python deepwalk/deepwalk/__main__.py --format edgelist --input "+directory+filename+" --output deepwalk/embed_penron.txt"
# 				os.system(st)
# 				f=open("deepwalk/embed_penron.txt",'r')
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
# 				st="python deepwalk/deepwalk/__main__.py --format edgelist --input "+directory+filename+" --output deepwalk/embed_penron.txt"
# 				os.system(st)
# 				f=open("deepwalk/embed_penron.txt",'r')
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

# print("c="+str(c))



f1=open(sys.argv[1][:-1]+"-emb_rand.txt",'w')
f1.write(str(len(D.keys())))
f1.write(" ")
f1.write(str(128))
for k in D.keys():
	f1.write("\n")
	f1.write(str(k))
	for i in range(0,len(D[k])):
		f1.write(" ")
		f1.write(str(D[k][i]))





