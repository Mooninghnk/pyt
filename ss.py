# a webscraper for zillo to see all the propery data
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}


def getPage(num):
    r = requests.get(f"https://www.realtor.com/international/cr/p{num}/?maxprice=300000", headers=headers)
    s = BeautifulSoup(r.content, "html.parser")
    x = s.find("div", class_="listings-list")
    list = x.find("ul", class_="tier-one-listing-table")
    li = list.find_all("li", class_="listing")
    for cc in li:
        image = cc.find("a", class_="img-box")
        img = image.attrs["href"]
        price = cc.find("p").text
        type = cc.find("div", class_="propertytype").text
        
        try:
            sqr = cc.find("span", class_="value").text
        except AttributeError:
            try:
                sqr = cc.find("b", class_="num").text
            except AttributeError:
                sqr = "0"
        
        print(f"https://www.realtor.com{img.strip()}", f"{price.strip()} {type.strip()} {sqr.strip()}")


for x in range(1, 4):
    getPage(x)
