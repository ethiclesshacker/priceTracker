import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt


data = pd.read_csv("phoneDetails.csv")
data = data[data.RAM>0][data.Storage>0]
data = data[["RAM", "Storage", "Front Camera", "Back Camera","Battery Capacity", "Price"]]

print(data)

predict = "Price"
x = data.drop([predict],1)
y = data[predict]

max = 0 
acc = 0
for _ in range(10):
    x_train , x_test , y_train , y_test = sklearn.model_selection.train_test_split(x,y, test_size=0.2)
    # x_train /= x_train.max()
    linear = linear_model.LogisticRegression(max_iter=400)

    linear.fit(x_train,y_train)
    # pred = linear.predict(x_test)
    acc = linear.score(x_test,y_test)
    
    # print(acc*100)

    if(acc>max):
        max = acc

print("Logistic Max = ", max*100)
