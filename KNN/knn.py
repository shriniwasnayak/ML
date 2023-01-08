class DataPoint:

	def __init__(self,attr_list,opclass):	
		self.attr_list = attr_list
		self.dis = 0
		self.opclass = opclass
		
	def __lt__(self,obj):
		return self.dis < obj.dis
		
	def __gt__(self,obj):
		return self.dis > obj.dis
		
	def __str__(self):
		return "\nAttr list : " + str(self.attr_list) + "\nDis : " + str(self.dis) + "\nClass Lable : " + str(self.opclass)

		
def cal_euc_dis(attr_list_1,attr_list_2):

	dis = 0
	size = len(attr_list_1)
	
	for i in range(size):
		dis += ((attr_list_1[i] - attr_list_2[i])**2)
		
	return dis
		
def find_dis(list_of_points,test_point):

	for point in list_of_points:
		point.dis = cal_euc_dis(test_point, point.attr_list)
		

def find_class(list_of_points,test_point,k):

	mydict = {}
	
	for point in list_of_points[:k]:
	
		if(point.opclass in mydict):
			mydict[point.opclass] += 1
		else:
			mydict[point.opclass] = 1
			
	modclass = -1
	maxval = 0
	
	print("\n")
	print(mydict)
	
	for key in mydict:
	
		if(mydict[key]>maxval):
			maxval = mydict[key]
			modclass = key
	
	return modclass

if(__name__ == "__main__"):
	
	k = int(input("Enter value of K : "))
	n = int(input("Enter number of points : "))
	print("Enter datapoints : ")
	
	list_of_points = []
	
	for i in range(n):
		templist = list(map(float,input().split()))
		size = len(templist)
		list_of_points.append((DataPoint(templist[:size-1],int(templist[size-1]))))
		
	n = int(input("Enter number of test points : "))
	print("Enter test points : ")
		
	for i in range(n):
		test_point = list(map(float,input().split()))
		find_dis(list_of_points,test_point)
		list_of_points.sort()
		pred_class = find_class(list_of_points,test_point,k)
	
		for j in list_of_points:
			print(j)  
		
		print("\n\nClass predicted : " + str(int(pred_class)))	
