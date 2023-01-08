import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

def classify(filename,clf,classifier_type):

	datamatrix = pd.read_csv(filename)
	
	X = datamatrix.iloc[:,:-1]
	Y = datamatrix.iloc[:,-1]
	
	X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.3, random_state = 37)
	
	clf.fit(X_Train,Y_Train)
	
	Y_Pred = clf.predict(X_Test)
	
	print("Classifier : " + classifier_type + "\n\n")
	print("================================================\n")
	print(classification_report(Y_Test,Y_Pred))
	print("\n================================================\n")
	
	cm = confusion_matrix(Y_Test,Y_Pred)
	fig = sns.heatmap(cm,annot = True)
	plt.savefig(classifier_type + "_heatmap.png")
	plt.clf()

classify("diabetes.csv",GaussianNB(),"Naive Bayes")
classify("diabetes.csv",SVC(kernel = "linear"),"SVM")
classify("diabetes.csv",DecisionTreeClassifier(random_state = 37),"Decision Tree")
classify("diabetes.csv",KNeighborsClassifier(),"KNN")
