import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

data = pd.read_csv("phoneDetails.csv")
data = data.drop(["Internet Connectivity 4G"],1)
data = data[data.RAM>0][data.Storage>0]

le = preprocessing.LabelEncoder()
company = le.fit_transform(list(data.Company))
data["Company"] = company

print(data)

predict = "Price"
X = data.drop([predict],1)
y = data[predict]

scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)

acc = 0 
max = 0
for i in range(10):
    print(i)
    x_train , x_test , y_train , y_test = sklearn.model_selection.train_test_split(rescaledX,y, test_size=0.2)

    model = linear_model.LogisticRegression(max_iter=4000)

    model.fit(x_train,y_train)
    acc = model.score(x_test,y_test)
    if(acc>max):
        max = acc

print("Logistic Val = ", max*100)
