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
companyNames = data.Company
le = preprocessing.LabelEncoder()
company = le.fit_transform(list(data.Company))
data["Company"] = company

print(data)

predict = "Price"
X = data.drop([predict],1)
y = data[predict]

# scaler = StandardScaler().fit(X)
# rescaledX = scaler.transform(X)

acc = 0 
max = 0

x_train , x_test , y_train , y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.2)
xtest = list(x_test["Company"]) # Work More
ytest = list(y_test)
final = x_test
final["Price"] = y_test
final["Company Name"] = companyNames
print(final)

scaler = StandardScaler().fit(X)
rescaledXTrain = scaler.transform(x_train)
rescaledXTest = scaler.transform(x_test)

# x_train = rescaledXTrain
# x_test = rescaledXTest

# model = linear_model.LogisticRegression(max_iter=4000)
# model.fit(x_train,y_train)
# acc = model.score(x_test,y_test)
# print("Logistic Accuracy = ", acc*100)

# predictions = model.predict(x_test)

# print("Original\tPredcition")
# # for i in range(50):
# #     print(test[i],"\t\t",predictions[i])
