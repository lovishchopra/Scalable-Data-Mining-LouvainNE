import sys
import os
from collections import defaultdict
import glob

print sys.argv

# Form the induced subgraph for nodes in each community in sys.argv[1]
print "Forming induced subgraphs--------------"
#sys.argv[1]=sys.argv[1][11:]
file=sys.argv[1]
print file

ff=open(file,'r')
l=[]
for line in ff:
	t=line.split()
	l.append(int(t[1]))

L=[]
if len(l)==0:
	raise Exception('Empty file')
for j in range(0,max(l)+1):
	L.append([])

ff.close()
'''List L indexed by communities contains list of nodes in corresponding community'''  

ff=open(file,'r')
for line in ff:
	t=line.split()
	L[int(t[1])].append(t[0])
ff.close()

for j in range(0,max(l)+1):
	st1=sys.argv[1][:-8]+str(j)+".txt"
	print "st1=",st1
	c=0
	f1=open(sys.argv[4],'r')
	f2=open(st1,'w')
	for line in f1:
		t=line.split()
		if t[0] in L[j] and t[1] in L[j]:
			c+=1
			f2.write(str(t[0]))
			f2.write(" ")
			f2.write(str(t[1]))
			f2.write("\n")
	nos=len(L[j])
	if nos>1:
		den=float(c)/float(nos*(nos-1))*1.0
	else:
		den=1
	print "Subgraph ",j
	print "Size of community=",len(L[j])
	print "Density of the community subgraph=",den
	f1.close()
	f2.close()

# Renumber the actual node IDs in each subgraph from 0 to n-1

print "Renumber node IDS from 0---------"

for j in range(0,max(l)+1):
	c=0
	l1=[]
	st1=sys.argv[1][:-8]+str(j)+".txt"
	
	exists=os.path.isfile(st1)
	if not exists:
		print "File does not exist"
		continue
	f=open(st1,'r')
	print "Subgraph ",j

	''' File *MapDet.txt contain the edgelist of the subgraph after renumbering from 0 to n-1 '''

	f1=open(st1[:-4]+"-MapDet.txt",'w')
	print st1[:-4]+"-MapDet.txt"
	''' File *Map.txt contains the mapping from actual node IDS in the subgraph to the renumbered node IDS '''

	f2=open(st1[:-4]+"-Map.txt",'w')	
	for line in f:
		t=line.split()
		if t[0] not in l1:
			l1.append(t[0])
		if t[1] not in l1:
			l1.append(t[1])

	for k in range(0,len(l1)):
		f2.write(str(l1[k]))
		f2.write(" ")
		f2.write(str(k))
		f2.write("\n")

	f=open(st1,'r')
	for line in f:
		t=line.split()
		f1.write(str(l1.index(t[0])))
		f1.write(" ")
		f1.write(str(l1.index(t[1])))
		f1.write("\n")


if(max(l)==0):
	sys.exit(0)
	
# Apply Louvain on each subgraph to get its communities

print "Apply Louvain on the subgraphs---------"

for j in range(0,max(l)+1):
	st1=sys.argv[1][:-8]+str(j)

	print "Louvain on Subgraph ",j
	print "st1=",st1
	st="./convert -i"+" "+st1+"-MapDet.txt -o"+" "+st1+".bin"
	os.system(st)
	st="./louvain"+" "+st1+".bin -l -1 -v -q 7 >"+" "+st1+".tree"
	os.system(st)
	st="./hierarchy"+" "+st1+".tree -n >"+" "+st1+"-level.txt"
	os.system(st)
	fl=open(st1+"-level.txt",'r')
	for line in fl:
		t=line.split()
		levels=int(t[0])
	print "Number of levels=",levels

	if levels==0:
		print "Level in subgraph "+str(j)+" is 0"
		continue
	print "Number of levels=",levels
	st="./hierarchy"+" "+st1+".tree -l"+" "+str(levels)+" >"+" "+st1+"_node2comm"
	os.system(st)
	st1=sys.argv[1][:-8]+str(j)+"-Map.txt"
	st2=sys.argv[1][:-8]+str(j)+"_node2comm"
	print "Remapping on subgraph",j
	print "st1=",st1
	print "st2=",st2
	
	exists = os.path.isfile(st2)
	if not exists:
		continue
		raise Exception('File does not exist')
	f=open(st1,'r')
	f1=open(st2,'r')
	d={}
	for line in f:
		t=line.split()
		d[t[1]]=t[0]
	print "Subgraph ",j
	st3=sys.argv[1][:-8]+str(j)+"-RMap.txt"
	pref=int(sys.argv[3])
	suf=int(sys.argv[2])
	st4=sys.argv[1][:pref]
	st4=st4+'temp/'
	lst=sys.argv[1][-suf:]
	st4=st4+lst[:-8]+str(j)+"-RMap.txt"
	'''dash=dict((letter,st3.count(letter)) for letter in set(st3))
	nt=dash['-']
	st4="dump-files/"
	for e in range(0,nt-2):
		st4=st4+"temp/"'''
	f2=open(st4,'w')
	for line in f1:
		t=line.split()
		f2.write(str(d[t[0]]))
		f2.write(" ")
		f2.write(str(t[1]))
		f2.write("\n")
	


# Do a reverse mapping of node IDS from 0 to n-1 to their actual IDs to store node to community in file *-RMap.txt

#print "Remapping the nodes to their original IDS to get node to community-------"

'''for j in range(0,max(l)+1):
	st1=sys.argv[1][:-8]+str(j)+"-Map.txt"
	st2=sys.argv[1][:-8]+str(j)+"_node2comm"
	
	exists = os.path.isfile(st2)
	if not exists:
		raise Exception('File does not exist')
		continue
	f=open(st1,'r')
	f1=open(st2,'r')
	d={}
	for line in f:
		t=line.split()
		d[t[1]]=t[0]
	print "Subgraph ",j
	st3=sys.argv[1][:-8]+str(j)+"-RMap.txt"
	f2=open("dump-files/"+st3,'w')
	for line in f1:
		t=line.split()
		f2.write(str(d[t[0]]))
		f2.write(" ")
		f2.write(str(t[1]))
		f2.write("\n")'''
	

