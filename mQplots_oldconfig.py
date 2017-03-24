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
def makeplot(str4,filename,ct,str_save3):
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
	plt.title(plotname+" config "+ct, fontsize = 11)
	plt.xlabel("Fraction of edges added")
	plt.ylabel("Modularity value")
	#plt.axis([0,1,0,1])
	#plt.show()
	plt.savefig(str_save3+plotname+".png")
	plt.clf()
	plt.close()

def choose_plot_ct(ct):
	if(ct == "multi_layer_0.002_clique"):
		str10 ="multi_layer"

	elif(ct == "multi_layer_complete_clique"):
		str10 ="multi_layer_complete"

	elif(ct == "single_layer_0.002_clique"):
		str10 ="single_layer"
	else:
		str10 ="single_layer_complete"

	return str10


#mod_type = [d for d in os.listdir(str1) if os.path.isdir(os.path.join(str1, d))]
mod_type = ["mQ_modified_march21","mQ_modified_march18","mQ","mQ_modified_march1","mQ_modified_march2","mQ_modified_single","mQ_modified_single_noError"]
str1 = './'
commu_type =["multi_layer_0.002_clique","multi_layer_complete_clique","single_layer_0.002_clique","single_layer_complete_clique"]

for mt in mod_type:
	str2 = str1 +mt +'/'
	str_save1 = str2 +'plots/'
	for ct in commu_type:
		plot_ct = choose_plot_ct(ct)
		str3 = str2+ct +'/'
		str_save2 = str_save1 +plot_ct +'/'
		
		for filename in os.listdir(str3):
			#makeplot('./mQ/single_layer_0.002_clique/p50.txt')
			if (filename[0]== '.'):
				continue
			makeplot(str3 ,filename,ct,str_save2)
	
