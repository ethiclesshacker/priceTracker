import requests
from bs4 import BeautifulSoup
import csv

import Flipkart


# Sample how to run Flipkart Module

# ftry = Flipkart.Product("https://www.flipkart.com/realme-x-space-blue-128-gb/p/itmfgybqzcgbxs26?pid=MOBFGYBQKYA5Y7HG&lid=LSTMOBFGYBQKYA5Y7HG7OS3JD&fm=neo%2Fmerchandising&iid=M_68031506-76e1-4de2-9dc5-8d7e4e16da78_18.GEIZE4KI3G8U&ppt=hp&ppn=hp&ssid=jvhwywiapc0000001582468462771&otracker=hp_omu_Dual%2BCamera%2BPhone_3_11.dealCard.OMU_Dual%2BCamera%2BPhone_GEIZE4KI3G8U_7&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_Dual%2BCamera%2BPhone_NA_dealCard_cc_3_NA_view-all_7&cid=GEIZE4KI3G8U")

# ftry.getPrice()
# print(ftry.price)

# Sample over

# Can return upto 1000+ links of phones
links = Flipkart.search("mobile phones") 

for i in range(20):
    ftry = Flipkart.Product(links[i])
    ftry.getPrice()
    print(ftry.price)