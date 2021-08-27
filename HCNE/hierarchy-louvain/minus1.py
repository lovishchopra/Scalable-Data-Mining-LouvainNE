import numpy as np 

f=open("prune_BlogCatalog.txt",'r')
f1 = open('prune_BlogCatalog3_m.txt','w')

for line in f:
	t=line.split()
	f1.write(str(int(t[0])-1))
	f1.write(" ")
	f1.write(str(int(t[1])-1))
	f1.write("\n")
