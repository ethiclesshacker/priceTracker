from selenium  import webdriver
import requests
from time import sleep

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")


def searchSel():
    terms = "mobile+phones"
    fLink = []
    for i in range(1,50):
            link = f"https://www.flipkart.com/search?q={terms}&otracker=start&page={i}"
            driver.get(link)
            sleep(1)

def searchReq():
    terms = "mobile+phones"
    fLink = []
    for i in range(1,50):
            link = f"https://www.flipkart.com/search?q={terms}&otracker=start&page={i}"
            r = requests.get(link)
            print(i)
            sleep(1)

searchReq()

# links = ["Aditya","Vikram","Singhania"]

# with open("linkkjbjkbkjs.txt","w") as f:
#     f.write("\n".join(links))