# import numpy as np 
# import math
# import os
# import glob
# import sys
# from datetime import datetime

# directory=sys.argv[1]



# zro=[]
# hro=[]
# for i in range(0,128):
# 	zro.append(0)
# 	hro.append(0)

# cc=0
# Z=[]
# ff=open("fb-cmu-emb_comm_3.txt",'r')
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





# def recurse(directory, alpha, c, st, graph, D):
# 	if(len(os.listdir(directory)) <= 0):
# 		return

# 	print(st)
# 	community=[]
# 	node2comm={}
# 	for filename in os.listdir(directory):
# 		if(filename.startswith(st) and filename.endswith("-Map.txt") and os.stat(directory+filename).st_size != 0):
# 			print("Parsing for file "+filename)
# 			nodes=[]
# 			subgraph=[]
# 			f = open(directory+filename, 'r')
# 			for line in f:
# 				t=line.split()
# 				node2comm[int(t[0])] = int(filename[-9])
# 				nodes.append(int(t[0]))
# 			community.append((filename[-9], nodes))  # storing (community no., list of nodes)

# 			filename1 = filename.split("-Map.txt")[0]+".txt"
# 			f = open(directory+filename1, 'r')
# 			for line in f:
# 				t=line.split()
# 				subgraph.append((int(t[0]), int(t[1])))

# 			recurse(directory+'temp/', alpha*0.005, c+1, filename1[:-4], subgraph, D)
		

# 	weighted_graph={}
# 	if(len(node2comm) > 0):
# 		for edge in graph:
# 			# print(edge)
# 			comm1 = node2comm[edge[0]]
# 			comm2 = node2comm[edge[1]]
# 			if(comm2 < comm1):
# 				temp=comm2
# 				comm2=comm1
# 				comm1=temp

# 			if((comm1, comm2) in weighted_graph):
# 				weighted_graph[(comm1, comm2)]+=1
# 			else:
# 				weighted_graph[(comm1, comm2)]=1


# 	new_filename='graph.txt'
# 	print(new_filename)
# 	f=open(new_filename, 'w')
# 	for key in weighted_graph:
# 		f.write(str(key[0])+' '+str(key[1])+' '+str(weighted_graph[key])+'\n')
# 	f.close()

# 	f = open(new_filename, 'r')
# 	count_line=0
# 	for line in f:
# 		count_line+=1
# 		if(count_line > 0):
# 			break

# 	if(count_line==0):
# 		if(c==0):
# 			z = np.random.normal(Zb,Zv).tolist()
# 			for comm in community:
# 				for node in comm[1]:
# 					if(node in D):
# 						for i in range(0, len(D[node])):
# 							D[node][i]+=z[i]
# 					else:
# 						D[node]=z
# 		else:
# 			x=np.random.normal(Zb,Zv).tolist()
# 			z=[]
# 			for i in range(0,len(x)):
# 				z.append(alpha*x[i])
# 			for comm in community:
# 				for node in comm[1]:
# 					if(node in D):
# 						for i in range(0, len(D[node])):
# 							D[node][i] += z[i]
# 					else:
# 						D[node] = z
# 	else:
# 		st="python deepwalk/deepwalk/__main__.py --format edgelist --input "+directory+filename+" --output deepwalk/embed_enron.txt"
# 		os.system(st)
# 		f=open("deepwalk/embed_enron.txt",'r')

# 		if(c==0):
# 			cc=0
# 			for line in f:
# 				cc+=1
# 				if cc==1:
# 					continue
# 				t=line.split()
# 				z=[]
# 				for i in range(1,len(t)):
# 					z.append(float(t[i]))
# 				for comm in community:
# 					if(int(comm[0]) == int(t[0])):
# 						for node in comm[1]:
# 							if(node in D):
# 								for i in range(0, len(D[node])):
# 									D[node][i]+=z[i]
# 							else:
# 								D[node]=z
# 		else:
# 			cc=0
# 			for line in f:
# 				cc+=1
# 				if cc==1:
# 					continue
# 				t=line.split()
# 				z=[]
# 				for i in range(1,len(t)):
# 					z.append(alpha*float(t[i]))
# 				for comm in community:
# 					if(int(comm[0]) == int(t[0])):
# 						for node in comm[1]:
# 							if(node in D):
# 								for i in range(0, len(D[node])):
# 									D[node][i] += z[i]
# 							else:
# 								D[node] = z




# f = open(directory[:-1]+".txt", 'r')
# graph=[]
# for line in f:
# 	t = line.split()
# 	graph.append((int(t[0]), int(t[1])))

# st = directory[:-1]+"-1"

# D={}
# recurse(directory, 1, 0, st, graph, D)


# f1=open(sys.argv[1][:-1]+"-emb_comm_1_deepwalk.txt",'w')
# f1.write(str(len(D.keys())))
# f1.write(" ")
# f1.write(str(128))
# for k in D.keys():
# 	f1.write("\n")
# 	f1.write(str(k))
# 	for i in range(0,len(D[k])):
# 		f1.write(" ")
# 		f1.write(str(D[k][i]))





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
					for line in f:
						t=line.split()
						if int(t[0]) in community_nodes:
							if int(file[-14]) not in community_nodes[int(t[0])]:
								community_nodes[int(t[0])].append(int(file[-14]))
						else:
							if int(file[-14]) != comm_map[int(t[0])]:
								community_nodes[int(t[0])] = [comm_map[int(t[0])], int(file[-14])]
							else:
								community_nodes[int(t[0])] = [comm_map[int(t[0])]]


	for filename in os.listdir(directory):
		if(filename.endswith("-MapDet_comm.txt") and os.stat(directory+filename).st_size != 0):
			print("Parsing for file "+filename)
			filename1 = filename.split("MapDet_comm.txt")[0]+"Map_comm.txt"
			f=open(directory+filename,'r')
			st="python deepwalk/deepwalk/__main__.py --format edgelist --input "+directory+filename+" --output deepwalk/embed_pkar.txt"
			os.system(st)
			f=open("deepwalk/embed_pkar.txt",'r')
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
						if community_nodes[node].index(int(filename1[-14])) > 0:
							z.append(alpha*float(t[i]))
						else:
							z.append(float(t[i]))
					if(node in D):
						for i in range(0, len(D[node])):
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
						if community_nodes[node].index(int(filename1[-14])) > 0:
							z.append(alpha*alpha*float(t[i]))
						else:
							z.append(alpha*float(t[i]))

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



f1=open(sys.argv[1][:-1]+"-emb_comm_2_deepwalk.txt",'w')
f1.write(str(len(D.keys())))
f1.write(" ")
f1.write(str(128))
for k in D.keys():
	f1.write("\n")
	f1.write(str(k))
	for i in range(0,len(D[k])):
		f1.write(" ")
		f1.write(str(D[k][i]))