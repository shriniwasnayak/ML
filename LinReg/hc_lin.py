import csv

csvreader = csv.reader(open("hc_ip.csv","r"))

x = []
y = []

for i in csvreader:

	if(float(i[0]) < 4.00):
	
		x.append(float(i[0]))
		y.append(float(i[1])) 
		
def solveeq(a1,b1,c1,a2,b2,c2):

	D = (a1*b2) - (a2*b1)
	x = (b2*c1) - (b1*c2)
	y = (a2*c1) - (a1*c2)

	return(x/D,-y/D)

xlist = x
ylist = y

n = len(xlist)
sumx = sum(xlist)
sumy = sum(ylist)
sumxsq = sum([xlist[i]**2 for i in range(n)])
sumxy = sum([xlist[i]*ylist[i] for i in range(n)])

a,b = solveeq(sumx,n,sumy,sumxsq,sumx,sumxy)

print("Line of best fit : y = {0}x + ({1})".format(a,b))		
