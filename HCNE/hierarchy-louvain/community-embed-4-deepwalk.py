import numpy as np 
import math
import os
import glob
import sys
from datetime import datetime

directory=sys.argv[1]


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




c=0
D={}
alpha=0.005
while len(os.listdir(directory))>0:
	D1={}

	community_nodes={}
	for filename in os.listdir(directory):
		if(filename.endswith("-RMap.txt") and os.stat(directory+filename).st_size != 0):
			length = len(filename[:-8])
			print(filename)
			comm_map={}
			f=open(directory+filename, 'r')
			for line in f:
				t=line.split()
				comm_map[int(t[0])]=int(t[1])

			for file in os.listdir(directory):
				if(file.startswith(filename[:-8]) and file.endswith("-Map_comm.txt") and os.stat(directory+file).st_size != 0):
					f=open(directory+file,'r')
					for line in f:
						t=line.split()
						if int(t[0]) in community_nodes:
							if int(file[length:-13]) not in community_nodes[int(t[0])]:
								community_nodes[int(t[0])].append(int(file[length:-13]))
						else:
							if int(file[length:-13]) != comm_map[int(t[0])]:
								community_nodes[int(t[0])] = [comm_map[int(t[0])], int(file[length:-13])]
							else:
								community_nodes[int(t[0])] = [comm_map[int(t[0])]]



	for filename in os.listdir(directory):
		if(filename.endswith("-MapDet_comm.txt") and os.stat(directory+filename).st_size != 0):
			print("Parsing for file "+filename)
			filename1 = filename.split("MapDet_comm.txt")[0]+"Map_comm.txt"
			st="python deepwalk/deepwalk/__main__.py --format edgelist --input "+directory+filename+" --output deepwalk/embed_fbcmu4.txt"
			os.system(st)
			f=open("deepwalk/embed_fbcmu4.txt",'r')
			f1=open(directory+filename1,'r')
			node_map={}
			for line in f1:
				t=line.split()
				node_map[int(t[1])]=int(t[0])

			community_number = int(filename[int(filename[:int(filename.rindex('-'))].rindex('-'))+1:int(filename.rindex('-'))])

			f1 = open(directory+filename, 'r')

			if c==0:
				for line in f1:
					t = line.split()
					node1=node_map[int(t[0])]
					node2=node_map[int(t[1])]
					if(community_nodes[node1][0] != community_nodes[node2][0]):
						if (node1 not in D1) and (node2 not in D1):
							z = np.random.normal(Zb,Zv).tolist()
							D1[node1]=z
							D1[node2]=z
						elif (node1 in D1) and (node2 not in D1):
							D1[node2]=D1[node1]
						elif (node1 not in D1) and (node2 in D1):
							D1[node1]=D1[node2]
						else:
							for i in range(len(D1[node1])):
								a=(D1[node1][i]+D1[node2][i])/2
								D1[node1][i]=a
								D1[node2][i]=a
				cc=0	
				for line in f:
					cc+=1
					if cc==1:
						continue
					t=line.split()
					z=[]
					node = node_map[int(t[0])]
					for i in range(1,len(t)):
						if community_nodes[node].index(community_number) > 0:
							z.append(alpha*float(t[i]))
						else:
							z.append(float(t[i]))
					if(node in D):
						if(node in D1):
							print(len(z), len(D1[node]))
							for i in range(len(D[node])):
								D[node][i]+=(0.8*z[i]+0.2*D1[node][i])
						else:
							for i in range(0, len(D[node])):
								D[node][i]+=z[i]
					else:
						if(node in D1):
							emb=[]
							for i in range(len(D1[node])):
								emb.append(0.8*z[i]+0.2*D1[node][i])
							D[node]=emb
						else:
							D[node]=z
			
			else:
				for line in f1:
					t = line.split()
					node1=node_map[int(t[0])]
					node2=node_map[int(t[1])]
					if(community_nodes[node1][0] != community_nodes[node2][0]):
						if (node1 not in D1) and (node2 not in D1):
							z = np.random.normal(Zb,Zv).tolist()
							D1[node1]=z
							D1[node2]=z
						elif (node1 in D1) and (node2 not in D1):
							D1[node2]=D1[node1]
						elif (node1 not in D1) and (node2 in D1):
							D1[node1]=D1[node2]
						else:
							for i in range(len(D1[node1])):
								a=(D1[node1][i]+D1[node2][i])/2
								D1[node1][i]=a
								D1[node2][i]=a
				cc=0
				for line in f:
					cc+=1
					if cc==1:
						continue
					t=line.split()
					z=[]
					node = node_map[int(t[0])]
					for i in range(1,len(t)):
						if community_nodes[node].index(community_number) > 0:
							z.append(alpha*alpha*float(t[i]))
						else:
							z.append(alpha*float(t[i]))

					if(node in D):
						if(node in D1):
							for i in range(len(D[node])):
								D[node][i]+=(0.8*z[i]+0.2*alpha*D1[node][i])
						else:
							for i in range(0, len(D[node])):
								D[node][i]+=z[i]
					else:
						if(node in D1):
							emb=[]
							for i in range(len(z)):
								emb.append(0.8*z[i]+0.2*alpha*D1[node][i])
							D[node]=emb
						else:
							D[node]=z
	c+=1
	if c>1:
		alpha=alpha*0.005
	directory=directory+'temp/'

print("c="+str(c))



f1=open(sys.argv[1][:-1]+"-emb_comm_4_deepwalk.txt",'w')
f1.write(str(len(D.keys())))
f1.write(" ")
f1.write(str(128))
for k in D.keys():
	f1.write("\n")
	f1.write(str(k))
	for i in range(0,len(D[k])):
		f1.write(" ")
		f1.write(str(D[k][i]))