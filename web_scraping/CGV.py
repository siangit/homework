import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

base_url = ' http://www.cgv.co.kr/movies/?lt=1&ft=0'

req = requests.get(base_url, headers=header_user)
html = req.text
soup = BeautifulSoup(html,"html.parser")


rank = soup.select(".rank")
title = soup.select(".title")
percent = soup.select(".percent")
date = soup.select(".txt-info strong")


for i in zip(rank,title,percent,date):
    print(i[0].text)
    print(i[1].text)
    print(i[2].text)
    print(i[3].text)
    print(sep="/")