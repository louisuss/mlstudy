# 1. id, class 속성으로 tag 찾기
# 2. css 이용해서 tag 찾기
# 3. 속성 값으로 tag 찾기
# 4. 정규 표현식으로 tag 찾기
# 5. 개발자 도구를 이용하여 동적으로 로딩되는 데이터 추출하기

import requests
from bs4 import BeautifulSoup

# 1
url = 'https://news.v.daum.net/v/20200806174953226'
resp = requests.get(url)

# features 입력 안하는 경우 경고뜸
soup = BeautifulSoup(resp.text, features="lxml")
title = soup.find('h3', class_='tit_view')
# print(title.get_text())

soup.find_all('span', class_='txt_info')

# 한번 찾은 후 다시 이용해서 활용
info = soup.find('span', class_='info_view')
info.find('span', class_='txt_info')

container = soup.find('div', id='cMain')
# print(container.find_all('p'))
contents = ''
for p in container.find_all('p'):
    contents += p.get_text().strip()

print(contents)