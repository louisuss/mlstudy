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

url = 'https://news.v.daum.net/v/20200808073012901'

driver.get(url)

# 해당 페이지 소스 가져오기
src = driver.page_source
soup = BeautifulSoup(src, features='lxml')

driver.close()

comment = soup.select_one('span.alex-count-area')
# get_text() : 내용 가져오기
print(comment.get_text())
