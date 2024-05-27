from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

#selenium version에 맞는 chrome을 자동으로 install
Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

url="http://naver.com"

#req 대신 사용한것
driver.get(url)
time.sleep(3)


html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
query = soup.select_one(".search_input_box")
print(query)