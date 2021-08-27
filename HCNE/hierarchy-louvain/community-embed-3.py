import numpy as np 
import math
import os
import glob
import sys
from datetime import datetime

directory=sys.argv[1]



c=0
D={}
alpha=0.005
while len(os.listdir(directory))>0:

	community_nodes={}
	for filename in os.listdir(directory):
		if(filename.endswith("-RMap.txt") and os.stat(directory+filename).st_size != 0):
			print(filename)
			comm_map={}
			f=open(directory+filename, 'r')
			for line in f:
				t=line.split()
				comm_map[int(t[0])]=int(t[1])

			for file in os.listdir(directory):
				if(file.startswith(filename[:-8]) and file.endswith("-Map_comm.txt") and os.stat(directory+file).st_size != 0):
					f=open(directory+file,'r')
					num_lines = sum(1 for line in f)
					f=open(directory+file,'r')
					for line in f:
						t=line.split()
						if int(t[0]) in community_nodes:
							if int(file[-14]) not in zip(*community_nodes[int(t[0])])[0]:
								community_nodes[int(t[0])].append([int(file[-14]),1])
							else:
								index = zip(*community_nodes[int(t[0])])[0].index(int(file[-14]))
								community_nodes[int(t[0])][index][1] += 1
						else:
							if int(file[-14]) != comm_map[int(t[0])]:
								community_nodes[int(t[0])] = [[comm_map[int(t[0])],num_lines-1], [int(file[-14]),1]]
							else:
								community_nodes[int(t[0])] = [[comm_map[int(t[0])],num_lines]]

	# print(community_nodes)

	for node in community_nodes:
		if(len(community_nodes[node]) > 1):
			s=0
			t=community_nodes[node][0][1]
			for i in range(1, len(community_nodes[node])):
				s += community_nodes[node][i][1]
			for i in range(len(community_nodes[node])):
				if i==0:
					community_nodes[node][i][1] = float(t-s)/float(t)
				else:
					community_nodes[node][i][1] /= float(t)


	for filename in os.listdir(directory):
		if(filename.endswith("-MapDet_comm.txt") and os.stat(directory+filename).st_size != 0):
			print("Parsing for file "+filename)
			filename1 = filename.split("MapDet_comm.txt")[0]+"Map_comm.txt"
			f=open(directory+filename,'r')
			st="python node2vec/src/main.py --input "+directory+filename+" --output node2vec/embed_fbcmu3.txt"
			os.system(st)
			f=open("node2vec/embed_fbcmu3.txt",'r')
			f1=open(directory+filename1,'r')
			node_map={}
			for line in f1:
				t=line.split()
				node_map[int(t[1])]=int(t[0])

			if c==0:
				cc=0
				for line in f:
					cc+=1
					if cc==1:
						continue
					t=line.split()
					z=[]
					node = node_map[int(t[0])]
					for i in range(1,len(t)):
						weight_index = zip(*community_nodes[node])[0].index(int(filename1[-14]))
						weight = community_nodes[node][weight_index][1]
						z.append(weight*float(t[i]))
					if(node in D):
						for i in range(len(D[node])):
							D[node][i]+=z[i]
					else:
						D[node]=z
			
			else:
				cc=0
				for line in f:
					cc+=1
					if cc==1:
						continue
					t=line.split()
					z=[]
					node = node_map[int(t[0])]
					for i in range(1,len(t)):
						weight_index = zip(*community_nodes[node])[0].index(int(filename1[-14]))
						weight = community_nodes[node][weight_index][1]
						z.append(weight*alpha*float(t[i]))
					if(node in D):
						for i in range(0, len(D[node])):
							D[node][i]+=z[i]
					else:
						D[node]=z
	c+=1
	if c>1:
		alpha=alpha*0.005
	directory=directory+'temp/'

print("c="+str(c))



f1=open(sys.argv[1][:-1]+"-emb_comm_3.txt",'w')
f1.write(str(len(D.keys())))
f1.write(" ")
f1.write(str(128))
for k in D.keys():
	f1.write("\n")
	f1.write(str(k))
	for i in range(0,len(D[k])):
		f1.write(" ")
		f1.write(str(D[k][i]))