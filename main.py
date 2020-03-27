import csv
import re
import Flipkart
import time


def numify(data):
    try:
        return re.findall(r'\d+', data)[0]
    except:
        return 0

def numifyStorage(data):
    data = data.upper()
    try:
        val = float(re.findall(r'\d+', data)[0])
        if("GB" in data):
            return val
        if("MB" in data):
            return (float(val/1024))
    except:
        return 0
    return 0

data = []
data.append(["Company", "RAM", "Storage", "Front Camera", "Back Camera",
             "Battery Capacity", "Internet Connectivity 4G", "Price"])

links = Flipkart.search("mobile phones")
print("Link Collection Done...")

with open("links.txt","w") as f:
    f.write("\n".join(links))

count = 1
c = 1
for link in links:
    print("Link no. : ",c)
    c = c + 1
    try:
        product = Flipkart.Product(link)
        product.getPrice()
        product.getFeatures()
        product.getName()

        company = product.companyName
        frontCam = numify(product.feautures.get("Secondary Camera", "0"))
        backCam = numify(product.feautures.get("Primary Camera", "0"))
        ram = numifyStorage(product.feautures.get("RAM", "0"))
        storage = numifyStorage(product.feautures.get("Internal Storage", "0"))
        battery = numify(product.feautures.get("Battery Capacity", "0"))
        price = product.price
        internet4G = 0

        if "4G" in product.feautures.get("Supported Networks", 0):
            internet4G = 1

        linkData = [company, ram, storage, frontCam,
                    backCam, battery, internet4G, price]
        data.append(linkData)

    except:
        if count <= 5:
            print("Sleeping....",count)
            time.sleep(180)
            count = count + 1
        else:
            continue


with open("phoneDetails2403.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
