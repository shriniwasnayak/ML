def createdatamatrix(filename):

	fileobj = open(filename,"r")
	
	list_of_lines = fileobj.readlines()
	
	datamatrix = []
	
	templist = list_of_lines[0].split(",")
	templist[len(templist)-1] = templist[len(templist)-1].split("\n")[0]
	
	datamatrix.append(templist)
	
	for line in list_of_lines[1:]:
	
		templist = line.split(",")
		
		datamatrix.append(list(map(float,templist)))
		
	return(datamatrix)
	

def split(datamatrix,percent):

	percent = percent//10
	
	train = []
	test = []
	
	train.append(datamatrix[0])
	test.append(datamatrix[0])
	
	for i in range(1,len(datamatrix)):
	
		if(i%percent == 0):
		
			test.append(datamatrix[i])
			
		else:
		
			train.append(datamatrix[i])
			
	return(train,test)


def classify(train,test):

	alphalist = [20,20,20,20,20,20,0.2,20,20] 

	threshhold = 0.005

	ylist = []
	
	for i in range(1,len(train)):
	
		if(train[i][8] == 1):
			ylist.append(i)	
	
	py = len(ylist)/len(train[1:])
	
	tp = 0
	tn = 0
	fp = 0
	fn = 0
	
	for i in range(1,len(test)):
	
		pofygx = py
	
		for j in range(8):
		
			pofxgy = 0
		
			for k in ylist:
			
				if( (test[i][j] == train[k][j]) or ((test[i][j] < (train[k][j]+alphalist[j])) and (test[i][j] > (train[k][j]-alphalist[j]))) ):
			
					pofxgy += 1
						
			if(pofxgy == 0):
				pofxgy = 1
				
			pofygx *= (pofxgy/len(ylist))
		
		if(pofygx >= threshhold):
			pofygx = 1
			
		else:
			pofygx = 0
			
		
		if(pofygx == test[i][8]):
			if(pofygx == 1):
				tp += 1
			else:
				tn += 1
		else:
			
			if(pofygx == 1):
				fp += 1
			else:
				fn += 1
				
	
	print("TP" + str(tp))
	print("TN" + str(tn))
	print("FP" + str(fp))
	print("FN" + str(fn))
	
	accuracy = (tp+tn)/len(test[1:])
	
	print("Accuracy = {0}\n".format(accuracy))

	
datamatrix = createdatamatrix("diabetes.csv")
train,test = split(datamatrix,70)
classify(train,test)
