import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder 

datamatrix = pd.read_csv("data.csv")

#print(datamatrix.describe())


lb = LabelEncoder()

startdate = lb.fit_transform(datamatrix["Start date"])
enddate = lb.fit_transform(datamatrix["End date"])
startstation = lb.fit_transform(datamatrix["Start station"])
endstation = lb.fit_transform(datamatrix["End station"])
membertype = lb.fit_transform(datamatrix["Member type"])

datamatrix = datamatrix.drop(columns = "Bike number")
datamatrix = datamatrix.drop(columns = "Start date")
datamatrix = datamatrix.drop(columns = "End date")
datamatrix = datamatrix.drop(columns = "Start station")
datamatrix = datamatrix.drop(columns = "End station")
datamatrix = datamatrix.drop(columns = "Member type")

datamatrix["Start date"] = startdate
datamatrix["End date"] = enddate
datamatrix["Start station"] = startstation
datamatrix["End station"] = endstation
datamatrix["Member Type"] = membertype

print(datamatrix.describe())

X = datamatrix.iloc[:,:-1]
Y = datamatrix.iloc[:,-1]

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.3, random_state = 37)

clf = GaussianNB()

clf.fit(X_Train,Y_Train)

Y_Pred = clf.predict(X_Test)

print(classification_report(Y_Test,Y_Pred))
