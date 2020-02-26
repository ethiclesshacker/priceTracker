import requests
from bs4 import BeautifulSoup
from time import sleep

class Product:

    def __init__(self,link):
        r = requests.get(link)
        html = r.text
        self.soup = BeautifulSoup(html,"html.parser")

    def printPage(self):
        print(self.soup.prettify())

    def getPrice(self):
        price = self.soup.find("div", {"class": "_1vC4OE _3qQ9m1"})
        price = price.contents[0]
        price = price.replace("₹","")
        price = price.replace(",","")
        self.price = (float(price))

    def getFeatures(self):
        self.features = self.soup.find_all("li", {"class": "_3YhLQA"})
        self.featureNames = self.soup.find_all("td", {"class": "_3-wDH3 col col-3-12"})




"""
fl = Flipkart("https://www.flipkart.com/realme-x-space-blue-128-gb/p/itmfgybqzcgbxs26?pid=MOBFGYBQKYA5Y7HG&lid=LSTMOBFGYBQKYA5Y7HG7OS3JD&fm=neo%2Fmerchandising&iid=M_68031506-76e1-4de2-9dc5-8d7e4e16da78_18.GEIZE4KI3G8U&ppt=hp&ppn=hp&ssid=jvhwywiapc0000001582468462771&otracker=hp_omu_Dual%2BCamera%2BPhone_3_11.dealCard.OMU_Dual%2BCamera%2BPhone_GEIZE4KI3G8U_7&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_Dual%2BCamera%2BPhone_NA_dealCard_cc_3_NA_view-all_7&cid=GEIZE4KI3G8U")
fl.getPrice()
fl.getFeatures()

# Can print everything now




# div Class id's for Flipkart:
# price = "_1vC4OE _3qQ9m1"
# tableHeadings = "_2lzn0o"
# features(all types) = "_3YhLQA"

"""


def search(terms):
    # terms = "mobile phones"
    terms = terms.replace(" ","+")
    fLink = []

    for i in range(1,51):
        link = f"https://www.flipkart.com/search?q={terms}&otracker=start&page={i}"
        r = requests.get(link)
        soup = BeautifulSoup(r.text,"html.parser")
        links = soup.find_all("a",{"class":"_31qSD5"})
        for link in links:
            l = link["href"]
            fLink.append(f"https://www.flipkart.com{l}")

        sleep(1)
    return fLink


# links = search("mobile phones")

# for link in links:
#     print(link)

