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

    # div Class id's for Flipkart:
    # price = "_1vC4OE _3qQ9m1"
    # tableHeadings = "_2lzn0o"
    # features(all types) = "_3YhLQA"



def search(terms):
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

