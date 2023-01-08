import matplotlib.pyplot as plt
import copy
import math

def createlistofattr(list_of_lines):

	templist = list_of_lines[0].split(",")

	l1 = [templist[0]]
	l2 = [templist[1]]
	l3 = [templist[2]]
	l4 = [templist[3]]
	l5 = [templist[4]]
	
	for line in list_of_lines[1:]:
	
		templist = line.split(",")
		l1.append(float(templist[0]))
		l2.append(float(templist[1]))
		l3.append(float(templist[2]))
		l4.append(float(templist[3]))
		l5.append((templist[4].split("\n")[0]))
			
	list_of_attributes = [l1,l2,l3,l4,l5]
	
	return(list_of_attributes)

def printdata(data):

	print("\n===========================================\n")
	print(data)
	print("\n===========================================\n")


		
def findmean(datalist,size):

	sumofdata = 0
	
	for data in datalist:
	
		sumofdata += data
	
	return(sumofdata/size)


	
def findmedian(datalist,size):

	templist = copy.deepcopy(datalist)
	
	templist.sort()
	
	med = 0
	
	if(size%2 == 1):
	
		med = templist[size // 2]

	else:
	
		med = templist[size // 2]
		med+= templist[(size // 2) - 1]
		med/=2
		
	return (med)

	
	
def findmode(datalist,size):

	tempdict = {}
	
	for data in datalist:
	
		if(data in tempdict):
		
			tempdict[data] += 1
			
		else:
		
			tempdict[data] = 1
			
			
	templist = list(tempdict.values())
	
	templist.sort(reverse = True)
	
	maxval = templist[0]
	
	ans = []
	
	for key in tempdict.keys():
	
		if(tempdict[key] == maxval):
		
			ans.append(key)
			
	return (ans)



def findvariance(datalist,size):

	mean = findmean(datalist,size)
	
	tempsum = 0
	
	for data in datalist:
	
		tempsum += ((data - mean) ** 2)
		
	return (tempsum)
	


def findstandarddeviation(datalist,size):

	tempsum = findvariance(datalist,size)
	
	return(math.sqrt(tempsum))
	
				

def findmin(datalist,size):

	temp = datalist[0]
	
	for data in datalist:
	
		if(data < temp):
		
			temp = data
			
	return (temp)
	
	
def findmax(datalist,size):

	temp = datalist[0]
	
	for data in datalist:
	
		if(data > temp):
		
			data = temp
			
	return (temp)


def findquartile(datalistone,size):

	quarlist = [0,0,0]
	
	quarlist[1] = findmedian(datalistone,size)
	
	datalist = copy.deepcopy(datalistone)
	datalist.sort()
	
	if(size % 2 == 0):
	
		med2 = size//2
		med1 = med2 - 1
		
		quarlist[0] = findmedian(datalist[0 : med1], len( datalist[0 : med1 ] ) )
		quarlist[2] = findmedian(datalist[med2+1 : ], len( datalist[med2+1 : ] ) )
	
	
	else:
		
		med = size//2
		
		quarlist[0] = findmedian(datalist[0:med], len(datalist[0:med]))
		quarlist[2] = findmedian(datalist[med+1 : ], len(datalist[med+1 : ]))
	
	return(quarlist)	
	
	
def findfrequency(datalist,size):

	tempdict = {}
	
	for data in datalist:
	
		if(data in tempdict):
		
			tempdict[data] += 1
			
		else:
		
			tempdict[data] = 1

	return (tempdict)


def analyze(list_of_attributes):


	for templist in list_of_attributes[:len(list_of_attributes) - 1]:
	
		report = ""
		
		report += "Parameter " + templist[0] + "\n"
		report += "Mean of the data : " + str(findmean(templist[1:],len(templist[1:]))) + "\n"
		report += "Median of data : " + str(findmedian(templist[1:],len(templist[1:]))) + "\n"
		report += "Mode of data : " + str(findmode(templist[1:],len(templist[1:]))) + "\n"
		report += "Variance of data : " + str(findvariance(templist[1:],len(templist[1:]))) + "\n" 		 
		report += "Standard Deviation of data : " + str(findstandarddeviation(templist[1:],len(templist[1:]))) + "\n"
		report += "Maximum in data : " + str(findmax(templist[1:],len(templist[1:]))) + "\n"
		report += "Min of data : " + str(findmin(templist[1:],len(templist[1:]))) + "\n"
		report += "Quartile of data : " + str(findquartile(templist[1:],len(templist[1:]))) + "\n"
		
		plt.hist(templist[1:])
		plt.xlabel(templist[0] + " in (cm)")
		plt.ylabel("frequency")
		plt.savefig(templist[0] + ".png")
		plt.show()
		plt.clf()
		plt.boxplot(templist[1:])	
		plt.savefig(templist[0] + "_boxplot.png")
		plt.show()
		plt.clf()
		
		printdata(report)
	

	tempdict = findfrequency(list_of_attributes[4][1:],len(list_of_attributes[4][1:]))
	report = str(tempdict)
	printdata(report)
	
				

fileobj = open("iris.csv","r")		
list_of_lines = fileobj.readlines()
list_of_attributes = createlistofattr(list_of_lines)
analyze(list_of_attributes)
