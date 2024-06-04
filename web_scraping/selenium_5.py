from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

# 화면 자동 설정
options.add_argument("--start-maximaized")

url = "http://google.com"
driver.get(url)