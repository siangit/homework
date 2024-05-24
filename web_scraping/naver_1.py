import requests
from bs4 import BeautifulSoup

url = "https://naver.com"

req = requests.get(url)

# print(req) 소스코드 상태 확인

html = req.text
# print(html) 소스코드 보기

soup = BeautifulSoup(html, "html.parser")
# print(soup) 마녀수프 부수기 -> 컴터 이해가능
 
query = soup.select_one("#query")
# print(query)
bringclass = soup.select_one(".search_input_box")
# print(bringclass)