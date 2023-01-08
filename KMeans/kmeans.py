import csv
import math
import random
import matplotlib.pyplot as plt

class Point:

	def __init__(self,x,y):
	
		self.x = x
		self.y = y
		self.dis = 0
		self.cluster = ()
		
	def __str__(self):
	
		return "\n({0},{1})\nDistance : {2}\nCluster : {3}".format(self.x,self.y,self.dis,self.cluster)

class Cluster:

	def __init__(self,x,y):
	
		self.x = x
		self.y = y
					
	def __eq__(self,obj):
	
		return self.x == obj.x and self.y == obj.y

	def __str__(self):
	
		return "({0},{1})".format(self.x,self.y)

def createpointlist(filename):

	csvobj = csv.reader(open(filename,"r"))
	
	pointlist = []
	
	for row in csvobj:
	
		pointlist.append(Point(float(row[0]),float(row[1])))
		
	return pointlist


def finddis(p1,p2):

	dis = (p1.x - p2.x)**2 + (p1.y - p2.y)**2
	
	return math.sqrt(dis)


def findbestcluster(pointlist,clusterlist):

	for point in pointlist:
	
		mindis = finddis(point,clusterlist[0])
		clusterid = 0
		
		for i in range(1,len(clusterlist)):
		
			dis = finddis(point,clusterlist[i])
		
			if(dis < mindis):
			
				mindis = dis
				clusterid = i
				
		point.dis = mindis
		point.cluster = Cluster(clusterlist[clusterid].x,clusterlist[clusterid].y)


def findnewclusters(pointlist,clusterlist):

	newclusterlist = []

	for cluster in clusterlist:
	
		xsum = 0
		ysum = 0
		count = 0
	
		for point in pointlist:
		
			if(cluster == point.cluster):
			
				xsum += point.x
				ysum += point.y
				count += 1
				
		newclusterlist.append(Cluster(xsum/count,ysum/count))
		
	return newclusterlist


def isclusterlistsame(clusterlista,clusterlistb):

	mydict = {}

	for cluster in clusterlista:
	
		mydict[(cluster.x,cluster.y)] = 1
		
	for cluster in clusterlistb:
	
		if((cluster.x,cluster.y) not in mydict):
			return False
			
		mydict[(cluster.x,cluster.y)] = 0
		
	for key in mydict:
	
		if(mydict[key] != 0):
			return False
			
	return True


def kmeansalgo(pointlist,k):

	clusterlist = []
	newclusterlist = []
	
	i = 0
	
	while(i < k):
	
		clusterid = random.randint(0,len(pointlist)-1)
	
		if(pointlist[clusterid] not in clusterlist):
		
			clusterlist.append(Cluster(pointlist[clusterid].x,pointlist[clusterid].y))
			i+=1
	
	clusterlist = [Cluster(pointlist[0].x,pointlist[0].y),Cluster(pointlist[7].x,pointlist[7].y)]
			
	newclusterlist = clusterlist
	
	print("\nInitial Clusters")
	for clu in clusterlist:
		print(clu)
	print("======================================================\n")
	
	iteration = 1
	
	while(True):
		
		clusterlist = newclusterlist
			
		findbestcluster(pointlist,clusterlist)
		
		print("\nPoints allocated to clusters")
		for p in pointlist:
			print(p)
		print("======================================================\n")
		
		newclusterlist = findnewclusters(pointlist,clusterlist)
	
		print("\nIteration : {0}\nClusters : ".format(iteration))
		for clu in newclusterlist:
			print(clu)
		print("======================================================\n")
		
		iteration += 1
		
		if(isclusterlistsame(newclusterlist,clusterlist)):
			break
		
	return clusterlist


#MAIN
filename = input("Enter file name : ")
pointlist = createpointlist(filename)

k = int(input("Enter value for K : "))

clusterlist = kmeansalgo(pointlist,k)


colorlist = ["red","green","blue","orange","yellow","brown",]
i = 0

print("\nFinal Clusters : \n")
for clu in clusterlist:
	
	plt.scatter(clu.x,clu.y,color = "black")
	print(clu)
	mycolor = colorlist[i]
	
	for point in pointlist:
	
		if(point.cluster == clu):
			plt.scatter(point.x,point.y,color = mycolor)
			
	i+=1
	
plt.show()

print("\nFinal Clusters : \n")
for clu in clusterlist:	
	print(clu)
