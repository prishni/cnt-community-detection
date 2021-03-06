#from __future__ import print_function
import random
import itertools	#for calculating n choose 2
import sys
import math as mt
import os
clq_size=100
no_clqs=3
ext=0
layer={}
edges={}
edge_per_clique ={}
couple_edges={}
couple_edges_diff_community ={}
couple_edges_spl={}

for i in range(0,2):							# i denotes the layer number
	start = i*((clq_size+ext)*no_clqs)+1		# start =1,301(start node in each layer)
	layer[i] = set()							# set of node in layer i
	edges[i]=[]									# list of edges in layer i
	edge_per_clique[i] ={}
	p=-1
	for j in range(0,no_clqs):					# j = count of number of cliques in each layer
		edge_per_clique[i][j]=[]
		if j!=0:
			start=end
		end=start+clq_size
		'''
		adding nodes to the list "layer[i]" where i denoted the layer number
		'''
		for m in range(start,end):
		        layer[i].add(m)
			    
			for n in range(start,end):
				'''
				adding all n choose 2 edges to the layer[i] (creating cliques of size 100)
			    '''
				if m<n:
					edges[i].append((m,n))
					edge_per_clique[i][j].append((m,n))
		'''
		didn't understood what ext is
		'''
		prev=random.randint(start,end-1)	
		for m in range(end,end+ext):
			layer[i].add(m)
			edges[i].append((prev,m))
			prev=m
			
		end=end+ext	
		'''
		selecting a node at random so as to connect two cliques in the same layer
		p is the node that will b connected to a node in the second clique
		'''
		if p==-1:
			p=random.randint(start,end-ext-1)
		else:
			current=random.randint(start,end-ext-1)
			edges[i].append((p,current))
			p=random.randint(start,end-ext-1)
		
								 
#print layer
#print edges

start1=1		
start2=((clq_size+ext)*no_clqs)+1			# 301

start_list1 =[]
start_list2=[]
'''
list of starting nodes of each clique in each layer
'''
for i in range(0,no_clqs):
	start_list1.append((i*clq_size)+1)
for i in range(0,no_clqs):
	start_list2.append((i*clq_size)+start2)


for i in range(0,no_clqs):
	end1=start1+clq_size					# stores the next value for start1 i.e (101,201)
	end2=start2+clq_size					# stores the next value for start2 i.e (401,501)
	couple_edges[i]=[]						# list of coupling edges
	couple_edges_spl[i]=[]
	couple_edges_diff_community[i] =[]
	
	'''
	Building complete bipartite connection between the 2 layers
	'''
	for k in range(start1,end1):
		for q in range(start2,end2):
			couple_edges[i].append((k,q))
	
	for k in range(start1,end1):
		for tuple_s in start_list2:
			if tuple_s == start2:
				continue
			for q in range(tuple_s,tuple_s+clq_size):
				couple_edges_diff_community[i].append((k,q))


	
	'''since ext = 0  , so ignore this loop, 
	'''
	for m in range(end1,end1+ext):
		for n in range(end2,end2+ext):
			couple_edges_spl[i].append((m,n))
	'''
	start1 = end1
	start2 = end2
	'''
	start1=end1+ext
	start2=end2+ext									 

'''
copy all edges from the couple_edges lists(fro all the 3 cliques) to a single couple_edge_list list
'''
couple_edge_list=[]
for l in range(0,no_clqs):
	for e in couple_edges[l]:
		couple_edge_list.append(e)	

#print "reached here"

'''
creating the bipartite part
'''
'''
calculating the number of coupling edges to be added out of total coupling edges(300) stored in the couple_edge_list list
'''
ec=0
frac1=0.0
for l in range(0,no_clqs):
	ec+=int(float(len(couple_edges[l]))*frac1)+len(couple_edges_spl[l])

