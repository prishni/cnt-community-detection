import sys
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

dirname = "./mQ_modified_single_noError/multi_layer_complete_clique/"

def makeplot(filename, dirname):
	#f = open("./mQ_modified_single_noError/multi_layer_complete_clique/"+filename)
	#f  = open(filename)
	f = open(dirname+filename)
	x = []
	y = []
	z = []
	for line in f:
		line = line.rstrip()
		n = line.split()
		x.append(float(n[0]))
		y.append(float(n[2]))
		z.append(float(n[3]))
	#print(x, y)
	#f = plt.figure(1)
	plt.figure()
	plotname = filename[0:3]+"_break_down"
	matplotlib.style.use('ggplot')
	y = np.array(y)
	z = np.array(z)
	w = y + z
	plt.plot(x, y, x, z, x, w)
	plt.title(plotname+" multi_layer_completeBD_clique", fontsize = 11)
	plt.xlabel("Fraction of coupling edges added")
	plt.ylabel("Modularity value")
	plt.axis([0,1,0,1])
	#plt.show()
	plt.savefig("./mQ_modified_single_noError/plots/multi_layer_complete/"+plotname+".png")
	#plt.savefig("../config1.png")
	plt.clf()

makeplot('p70_mQ_modified_single_100_5_config1_no_ext_breakdown.txt', dirname)

''''for filename in os.listdir('./mQ_modified_single_noError/single_layer_0.002_clique'):
	#makeplot('./mQ/multi_layer_0.002_clique/p50.txt')
	if (filename[0]== '.'):
		continue
	makeplot(filename)'''
