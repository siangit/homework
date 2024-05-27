from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import requests

#selenium version에 맞는 chrome을 자동으로 install
# Service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=Service)

url = "https://section.cafe.naver.com/ca-fe/home"

# driver.get(url)
# time.sleep(5)
# html=driver.page_source

req=requests.get(url)
html = req.text
print(html)