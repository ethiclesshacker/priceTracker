import pandas as pd
import numpy as np
import sklearn
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import pickle


data = pd.read_csv("phoneDetails2403NonSale.csv")

# Cleaning the dataset
data = data.drop(["Internet Connectivity 4G"],1)
data = data[data.RAM>0][data.Storage>0]
data = data.drop_duplicates()
data = data.drop(["Company"],1)

classes = []
prices = list(data["Price"])

# Using custom values to create a "Class" column
for price in prices:
    if(price<5000):
        classes.append("Low")
    elif(price<15000):
        classes.append("Budget")
    elif(price<30000):
           classes.append("Mid-Range")
    else:
        classes.append("Premium")

data["Class"] = classes

X = data.drop(["Price","Class"],1)
y = data["Class"]

classes = ["Low","Budget","Mid-Range","Premium"]


# max = 0 
# for _ in range(100):   
#     x_train, x_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state=1)
#     clf = svm.SVC(C=2,decision_function_shape="ovo",gamma=1,kernel="rbf",random_state=1)
#     clf.fit(x_train,y_train)
#     y_pred = clf.predict(x_test)
#     acc = metrics.accuracy_score(y_test,y_pred)
#     if(acc>max):
#         print(acc)
#         max = acc

# print(max*100)

clf = SVC(C=2,decision_function_shape="ovo",gamma=1,kernel="rbf")
scores = cross_val_score(clf,X,y,cv=20)
print(scores)
print("Accuracy = ",scores.mean())
print("+/-",scores.std() * 2)

# x_train, x_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)

# svm=SVC(random_state=1)
# svm.fit(x_train,y_train)
# print("train accuracy:",svm.score(x_train,y_train))
# print("test accuracy:",svm.score(x_test,y_test))


# svm_model=SVC(C=2,decision_function_shape="ovo",gamma=1,kernel="rbf",random_state=1)

# svm_model.fit(x_train,y_train)


# print("train_accuracy:",svm_model.score(x_train,y_train))
# print("test_accuracy: ", svm_model.score(x_test,y_test))