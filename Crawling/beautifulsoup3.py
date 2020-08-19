# 1. id, class 속성으로 tag 찾기
# 2. css 이용해서 tag 찾기
# 3. 속성 값으로 tag 찾기
# 4. 정규 표현식으로 tag 찾기
# 5. 개발자 도구를 이용하여 동적으로 로딩되는 데이터 추출하기

import requests
from bs4 import BeautifulSoup

# 2
# - select, select_one 함수 사용
# - css selector 사용
# > 태그명 찾기 tag
# > 자손 태그 찾기 - 자손 관계 (tag tag)
# > 자식 태그 찾기 - 다이렉트 자식 관계 (tag > tag)
# > 아이디 찾기 #id
# > 클래스 찾기 .class
# > 속성값 찾기 [name='test']
# >> 속성값 prefix 찾기 [name ^= 'test']
# >> 속성값 suffix 찾기 [name $= 'test']
# >> 속성값 substring 찾기 [name *= 'test']
# > n번째 자식 tag 찾기 :nth-child(n)

url = 'https://news.v.daum.net/v/20200806174953226'
resp = requests.get(url)

# features 입력 안하는 경우 경고뜸
soup = BeautifulSoup(resp.text, features="lxml")

# print(soup.select('h3'))

# div 태그 이면서 id가 harmonyContainer
# print(soup.select('div#harmonyContainer'))

# harmonyContainer 안에 모든 p 태그
# print(soup.select('#harmonyContainer p'))

# harmonyContainer 바로 아래에 있는 p 태그 출력
# print(soup.select('#harmonyContainer > p'))

# class 지정
# print(soup.select('h3.tit_view'))
# print(soup.select('h3[class="tit_view"]'))
# # tx로 시작하는 것만 가져오기
# print(soup.select('h3[class^="tx"]'))
# # 끝이 view
# print(soup.select('h3[class$="view"]'))
# # _ 포함하는 모든 클래스
# print(soup.select('h3[class*="_"]'))

# 해당하는 번째의 것만 가져오기
# print(soup.select('span.txt_info:nth-child(2)'))
