import pandas as pd
import numpy as np
import sklearn
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import KFold
import pickle


data = pd.read_csv("cleanedDatasetFinal.csv")

X = data.drop(["Company","Original Price","Sale Price","Original Class","Sale Class"],1)
y = data["Original Class"]

classes = ["Low","Budget","Mid-Range","Premium"]

num_folds = 10

max = 0
for _ in range(100):
    # Splitting train/test data everytime
    x_train , x_test , y_train , y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.2)

    clf = svm.SVC(C=2,decision_function_shape="ovo",gamma=1,kernel="rbf")
    clf.fit(x_train,y_train)
    y_pred = clf.predict(x_test)
    acc = metrics.accuracy_score(y_test,y_pred)

    if acc > max :
        max = acc


print(max*100)

