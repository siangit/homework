# 전정국 스크래핑
import requests
from bs4 import BeautifulSoup

header_user = {
    "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="

keyword = input("검색어를 하나만 입력해주세요 ")

url = base_url+keyword
# print(url)
req = requests.get(url, headers = header_user)
html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".title_link")
name = soup.select(".name")

for i in zip(results,name):
    print(i[0].text)
    print(i[1].text)
    print(i[0]['href'])