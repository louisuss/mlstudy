# chrome -> network -> xhr 보기
# HTTP 상태 코드
# 1XX (정보): 요청을 받았으며 프로세스를 계속함
# 2XX (성공): 요청을 성공적으로 받음
# 3XX (리다이렉션): 요청 완료를 위해 추가 작업 조치 필요
# 4XX (클라이언트 오류): 요청의 문법이 잘못됬거나 요청 처리 불가
# 5XX (서버 오류): 서버가 유효한 요청에 대해 충족 실패

import requests
from bs4 import BeautifulSoup

url = 'https://comment.daum.net/apis/v1/posts/@20200808073012901'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': '''ko-KR, ko
    q = 0.9, en-US
    q = 0.8, en
    q = 0.7''',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb3J1bV9rZXkiOiJuZXdzIiwiZ3JhbnRfdHlwZSI6ImFsZXhfY3JlZGVudGlhbHMiLCJzY29wZSI6W10sImV4cCI6MTU5Njk0MTE2OSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9DTElFTlQiXSwianRpIjoiOGU0ZTVjY2ItMWQ4My00MWMwLWE1YzMtYzk5ODI3OGQxY2VmIiwiZm9ydW1faWQiOi05OSwiY2xpZW50X2lkIjoiMjZCWEF2S255NVdGNVowOWxyNWs3N1k4In0.bRdSnn0_qyxt207BxPnmjveI-N2NSOd5rSlji0_ixgQ',
    'Connection': 'keep-alive',
    'Cookie': '''_TI_NID = iok9mjEFfnWoNqMjDA5hhaBEQhDFWn9IakmV0077HQq5cuuPjcs/9kABU5+vukns1TkKb8nQ/Gf21w/CfgcQZQ ==
    TIARA = LYhf5MDuZtO1gRksHu1wvEieMT5P3sZ57TrXpeCY1-hQa4KKWoR-IzyYg2p_4RoHXnB.2rtPUiacP2Pc4Duoeg00''',
    'Host': 'comment.daum.net',
    'Origin': 'https://news.v.daum.net',
    'Referer': 'https://news.v.daum.net/v/20200808073012901',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': '''Mozilla/5.0 (Macintosh
                                Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'''
}

# resp = requests.get(url, headers=headers)
# # <Response [401]>
# print(resp.json()['commentCount'])

# 로그인해서 데이터 크롤링
# 로그인 자동화하고 로그인에 사용한 세션 유지하여 크롤링 진행

# 1. endpoint 찾기(개발자 도구 network 활용)
# 2. id, password 전달되는 form data 찾기
# 3. session 객체 생성하여 login 진행
# 4. 이후 session 객체로 원하는 페이지로 이동하여 크롤링

# # 로그인 endpoint
# url = 'https://www.kangcom.com/member/member_check.asp'

# # id, password
# data = {
#     'id': 'dobi1115',
#     'pwd': 'dobi1115'
# }

# # 세션 생성
# s = requests.Session()

# # <Response [200] >
# # 세션 유지
# resp = s.post(url, data=data)
# # print(resp)

# my_page = 'htttps://www.kangcom.com/mypage/'
# resp = s.get(my_page)

# # my_page html 정보 받음
# soup = BeautifulSoup(resp.text)

# # milege 부분 태그 설정
# td = soup.select_one('td.a_bbslist55:nth-child(3)')
# mileage = td.get_text()
