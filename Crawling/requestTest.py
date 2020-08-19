# get, post
# text, status_code, headers

import requests

url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=293&aid=0000030207'

# HTTP get 요청
resp = requests.get(url)
# print(resp.text)

# URL만으로 크롤링 안되는 경우 - 헤더 보기
# 헤더에 user-agent 재정의 필요
# 헤더 정보 사용
url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=293&aid=0000030207'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
resp = requests.get(url, headers=headers)
# print(resp.text)
# Response 처리
# print(resp.status_code)
if resp.status_code == 200:
    print(resp.text)
else:
    print('Error')


# post - 민감한 데이터 정보 사용 시 사용 (로그인 등)
url = 'https://www.kangcom.com/member/member_check.asp'
data = {
    'id': 'dobi1115',
    'pwd': '12343453'
}
resp = requests.post(url, data=data)
# print(resp.text)