F= 0.7
ec_new_F = int(ec*F)
ec_new_1_F = int(ec - ec_new_F)
e11 =ec_new_F/no_clqs
e12 =ec_new_F/no_clqs
e21 =ec_new_F/no_clqs
e22 =ec_new_1_F/no_clqs
e31 =ec_new_1_F/no_clqs
e32 =ec_new_1_F/no_clqs
towrite =  e11+e12+e21+e22+e31+e32
#print "reached here0"

'''
ec = number to coupling edges to be added
'''

ec=int(float(len(couple_edges[l]))*frac1)*no_clqs
'''
Adding F fraction of coupling edges in the community
'''
edge_set=set()
ec_new_F = int(ec*F)

for a in range(0,no_clqs):
	i=0
	loop_condition = ec_new_F/no_clqs
	while(i<loop_condition):
		#print i
		eindex = random.randint(0, len(couple_edges[a])-1)
		eindex=random.randint(0,len(couple_edges[a])-1)
		for e in couple_edges[a]:
			eindex-=1
			if eindex==0:
				break
		#e = couple_edges[a][eindex]
		if(e not in edge_set):
			edge_set.add(e)
			i = i+1
#print "reached here"

'''
Adding (1-F) fraction of coupling edges in the community
'''
edge_set_diff_comm = set()
ec_new_1_F  = int(ec - ec_new_F)
for a in range(0,no_clqs):
	i=0
	while i< (ec_new_1_F/no_clqs):
		eindex=random.randint(0,len(couple_edges_diff_community[a])-1)
		for e in couple_edges_diff_community[a]:
			eindex-=1
			if eindex==0:
				break
		#e = couple_edges[a][eindex]
		if e not in edge_set_diff_comm:
			edge_set_diff_comm.add(e)
			i=i+1
#print "reached here2"


#F = float(sys.argv[1])

my_list ={}
my_range ={}
for j in range(0,2):
	if j ==0:
		start = start_list1
	else:
		start = start_list2
	my_list[j] = []
	my_range[j] =[]
	print list(range(start[1],start[1]+100)) + list(range(start[2],start[2]+100))
	my_list[j].append(list(range(start[1],start[1]+100)) + list(range(start[2],start[2]+100)))
	my_list[j].append(list(range(start[0],start[0]+100)) + list(range(start[2],start[2]+100)))
	my_list[j].append(list(range(start[1],start[1]+100)) + list(range(start[0],start[0]+100)))
	my_range[j].append(list(range(start[0],start[0]+100)))
	my_range[j].append(list(range(start[1],start[1]+100)))
	my_range[j].append(list(range(start[2],start[2]+100)))

