# find, find_all, get_text(), attribute

from bs4 import BeautifulSoup

# html 문자열 파싱
# - 문자열로 정의된 html 데이터 파싱

# find 함수
# - html tag 검색
# - 검색 조건을 명시하여 찾고자 하는 tag 검색
html = """
<h3>Hi</h3>
<p>HI2</p>
<div cutom='95'>
"""
soup = BeautifulSoup(html)
soup.find('h3')
soup.find('p')
soup.find('div', custom='95')
# soup.find('div', class='95') -> error
soup.find('div', class_='95')
attrs = {
    'id': 'upper',
    'class': 'test',
}
soup.find('div', attrs=attrs)


# find_all 함수
# - 조건에 맞는 모든 tag를 리스트로 반환
soup.find_all('div')

# get_text 함수
# - tag 안의 value 추출
# - 부모 tag의 경우, 모든 자식 tag의 value를 추출
tag = soup.find('h3')
tag.get_text()

# 부모 태그
tag = soup.find('div', id='upper')
# 자식 값 다 가져옴
tag.get_text()


# attribute 값 추출
# - 추출하고자 하는 값이 attribute에도 존재
# - 검색한 tag 에 attribute 이름을 [] 연산을 통해 추출 가능
# - div.find('h3')['title']

tag = soup.find('h3')
tag['title']
