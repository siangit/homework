import requests
from bs4 import BeautifulSoup

header_user = {
    "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

url = "https://naver.com"

req = requests.get(url, headers = header_user)
print(req.raise_for_status)
# print(req.request) 방식 확인
# print(req) 소스코드 상태 확인

html = req.text
# print(html) 소스코드 보기

soup = BeautifulSoup(html, "html.parser")
# print(soup) 마녀수프 부수기 -> 컴터 이해가능