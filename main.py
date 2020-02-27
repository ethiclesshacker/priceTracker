import requests
from bs4 import BeautifulSoup
import csv
import re
import Flipkart

def numify(data):
    return re.findall(r'\d+',data)[0]

data = []
data.append(["Company","RAM","Storage","Front Camera","Back Camera","Battery Capacity","Internet Connectivity 4G","Price"])

links = ["https://www.flipkart.com/redmi-7a-matte-blue-32-gb/p/itmfhz4cztznu8kk?pid=MOBFHZ4BZW2GM6UH&lid=LSTMOBFHZ4BZW2GM6UHFKVO3U&marketplace=FLIPKART&srno=s_1_10&otracker=search&otracker1=search&fm=SEARCH&iid=37bf99bc-d546-45c2-98b3-54d207efa31b.MOBFHZ4BZW2GM6UH.SEARCH&ppt=sp&ppn=sp&ssid=zt8irfm0hs0000001582536164104&qH=a81ad6e72f7a2fd1"]

for link in links:
    product = Flipkart.Product(link)
    product.getPrice()
    product.getFeatures()

    frontCam = numify(product.feautures.get("Secondary Camera",0))
    backCam = numify(product.feautures.get("Primary Camera",0))
    ram = numify(product.feautures.get("RAM",0))
    storage = numify(product.feautures.get("Internal Storage",0))
    company = product.feautures.get("Model Name",0)
    company = company.split()[0]
    battery = numify(product.feautures.get("Battery Capacity",0))
    price = product.price
    internet4G =  0

    if "4G" in product.feautures.get("Supported Networks",0):
        internet4G =  1

    linkData = [company, ram, storage, frontCam, backCam, battery, internet4G, price]

    data.append(linkData)


with open("phoneDetails.csv","w",newline="") as f :
    writer = csv.writer(f)
    writer.writerows(data)