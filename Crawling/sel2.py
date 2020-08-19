# requests, BeautifulSoup 조합으로 크롤링 실패 시 적용
# 웹페이지 테스트 자동화용 모듈
# 개발/테스트용 드라이버(웹브라우저)를 사용하여 실제 사용자가 사용하는 것 처럼 동작

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time

chrome_driver = '/Users/louis/Selenium/chromedriver'

driver = webdriver.Chrome(chrome_driver)

driver.get('https://www.python.org')

search = driver.find_element_by_id('id-search-field')
search.clear()
time.sleep(2)
search.send_keys('lambda')

time.sleep(2)

search.send_keys(Keys.RETURN)

time.sleep(2)

driver.close()
