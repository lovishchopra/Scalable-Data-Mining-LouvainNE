import numpy as np 
import matplotlib.pyplot as plt


prec_harp=[]
count_harp=0
tot_harp=0
with open('fb-cmu/fb-cmu_out_harp.txt','r') as f:
	for line in f:
		t=line.split()
		prec_harp.append(float(t[1]))
		if(int(t[0]) == 1):
			count_harp+=1
		tot_harp+=1



prec_node2vec=[]
count_node2vec=0
tot_node2vec=0
with open('fb-cmu/fb-cmu_out_node2vec.txt','r') as f:
	for line in f:
		t=line.split()
		prec_node2vec.append(float(t[1]))
		if(int(t[0]) == 1):
			count_node2vec+=1
		tot_node2vec+=1


prec_deepwalk=[]
count_deepwalk=0
tot_deepwalk=0
with open('fb-cmu/fb-cmu_out_deepwalk.txt','r') as f:
	for line in f:
		t=line.split()
		prec_deepwalk.append(float(t[1]))
		if(int(t[0]) == 1):
			count_deepwalk+=1
		tot_deepwalk+=1



prec_comm_2=[]
count_comm_2=0
tot_comm_2=0
c=0
with open('fb-cmu/fb-cmu_out_comm_2.txt','r') as f:
	for line in f:
		t=line.split()
		prec_comm_2.append(float(t[1]))
		if(int(t[0]) == 1):
			count_comm_2+=1
		tot_comm_2+=1


prec_comm_2_d=[]
count_comm_2_d=0
tot_comm_2_d=0
with open('fb-cmu/fb-cmu_out_comm_2_deepwalk.txt','r') as f:
	for line in f:
		t=line.split()
		prec_comm_2_d.append(float(t[1]))
		if(int(t[0]) == 1):
			count_comm_2_d+=1
		tot_comm_2_d+=1


prec_comm_4=[]
count_comm_4=0
tot_comm_4=0
c=0
with open('fb-cmu/fb-cmu_out_comm_4.txt','r') as f:
	for line in f:
		t=line.split()
		prec_comm_4.append(float(t[1]))
		if(int(t[0]) == 1):
			count_comm_4+=1
		tot_comm_4+=1



print(float(count_harp)/tot_harp)
print(count_harp, tot_harp)

print(float(count_node2vec)/tot_node2vec)
print(count_node2vec, tot_node2vec)

print(float(count_deepwalk)/tot_deepwalk)
print(count_deepwalk, tot_deepwalk)

print(float(count_comm_2)/tot_comm_2)
print(count_comm_2, tot_comm_2)

print(float(count_comm_2_d)/tot_comm_2_d)
print(count_comm_2_d, tot_comm_2_d)

print(float(count_comm_4)/tot_comm_4)
print(count_comm_4, tot_comm_4)


plt.figure()
plt.plot([i for i in range(tot_harp)][:10000], prec_harp[:10000], linewidth=0.8, linestyle='--', color='k')
plt.plot([i for i in range(tot_node2vec)][:10000], prec_node2vec[:10000], linewidth=0.8, color='r')
plt.plot([i for i in range(tot_deepwalk)][:10000], prec_deepwalk[:10000], linewidth=0.8, color='b')
plt.plot([i for i in range(tot_comm_2)][:10000], prec_comm_2[:10000], linewidth=0.8, color='g')
plt.plot([i for i in range(tot_comm_2_d)][:10000], prec_comm_2_d[:10000], linewidth=0.8, color='y')
plt.plot([i for i in range(tot_comm_4)][:10000], prec_comm_4[:10000], linewidth=0.8, color='m')

plt.legend(['HARP','Node2vec','Deepwalk', 'Method-2(Node2Vec)', 'Method-2(Deepwalk)', 'Method-4(Node2Vec)'])
plt.ylabel('Precision at K value')
plt.xlabel('Number of edges sampled')
plt.title("Precision at K")
plt.savefig('precK_fbcmu.png')
