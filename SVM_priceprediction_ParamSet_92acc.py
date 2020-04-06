import pandas as pd
import numpy as np
import sklearn
from sklearn import svm
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn import metrics
import pickle


data = pd.read_csv("phoneDetails2403NonSale.csv")

# Cleaning the dataset
data = data.drop(["Internet Connectivity 4G"],1)
data = data[data.RAM>0][data.Storage>0]
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
print(data)

X = data.drop(["Price","Class"],1)
x_data=X
y = data["Class"]

classes = ["Low","Budget","Mid-Range","Premium"]


import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
from yellowbrick.target import ClassBalance
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import svm, datasets


x_train, x_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state=1)


svm=SVC(random_state=1)
svm.fit(x_train,y_train)
print("train accuracy:",svm.score(x_train,y_train))
print("test accuracy:",svm.score(x_test,y_test))


svm_model=SVC(C=2,decision_function_shape="ovo",gamma=1,kernel="rbf",random_state=1)

svm_model.fit(x_train,y_train)

print("after setting parameter")

print("train_accuracy:",svm_model.score(x_train,y_train))
print("test_accuracy: ", svm_model.score(x_test,y_test))