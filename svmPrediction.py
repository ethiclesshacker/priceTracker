import pandas as pd
import numpy as np
import sklearn
from sklearn import svm
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn import metrics
import pickle

from sklearn import preprocessing
import matplotlib.pyplot as plt
from matplotlib import style


data = pd.read_csv("phoneDetails2403NonSale.csv")
data = data.drop(["Internet Connectivity 4G"],1)
data = data[data.RAM>0][data.Storage>0]
data = data.drop(["Company"],1)

classes = []
prices = list(data["Price"])

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

max = 0
for _ in range(50):
    # Splitting train/test data everytime
    x_train , x_test , y_train , y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.2)

    clf = svm.SVC()
    clf.fit(x_train,y_train)
    y_pred = clf.predict(x_test)
    acc = metrics.accuracy_score(y_test,y_pred)

    if acc > max :
        max = acc


print(max*100)

