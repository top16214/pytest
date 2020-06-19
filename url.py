# -*- coding:utf-8 -*-

#import io       # io 库是处理stream数据的良器

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = r"https://news.163.com/20/0606/20/FEFF36MN0001899O.html"
response = urlopen(url)
htmltext = response.read()
bs = BeautifulSoup(htmltext, "lxml")
#content = [element.get("href") for element in bs.find_all("a")]
#for k, v in enumerate(content, start=1):
#    print(k, v)

content = bs.find_all('li', class_="related_article_item")
for item in content:
    print(type(item))
    print(item.a.string)
    print(item.a.get("href"))
