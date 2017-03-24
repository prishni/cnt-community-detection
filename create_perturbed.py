import random

clq_size=100
no_clqs=3
ext=0
layer={}
edges={}
couple_edges={}
couple_edges_spl={}

for i in range(0,2):
	start=i*((clq_size+ext)*no_clqs)+1
	layer[i]=set()
	edges[i]=[]
	
	p=-1
	for j in range(0,no_clqs):
		if j!=0:
			start=end
		end=start+clq_size
		
		for m in range(start,end):
		        layer[i].add(m)
			for n in range(start,end):
				if m<n:
					edges[i].append((m,n))
		prev=random.randint(start,end-1)			
		for m in range(end,end+ext):
			layer[i].add(m)
			edges[i].append((prev,m))
			prev=m
			
		end=end+ext	
		
		if p==-1:
			p=random.randint(start,end-ext-1)
		else:
			current=random.randint(start,end-ext-1)
			edges[i].append((p,current))
			p=random.randint(start,end-ext-1)
		
								 
#print layer
#print edges

start1=1
start2=((clq_size+ext)*no_clqs)+1

for i in range(0,no_clqs):
	end1=start1+clq_size
	end2=start2+clq_size
	couple_edges[i]=[]
	couple_edges_spl[i]=[]
	
	for j in range(0,clq_size):
		couple_edges[i].append((start1+j,start2+j))
	
	for m in range(end1,end1+ext):
		for n in range(end2,end2+ext):
			couple_edges_spl[i].append((m,n))
	start1=end1+ext
	start2=end2+ext									 
	
couple_edge_list=[]
for l in range(0,no_clqs):
	for e in couple_edges[l]:
		couple_edge_list.append(e)	

for perturb in range(0,101):
	frac=float(perturb)/100.0
	str1='./config5_no_ext/config5_'+str(frac)+'.txt'
	fp=open(str1,'w')
	
	frac2=0.002 #For config3/config5_no_ext we do not consider cliques, so frac2<1.0, for config 1 and 2, frac2 = 1
	fp.write('2\n')
	for l in range(0,2):
		for m in layer[l]:
			fp.write(str(m)+' ')
		fp.write('\n')
		s=set()
		for e in edges[l]:
			r=random.random()
			if r<frac2:
				#print s,e[0],e[1]
				s.add((e[0],e[1]))
		fp.write(str(len(s))+'\n')
		for e in s:
			fp.write(str(e[0])+' '+str(e[1])+'\n')
	
	fp.write('1\n1 2\n')
	
	
	ec=0
	for l in range(0,no_clqs):
		ec+=int(float(len(couple_edges[l]))*frac)+len(couple_edges_spl[l])
	
	fp.write(str(ec)+'\n')
	
	ec=int(float(len(couple_edges[l]))*frac)*no_clqs
	edge_set=set()
	i=0
	while i<ec:
		eindex=random.randint(0,len(couple_edge_list)-1)
		for e in couple_edge_list:
			eindex-=1
			if eindex==0:
				break
		if e not in edge_set:
			edge_set.add(e)
			fp.write(str(e[0])+' '+str(e[1])+'\n')
		        i=i+1
	
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
			
	#For config1/config3/config5-- multilayer ground truth communities
	
	fp.write(str(no_clqs)+'\n')
	
	start1=1
	start2=((clq_size+ext)*no_clqs)+1

	for i in range(0,no_clqs):
		end1=start1+clq_size+ext
		end2=start2+clq_size+ext
			
		for m in range(start1,end1):
			fp.write(str(m)+' ')
		
		for m in range(start2,end2):
			fp.write(str(m)+' ')
		fp.write('\n')
				
		start1=end1
		start2=end2									 
	
	
	#For config2/config4-- single layer ground truth communities
	'''
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
	'''								
	fp.close()					