coupling_type=["with_0_coupling","with_0.1_coupling"]
for ct in coupling_type:
	for fraction_filename in range(10, 101, 10):
		for perturb in range(0,101):
			print perturb 
			frac=float(perturb)/100.0
			str1='./new_config_single/'+ct+'/Test_config('+ str(fraction_filename) +'%)/test_config'+str(frac)+'.txt'
			if not os.path.exists('./new_config_single/'+ct+'/Test_config('+ str(fraction_filename) +'%)'):
			    os.makedirs('./new_config_single/'+ct+'/Test_config('+ str(fraction_filename) +'%)')
			fraction = int(fraction_filename)/100.0
			print str1
			fp=open(str1,'w')
			
			#frac2=0.002 #For config3/config5_no_ext we do not consider cliques, so frac2<1.0, for config 1 and 2, frac2 = 1
			fp.write('2\n')


			for l in range(0,2):				#for 2 layers
				'''
				writes all nodes in each layer to a file, layer[l] is a list of nodes in layer l
				'''
				for m in layer[l]:
					fp.write(str(m)+' ') 		
				fp.write('\n')

				# useless since ext= 0
				total_edge = frac*len(edges[l])
				in_commu = int(fraction * total_edge/3)
				out_commu = int(((1-fraction)*total_edge/3)/2)
				s=set()

				for i in range(0,3):
					#print j,i
					x = 0
					while(x<in_commu):
					#for x in range(0,in_commu):
						r=random.randint(0,len(edge_per_clique[l][i])-1)
						#print s,e[0],e[1]
						e = edge_per_clique[l][i][r]
						if e not in s:
							x = x+1
							s.add((e[0],e[1]))
							
					x = 0
					while(x<out_commu):	
					#for x in range(0,out_commu):
						u = random.randint(0,len(my_list[l][i])-1)
						v = random.randint(0,len(my_range[l][i])-1)
						u = my_list[l][i][u]
						v= my_range[l][i][v]
						#print "&&&&&&"
						#print len(my_range[l][i])
						#print v
						e = (u,v)
						e1 = (v,u)
						if e not in s and e1 not in s:
							s.add(e)
							x = x + 1
					
				fp.write(str(len(s))+'\n')
				for e in s:
					fp.write(str(e[0])+' '+str(e[1])+'\n')



				'''***********************************************************
				writing all the edges of all cliques of the layer l to a file
				**************************************************************'''

				'''fp.write(str(len(edges[l]))+'\n')
				for e in edges[l]:
					fp.write(str(e[0])+' '+str(e[1])+'\n')
				'''

			
			fp.write('1\n1 2\n')
			fp.write(str(towrite)+'\n')
			'''
			writing the bipartite part
			'''
			for e in edge_set:
				fp.write(str(e[0])+' '+str(e[1])+'\n')
			
			for e in edge_set_diff_comm:
				fp.write(str(e[0])+' '+str(e[1])+'\n')
			
			
			
			'''while i<ec_new_F:
				eindex=random.randint(0,len(couple_edge_list)-1)
				for e in couple_edge_list:
					eindex-=1
					if eindex==0:
						break
				if e not in edge_set:
					edge_set.add(e)
					fp.write(str(e[0])+' '+str(e[1])+'\n')
				        i=i+1'''
			##########################
			'''
			while (i < ec_new_F/no_clqs):
				print("are you fucking kidding me?!")
				sys.stdout.flush()
				break;
				eindex=random.randint(0,len(couple_edges[a])-1)
				print len(couple_edges[a])
				print "eindex = " +str(eindex)
				#for e in couple_edges[a]:
				#	eindex-=1
				#	if eindex==0:
				#		break
				e = couple_edges[a][eindex]
				print e
				if e not in edge_set:
					print "added"
					edge_set.add(e)
					fp.write(str(e[0])+' '+str(e[1])+'\n')
					fp.write("-------"+str(a)+"\n")
					i=i+1
				'''

			
					

			
			for l in range(0,no_clqs):
				'''
				ec=int(float(len(couple_edges[l]))*frac)
				edge_set=set()
				i=0
				while i<ec:
					eindex=random.randint(0,len(couple_edges[l])-1)
					for e in couple_edges[l]:
						eindex-=1
						if eindex==0:
							break
					if e not in edge_set:
						edge_set.add(e)
						fp.write(str(e[0])+' '+str(e[1])+'\n')
					        i=i+1
				'''	        
				for e in couple_edges_spl[l]:	        
					fp.write(str(e[0])+' '+str(e[1])+'\n')
					
					
			if ext>0:
				fp.write(str(no_clqs*3)+'\n')
			else:
				fp.write(str(no_clqs*2)+'\n')
				
			start1=1
			start2=((clq_size+ext)*no_clqs)+1

			for i in range(0,no_clqs):
				end1=start1+clq_size
				end2=start2+clq_size
					
				for m in range(start1,end1):
					fp.write(str(m)+' ')
				fp.write('\n')	
				
				for m in range(start2,end2):
					fp.write(str(m)+' ')
				fp.write('\n')
				
				for m in range(end1,end1+ext):
					fp.write(str(m)+' ')
				for m in range(end2,end2+ext):
					fp.write(str(m)+' ')
				if ext>0:
					fp.write('\n')
							
				start1=end1+ext
				start2=end2+ext	
										
			fp.close()					
