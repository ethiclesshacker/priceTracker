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

    def getName(self):
        name = self.soup.find("span",{"class":"_35KyD6"})
        name = name.contents[0]
        self.companyName = name.split()[0]

    def getPrice(self):
        price = self.soup.find("div", {"class": "_1vC4OE _3qQ9m1"})
        price = price.contents[0]
        price = price.replace("₹","")
        price = price.replace(",","")
        self.price = (int(price))

    def getFeatures(self):
        self.featuresALL = self.soup.find_all("li", {"class": "_3YhLQA"})
        self.featureNames = self.soup.find_all("td", {"class": "_3-wDH3 col col-3-12"})

        self.feautures = dict()

        for i in range(len(self.featureNames)):
            self.feautures[self.featureNames[i].contents[0]] = self.featuresALL[i].contents[0]

    # div Class id's for Flipkart:
    # price = "_1vC4OE _3qQ9m1"
    # tableHeadings = "_2lzn0o"
    # features(all types) = "_3YhLQA"



def search(terms):
    terms = terms.replace(" ","+")
    fLink = []
    data = []
    for i in range(1,51):
        link = f"https://www.flipkart.com/search?q={terms}&otracker=start&page={i}"
        r = requests.get(link)
        print("Page no. : ",i)
        soup = BeautifulSoup(r.text,"html.parser")
        links = soup.find_all("a",{"class":"_31qSD5"})
        for link in links:
            l = link["href"]
            fLink.append(f"https://www.flipkart.com{l}")
        data.append(r)
        sleep(1)

    print(data)
    return fLink
