# 1. id, class 속성으로 tag 찾기
# 2. css 이용해서 tag 찾기
# 3. 속성 값으로 tag 찾기
# 4. 정규 표현식으로 tag 찾기
# 5. 개발자 도구를 이용하여 동적으로 로딩되는 데이터 추출하기
# find, find_all 함수에 모든 문자열로 오는 값들은 정규표현식으로 대체해서 값의 범위를 명시가능

import requests
from bs4 import BeautifulSoup
import re

# 4
# 댓글 개수 추출
# - 댓글의 경우, 최초 로딩 시에 전달되지 않음
# - 이 경우는 추가적으로 AJAX로 비동기적 호출을 하여 따로 data 전송을 함
# > 개발자 도구의 network 탭에서 확인(XHR: XmlHTTPRequest)
# > 비동기적 호출: 사이트의 전체가 아닌 일부분만 업데이트 가능하도록 함

url = 'https://news.v.daum.net/v/20200806174953226'
resp = requests.get(url)

# features 입력 안하는 경우 경고뜸
soup = BeautifulSoup(resp.text, features="lxml")

# 모든 h관련 태그 가져오기
# \d : 숫자
soup.find_all(re.compile('h\d'))


soup.find_all('img', attrs={'src': re.compile('.+\.jpg')})

# view로 끝나는 모든 태그
soup.find_all('h3', class_=re.compile('.+view$'))
soup.find_all('h3', class_=re.compile('.+newsview$'))
