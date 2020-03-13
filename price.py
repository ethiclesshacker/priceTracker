import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
from sklearn.preprocessing import scale


data = pd.read_csv("phoneDetails.csv")
data = data.drop(["Internet Connectivity 4G"],1)
data = data[data.RAM>0][data.Storage>0]

le = preprocessing.LabelEncoder()
company = le.fit_transform(list(data.Company))
data["Company"] = company

print(data)

data_standardized=scale(data)
data_standardized.mean(axis=0)

print(data_standardized)

predict = "Price"
# X = data_standardized.drop([predict],1)
X = data_standardized
y = data[predict]


x_train , x_test , y_train , y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.2)

model = linear_model.LogisticRegression(max_iter=4000)

model.fit(x_train,y_train)
acc = model.score(x_test,y_test)

print("Logistic Val = ", acc*100)
