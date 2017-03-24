import sys
import os
import matplotlib.pyplot as plt
import matplotlib

'''
mQ_modified_new_march1
mQ_modified_new_march2
mQ_modified_single
mQ_modified_single_noError
mQ
'''
def makeplot(str4,filename,ct,coup_t,str_save3):
	f = open(str4+filename)
	#f  = open(filename)
	x = []
	y = []
	for line in f:
		line = line.rstrip()
		n = line.split()
		x.append(float(n[0]))
		y.append(float(n[2]))
	#print(x, y)
	#f = plt.figure(1)
	plt.figure()
	if (filename[0:4] == 'p100'):
		plotname ='p100'
	else:
		plotname = filename[0:3]
	matplotlib.style.use('ggplot')
	plt.plot(x, y)
	plt.title(plotname+" new_config "+ct+" ("+coup_t+")", fontsize = 11)
	plt.xlabel("Fraction of edges added")
	plt.ylabel("Modularity value")
	#plt.axis([0,1,0,1])
	#plt.show()
	plt.savefig(str_save3+plotname+".png")
	plt.clf()
	plt.close()


str1 = './new_config_mod/'
mod_type = [d for d in os.listdir(str1) if os.path.isdir(os.path.join(str1, d))]
#mod_type = ["mQ_modified_new_march18"]
commu_type =["multi_layer","single_layer"]
coupling_type=[d for d in os.listdir('./new_config_mod/mQ_modified_single/single_layer/') if os.path.isdir(os.path.join('./new_config_mod/mQ_modified_single/single_layer/', d))]

for mt in mod_type:
	str2 = str1 +mt +'/'
	str_save1 = str2 +'plots/'
	for ct in commu_type:
		str3 = str2+ct +'/'
		str_save2 = str_save1 +ct +'/'
		for coup_t in coupling_type:
			str4 = str3 + coup_t +'/'
			str_save3 = str_save2 +coup_t +'/'
			for filename in os.listdir(str4):
				#makeplot('./mQ/single_layer_0.002_clique/p50.txt')
				if (filename[0]== '.'):
					continue
				makeplot(str4 ,filename,ct,coup_t,str_save3)
		
