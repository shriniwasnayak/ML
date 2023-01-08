import csv

def createlist(filename):

	csvobj = csv.reader(open(filename,"r"))

	xlist = []
	ylist = []
	
	for row in csvobj:
		xlist.append(float(row[0]))
		ylist.append(float(row[1]))

	return(xlist,ylist)

def solveeq(a1,b1,c1,a2,b2,c2):

	D = (a1*b2) - (a2*b1)
	x = (b2*c1) - (b1*c2)
	y = (a2*c1) - (a1*c2)

	return(x/D,-y/D)

filename = input("\nEnter File name : ")
xlist,ylist = createlist(filename)

n = len(xlist)
sumx = sum(xlist)
sumy = sum(ylist)
sumxsq = sum([xlist[i]**2 for i in range(n)])
sumxy = sum([xlist[i]*ylist[i] for i in range(n)])

a,b = solveeq(sumx,n,sumy,sumxsq,sumx,sumxy)

print("Line of best fit : y = {0}x + ({1})".format(a,b))
