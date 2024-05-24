import requests
from bs4 import BeautifulSoup

header_user = {
    "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

base_url = "https://www.melon.com/chart/index.htm"
req = requests.get(base_url, headers= header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

top_total = soup.select(".lst50, .lst100")

for rank, i in enumerate(top_total,1):
    rank = i.select_one(".rank")
    title = i.select_one(".ellipsis.rank01 a")
    singer = i.select_one(".checkEllipis")
    album = i.select_one(".ellipsis.rank03 a")
    print(rank.text)
    print(title.text)
    print(singer.text)
    print(album.text)
    print(sep="/")