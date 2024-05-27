from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#selenium version에 맞는 chrome을 자동으로 install
Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

url="http://naver.com"

driver.get(url)
time.sleep(3)

title=driver.title
print(title)

html = driver.page_source
print(html)