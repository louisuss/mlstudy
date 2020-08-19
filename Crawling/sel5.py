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
import requests

# news에 id 를 인자로 줌


def get_daum_news_title(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, features='lxml')

    title_tag = soup.select_one('h3.tit_view')

    if title_tag:
        return title_tag.get_text()
    return ""

# print(get_daum_news_title(20200808073012901))
# print(get_daum_news_title(20200808020301917))


def get_daum_news_content(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, features='lxml')

    content = ''

    for p in soup.select('div#harmonyContainer p'):
        content += p.get_text()

    return content


# print(get_daum_news_content(20200808073012901))
# print(get_daum_news_content(20200808020301917))


# chrome_driver = '/Users/louis/Selenium/chromedriver'
# driver = webdriver.Chrome(chrome_driver)

# offset 만큼 댓글 존재시 출력, 없으면 [] 출력
# 401 에러뜨는 경우
url = 'https://comment.daum.net/apis/v1/posts/@20200808020301917/comments?parentId=0&offset=3&limit=10&sort=LATEST&isInitial=false&hasNext=true'

# headers = {
#     Host: comment.daum.net
#     Connection: keep-alive
#     Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb3J1bV9rZXkiOiJuZXdzIiwiZ3JhbnRfdHlwZSI6ImFsZXhfY3JlZGVudGlhbHMiLCJzY29wZSI6W10sImV4cCI6MTU5Njk0MTE2OSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9DTElFTlQiXSwianRpIjoiOGU0ZTVjY2ItMWQ4My00MWMwLWE1YzMtYzk5ODI3OGQxY2VmIiwiZm9ydW1faWQiOi05OSwiY2xpZW50X2lkIjoiMjZCWEF2S255NVdGNVowOWxyNWs3N1k4In0.bRdSnn0_qyxt207BxPnmjveI-N2NSOd5rSlji0_ixgQ
#     User-Agent: Mozilla/5.0 (Macintosh
#                              Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
#     Accept: */*
#     Origin: https: // news.v.daum.net
#     Sec-Fetch-Site: same-site
#     Sec-Fetch-Mode: cors
#     Sec-Fetch-Dest: empty
#     Referer: https: // news.v.daum.net/v/20200808020301917
#     Accept-Encoding: gzip, deflate, br
#     Accept-Language: ko-KR, ko
#     q = 0.9, en-US
#     q = 0.8, en
#     q = 0.7
#     Cookie: _TI_NID = iok9mjEFfnWoNqMjDA5hhaBEQhDFWn9IakmV0077HQq5cuuPjcs/9kABU5+vukns1TkKb8nQ/Gf21w/CfgcQZQ ==
#     TIARA = S.oBPgrpYzBj6bMn6yZ1SKsvxB -
#     pN9wlmCXqLHCD6ePnvJbrwv3qjIiPrtEVkmJD.nrATMdCQA4r2iOTx7WQ8w00
# }
resp = requests.get(url)
# resp = requests.get(url, headers=headers)
print(resp.json())


def get_daum_news_comments(news_id):
    url_template = 'https://comment.daum.net/apis/v1/posts/@{}/comments?parentId=0&offset={}&limit=10&sort=LATEST&isInitial=false&hasNext=true'
    offset = 0
    comments = []
    while True:
        url = url_template.format(news_id, offset)
        resp = requests.get(url)
        data = resp.json()
        if not data:
            break

        # data 역시 타입이 리스트이기 때문에 extend로 추가
        comments.extend(data)
        # limit이 10이므로 10으로 설정
        offset += 10
    return comments


147094180
147093498
# print(len(get_daum_news_comments('147091429')))
# driver.get(url)

# driver.close()
