import pandas as pd 
import numpy as np 
from joblib import load

df = pd.read_csv("cleanedDatasetFinal.csv")
# Using saved model to predict class od products at sale
X = df.drop(["Company","Original Price","Original Class","Sale Price","Sale Class"],1)
clf = load("svm_model.joblib")
y = clf.predict(X)
df["Sale Class"] = y


print(df)

# Dividing data into four parts according to Original Class
low = df[df["Original Class"]=="Low"]
budget = df[df["Original Class"]=="Budget"]
midRange = df[df["Original Class"]=="Mid-Range"]
premium = df[df["Original Class"]=="Premium"]

classes = ["Low","Budget","Mid-Range","Premium"]
counts = [0,0,0,0]
def calculateValue(data):

    """
    Input : A DataFrame data.

    Variables : S ==> Standard Deviation
                mean ==> Mean
                P1 ==> Original Price
                P2 ==> Sale Price
                C1 ==> Original Class
                C2 ==> Sale Class

    Output :    How good a deal is :
                (I) P2 - P1 < S => "Not a good deal"
                (II) 2S > P2 - P1 >= S => "Acceptable"
                (III) 3S > P2 - P1 >= 2S => "Good deal"
                (IV) Sale Class < Orignal Class ==> "Excellent"

    """
    S = data.loc[:,"Original Price"].std()
    mean = data.loc[:,"Original Price"].mean()
    P1 = list(data["Original Price"])
    P2 = list(data["Sale Price"])
    C1 = list(data["Original Class"])
    C2 = list(data["Sale Class"])

    print("SD : ",S,"Mean :",mean)

    deal = []
    c =0
    for i in range(len(P2)):
        if(classes.index(C2[i])<classes.index(C1[i])):
            deal.append("Excellent")
            counts[0] = counts[0] + 1
        elif(P2[i]-P1[i]<S/2):
            deal.append("Poor deal.")
            counts[1] = counts[1] + 1
        elif(S>P2[i]-P1[i] >= S/2):
            deal.append("Acceptable")
            counts[2] = counts[2] + 1
        elif(P2[i]-P1[i] > S):
            deal.append("Good deal")
            counts[3] = counts[3] + 1
        else:
            deal.append("Error")
            c = c + 1

    print("C = ",c)
    return deal

low["Deal"] = calculateValue(low)
budget["Deal"] = calculateValue(budget)
midRange["Deal"] = calculateValue(midRange)
premium["Deal"] = calculateValue(premium)

vertical_stack = pd.concat([low,budget,midRange,premium],axis=0)
vertical_stack.to_excel('output.xlsx', index=False)
print(vertical_stack)
print("Counts = ",counts)

