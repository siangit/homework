# 전정국 스크래핑
import requests
from bs4 import BeautifulSoup

header_user = {
    "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

base_url = "https://search.naver.com/search.naver?sm=tab_hty.top&ssc=tab.blog.all&query="

keyword = "유산균"

url = base_url+keyword
# print(url)
req = requests.get(url, headers = header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".title_link")
advertisement = soup.select(".spblog.ico_ad")
viewall = soup.select(".view_wrap")

for i in zip(viewall,results):
    if "spblog ico_ad" in i[0]:
        print(i[1].text)