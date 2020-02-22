import requests
from bs4 import BeautifulSoup

link = "https://www.flipkart.com/moto-e6s-polished-graphite-64-gb/p/itm13d6688c18a87?pid=MOBFGB3JBBGZGG58&lid=LSTMOBFGB3JBBGZGG58SIVC3B&fm=neo%2Fmerchandising&iid=M_e1f0c00b-f0e5-461e-b75a-93b6a2e419af_26.T1P4LNCYM0H6&ssid=8penlqxwlc0000001582285094620&otracker=hp_omu_Latest%2BLaunches_4_8.dealCard.OMU_Latest%2BLaunches_T1P4LNCYM0H6_5&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_Latest%2BLaunches_NA_dealCard_cc_4_NA_view-all_5&cid=T1P4LNCYM0H6"

def getPrice(link):
    r = requests.get(link)
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"})
    price = price.contents[0]
    price = price.replace("₹","")
    price = price.replace(",","")
    price = (float(price))

    return price

def getStorage(link):
    r = requests.get(link)
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    tableHeadings = soup.find_all("div", {"class": "_2lzn0o"})
    for tH in tableHeadings:
        print(tH.contents[0])

getStorage(link)




# price = "_1vC4OE _3qQ9m1"
# tableHeadings = "_2lzn0o"
# features(all types) = "_3YhLQA"
