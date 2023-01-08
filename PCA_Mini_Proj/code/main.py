import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time
import warnings



warnings.filterwarnings("ignore")



threshold = 1.0

input_file_path = "/home/shriniwas/BE/LP3/MLProj/input/"
input_file_name = "test.csv"

analysis_file_path = "/home/shriniwas/BE/LP3/MLProj/output/"
analysis_file_name = "analysis.txt"

pca_img_file_path = "/home/shriniwas/BE/LP3/MLProj/output/"
pca_img_file_name = "explained_variance_ratio.png"

pca_data_file_path = "/home/shriniwas/BE/LP3/MLProj/output/"
pca_data_file_name = "e_" + input_file_name

accuracy_graph_path = "/home/shriniwas/BE/LP3/MLProj/output/"
accuracy_graph_name = "accuracy_comparison.png"

time_graph_path = "/home/shriniwas/BE/LP3/MLProj/output/"
time_graph_name = "time_comparison.png"



def analysis(df,input_file_name,analysis_file_path,analysis_file_name):

	try:
	
		analysis_fileobj = open(analysis_file_path + analysis_file_name,"w")

	except:
	
		print(":: Unable to open " + analysis_file_name + " :: ")
		exit(1)

	
	analysis_df = df.describe()

	analysis_fileobj.write("\n\n=========================================\n\n")
	analysis_fileobj.write("File name : " + input_file_name + "\n")
	analysis_fileobj.write("Data size : {0}".format(len(df)) + "\n")
	analysis_fileobj.write("Number of columns : {0}".format(len(analysis_df.columns)))
	analysis_fileobj.write("\n\n=========================================\n\n")

	dict_of_attr = {"mean" : "Mean","std" : "Standard Deviation","25%" : "1st Quartile","50%" : "Median","75%" : "3rd Quartile","min" : "Minimum value","max" : "Maximum value"}

	for col in analysis_df:

		analysis_fileobj.write("Column Name : " + col + "\n")
		
		for attr in dict_of_attr:
		
			analysis_fileobj.write(dict_of_attr[attr] + " : " + str(analysis_df[col][attr]) + "\n")
			
		analysis_fileobj.write("Mode : " + " ".join(list(map(str,[i for i in df[col].mode()]))) + "\n")
		
		analysis_fileobj.write("\n\n")


def GNB(data_df,target_df):

	start_time = time.time()

	X_train , X_test , Y_train , Y_test = train_test_split(data_df , target_df , test_size = 0.25, random_state = 7)

	model = GaussianNB()
	
	model.fit(X_train,Y_train)
	
	Y_pred = model.predict(X_test)
	
	accuracy = metrics.accuracy_score(Y_test,Y_pred)
	
	end_time = time.time()
	
	return accuracy,(end_time - start_time)	
	
	

def KNN(data_df,target_df):

	start_time = time.time()

	X_train , X_test , Y_train , Y_test = train_test_split(data_df , target_df , test_size = 0.25, random_state = 7)

	model = KNeighborsClassifier(3)
	
	model.fit(X_train,Y_train)
	
	Y_pred = model.predict(X_test)
	
	accuracy = metrics.accuracy_score(Y_test,Y_pred)
	
	end_time = time.time()
	
	return accuracy,(end_time - start_time)	


def SVM(data_df,target_df):

	start_time = time.time()

	X_train , X_test , Y_train , Y_test = train_test_split(data_df , target_df , test_size = 0.25, random_state = 7)

	model = SVC(kernel = "linear")
	
	model.fit(X_train,Y_train)
	
	Y_pred = model.predict(X_test)
	
	accuracy = metrics.accuracy_score(Y_test,Y_pred)
	
	end_time = time.time()
	
	return accuracy,(end_time - start_time)		


def pca(df,threshold,pca_img_file_path,pca_img_file_name):

	mat = df.values
	mat = scale(mat)
	
	pca_model = PCA()
	
	pca_model.fit(mat)
		
	list_of_variance_ratio = list(pca_model.explained_variance_ratio_)
	
	plt.plot(list_of_variance_ratio,color = "red")
	plt.xlabel("Components")
	plt.ylabel("Explained Variance Ratio")
	plt.savefig(pca_img_file_path + pca_img_file_name)
	plt.clf()
	
	cumulative_var = 0
	
	iterator = 0
	
	while( iterator < len(list_of_variance_ratio)):
	
		if(cumulative_var >= threshold):
		
			break
			
		cumulative_var += list_of_variance_ratio[iterator]
		
		iterator += 1
		
	mat = PCA(n_components = iterator).fit_transform(mat)
	
	return pd.DataFrame(mat)
	

#MAIN
		
df = pd.read_csv(input_file_path + input_file_name)
target_df = df["target"]
del df["target"]
data_df = df

analysis(data_df,input_file_name,analysis_file_path,analysis_file_name)

GNB_accuracy,GNB_time = GNB(data_df,target_df)

KNN_accuracy,KNN_time = KNN(data_df,target_df)

SVM_accuracy,SVM_time = SVM(data_df,target_df)

e_data_df = pca(data_df,threshold,pca_img_file_path,pca_img_file_name)

e_data_df.to_csv(pca_data_file_path + pca_data_file_name)

e_GNB_accuracy,e_GNB_time = GNB(e_data_df,target_df)

e_KNN_accuracy,e_KNN_time = KNN(e_data_df,target_df)

e_SVM_accuracy,e_SVM_time = SVM(e_data_df,target_df)

accuracy_list = [GNB_accuracy,e_GNB_accuracy,KNN_accuracy,e_KNN_accuracy,SVM_accuracy,e_SVM_accuracy]
time_list = [GNB_time,e_GNB_time,KNN_time,e_KNN_time,SVM_time,e_SVM_time]

plt.bar(["GNB","GNB PCA","KNN","KNN PCA","SVM","SVM PCA"],accuracy_list,0.3,color = ["red","blue","green","yellow","orange","brown"])
plt.xlabel("Algorithm")
plt.ylabel("Accuracy")
plt.savefig(accuracy_graph_path + accuracy_graph_name)
plt.clf()

plt.bar(["GNB","GNB PCA","KNN","KNN PCA","SVM","SVM PCA"],time_list,0.3,color = ["red","blue","green","yellow","orange","brown"])
plt.xlabel("Algorithm")
plt.ylabel("Time")
plt.savefig(time_graph_path + time_graph_name)
plt.clf()

"""
print(GNB_accuracy,GNB_time)
print(KNN_accuracy,KNN_time)
print(SVM_accuracy,SVM_time)
print(e_GNB_accuracy,e_GNB_time)
print(e_KNN_accuracy,e_KNN_time)
print(e_SVM_accuracy,e_SVM_time)
"""
