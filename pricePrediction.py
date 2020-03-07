import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn import preprocessing
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

max = 0 
acc = 0

for _ in range(1000):
    x_train , x_test , y_train , y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.2)

    
    model = linear_model.LinearRegression()

    model.fit(x_train,y_train)
    acc = model.score(x_test,y_test)

    if(acc>max):
        max = acc
        # with open("linearRegression2.pickle","wb") as f:
        #     pickle.dump(model,f)

print("Linear Max = ", max*100)
