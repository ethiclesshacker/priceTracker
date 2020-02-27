import requests
from bs4 import BeautifulSoup
import csv

import Flipkart


# Sample how to run Flipkart Module

# ftry = Flipkart.Product(LINK)

# ftry.getPrice()
# print(ftry.price)

# Sample over

# Can return upto 1000+ links of phones

# links = Flipkart.search("mobile phones")

data = []
data.append(["Company","RAM","Storage","Front Camera","Back Camera","Battery Capacity","Internet Connectivity 4G","Price"])
# for i in range(20):
#     ftry = Flipkart.Product(links[i])
#     ftry.getPrice()
#     print(ftry.price)

links = ["https://www.flipkart.com/redmi-7a-matte-blue-32-gb/p/itmfhz4cztznu8kk?pid=MOBFHZ4BZW2GM6UH&lid=LSTMOBFHZ4BZW2GM6UHFKVO3U&marketplace=FLIPKART&srno=s_1_10&otracker=search&otracker1=search&fm=SEARCH&iid=37bf99bc-d546-45c2-98b3-54d207efa31b.MOBFHZ4BZW2GM6UH.SEARCH&ppt=sp&ppn=sp&ssid=zt8irfm0hs0000001582536164104&qH=a81ad6e72f7a2fd1"]

for link in links:
    # linkData = []
    product = Flipkart.Product(link)

    product.getPrice()
    product.getFeatures()
    frontCam = ""
    backCam = ""
    ram = ""
    storage = ""
    company = ""
    battery = ""
    internet4G = ""
    price = ""

    l = len(product.featureNames)
    for i in range(l):
        featureName = product.featureNames[i].contents[0]
        feature = product.features[i].contents[0]
        if "RAM" in featureName:
            ram = feature
        if "Secondary Camera" == featureName:
            frontCam = feature
        if "Primary Camera" == featureName:
            backCam = feature
        if "Battery Capacity" == featureName:
            battery = feature
        if "Internal Storage" == featureName:
            storage = feature

    internet4G = 0
    price = product.price

    linkData = [company, ram, storage, frontCam, backCam, battery, internet4G, price]

    print(linkData)
    data.append(linkData)


with open("out.csv","w",newline="") as f :
    writer = csv.writer(f)
    writer.writerows(data)


