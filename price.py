import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler


data = pd.read_csv("phoneDetails2403NonSale.csv")
# Removing internet connectivity and anomalous data
data = data.drop(["Internet Connectivity 4G"],1) 
data = data[data.RAM>0][data.Storage>0]
# Encoding company names to numbers
le = preprocessing.LabelEncoder()
company = le.fit_transform(list(data.Company))
data["Company"] = company

print(data)

predict = "Price"
X = data.drop([predict],1)
X = X.drop(["Company"],1) # To drop company from Dataset
y = data[predict]

print(X)
# Splitting train data/test data
x_train , x_test , y_train , y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.2)

# Scaling data using StandardScaler()
scaler = StandardScaler().fit(X)
rescaledXTrain = scaler.transform(x_train)
rescaledXTest = scaler.transform(x_test)
x_train = rescaledXTrain
x_test = rescaledXTest

# Training model and printing accuracy percentage
model = linear_model.LogisticRegression(max_iter=4000)
model.fit(x_train,y_train)
acc = model.score(x_test,y_test)
print("Accuracy = ", acc*100)

# Printing predictions
predictions = model.predict(x_test)
test = list(y_test)
print("Original\tPredcition")
for i in range(50):
    print(test[i],"\t\t",predictions[i])
