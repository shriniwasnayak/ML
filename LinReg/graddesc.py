import csv

def createlist(filename):

	csvobj = csv.reader(open(filename,"r"))

	xlist = []
	ylist = []
	
	for row in csvobj:
		xlist.append(float(row[0]))
		ylist.append(float(row[1]))

	return(xlist,ylist)

def Jd0(t0,t1,xlist,ylist):

	val = 0	

	for i in range(len(xlist)):
	
		val += (t0 + t1*xlist[i] - ylist[i])

	return val

def Jd1(t0,t1,xlist,ylist):

	val = 0	

	for i in range(len(xlist)):
	
		val += ((t0 + t1*xlist[i] - ylist[i])*xlist[i])

	return val

def costfunc(t0,t1,xlist,ylist):

	val = 0	

	for i in range(len(xlist)):
	
		val += ((t0 + t1*xlist[i] - ylist[i])**2)

	return (val/(2*len(xlist)))

def findeq(xlist,ylist,alpha,ep):

	t0 = 0
	t1 = 0.5

	jnew = costfunc(t0,t1,xlist,ylist)
	jold = jnew+2*ep	

	while(jold-jnew > ep):

		temp0 = t0 - alpha*Jd0(t0,t1,xlist,ylist)
		temp1 = t1 - alpha*Jd1(t0,t1,xlist,ylist)

		t0 = temp0
		t1 = temp1

		jold = jnew
		jnew = costfunc(t0,t1,xlist,ylist)

	return(t1,t0)

filename = input("\nEnter File name : ")

alpha = 0.03
ep = 0.00001

xlist,ylist = createlist(filename)
a,b = findeq(xlist,ylist,alpha,ep)

print("Line of best fit : y = {0}x + ({1})".format(a,b))

