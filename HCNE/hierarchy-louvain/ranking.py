import sys
from datetime import datetime
startTime=datetime.now()

DN={}
f=open(sys.argv[2],'r')
for line in f:
	t=line.split()
	DN[t[0]]=[]
	DN[t[1]]=[]

d1={}
f=open(sys.argv[2],'r')
for line in f:
	t=line.split()
	d1[t[0]]=[]
	d1[t[1]]=[]

f=open(sys.argv[2],'r')
for line in f:
	t=line.split()
	d1[t[0]].append(t[1])
	d1[t[1]].append(t[0])


import os
import pickle


directory=sys.argv[1]
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

#c=c-1


while c>0:
	if os.path.isdir(directory)==False:
		break
	print c
	for filename in os.listdir(directory):
		if filename.endswith("-RMap.txt") or filename.endswith(".tree") or filename.endswith(".bin") or filename.endswith("level.txt") or filename.endswith("-MapDet.txt") or filename.endswith("-Map.txt") or filename.endswith("node2comm"):
			continue
		if filename.endswith(".txt"):
			l=[]
			f=open(directory+filename,'r')
			for line in f:
				t=line.split()
				if len(t)==0:
					break
				l.append(t[0])
				l.append(t[1])
			l=list(set(l))
			'''for x in l:
				for x1 in l:
					if x!=x1 and x1 not in DN[x] and x1 not in d1[x]:
						DN[x].append(x1)'''
			for x in l:
				for x1 in l:
					if x!=x1 and x1 not in DN[x]:
						DN[x].append(x1)

	c=c-1
	directory=directory[:-5]
	

st=sys.argv[1][:-1]
st=st+"-hierarchy-rank.p"
pickle.dump(DN,open(st,"wb"))

'''import pickle
d=pickle.load(open("hierarchy-rank.p","rb"))

for k in d.keys():
	print len(d[k])'''


print "---Time---",datetime.now()-startTime			