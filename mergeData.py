import pandas as pd 
import numpy as np

nonSale = pd.read_csv("phoneDetails2403NonSale.csv")
sale = pd.read_csv("phoneDetails1903Discounted.csv")

nonSale = nonSale.rename(columns={"Price":"Original Price"})
nonSale["Sale Price"] = sale.Price

nonSale = nonSale.drop(["Internet Connectivity 4G"],1)
nonSale = nonSale[nonSale.RAM>0][nonSale.Storage>0]

nonSale = nonSale.drop_duplicates(subset=["Company","RAM","Storage","Front Camera","Back Camera","Battery Capacity","Original Price"])


prices = list(nonSale["Original Price"])
classes = []
# Using custom values to create a "Class" column
for price in prices:
    if(price<5000):
        classes.append("Low")
    elif(price<15000):
        classes.append("Budget")
    elif(price<30000):
           classes.append("Mid-Range")
    else:
        classes.append("Premium")

nonSale["Original Class"] = classes


prices = list(nonSale["Sale Price"])
classes = []
# Using custom values to create a "Sale Class" column
for price in prices:
    if(price<5000):
        classes.append("Low")
    elif(price<15000):
        classes.append("Budget")
    elif(price<30000):
           classes.append("Mid-Range")
    else:
        classes.append("Premium")
nonSale["Sale Class"] = classes

print(nonSale)
print(sale)

nonSale.to_csv("cleanedDatasetFinal.csv",index=False)