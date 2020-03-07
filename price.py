import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing


data = pd.read_csv("phoneDetails.csv")
data = data.drop(["Internet Connectivity 4G"],1)
data = data[data.RAM>0][data.Storage>0]
print(data)
le = preprocessing.LabelEncoder()
company = le.fit_transform(list(data.Company))
data["Company"] = company

print(data)

predict = "Price"
X = data.drop([predict],1)
y = data[predict]

X_train , X_test , y_train , y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.2)