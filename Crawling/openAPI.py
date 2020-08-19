# OPEN API 활용
# 1. 공공데이터 포털
# 2. API 사용 요청 / 키 발급
# 3. API 문서 확인
# 4. API 테스트 및 개발

# key 값 확인
# - 서비스 호출 트래킹할 목적이나 악의적인 사용을 금지할 목적으로 주로 사용

from urllib import urlencode, quote_plus
from urllib2 import Request, urlopen
service_key = 'rjpiGWFC4HdqwHE3oC7E0 % 2BXAgcvCyh6iA98jJDBu88y2sBNTUpM5ROmFvDOHwZgXmUpg4cFRjkqLiddca9Ndaw % 3D % 3D'

# Endpoint 확인
# - API가 서비스되는 서버의 IP 혹은 domain 주소
# endpoint = 'http: // api.visitkorea. or .kr/openapi/service{}'.format(service_key)
# resp = requests.get(endpoint)
# resp.json()

# Parameter 확인
# - API 호출에 필요한 parameter 값 확인 및 구성


# request 및 response 확인
# requests 모듈 활용하여 API 호출
# response 확인하여 원하는 정보 추출
# json 데이터의 경우, python dictionary로 변경하여 사용 가능


url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode'
queryParams = '?' + urlencode({quote_plus('ServiceKey'): '서비스키', quote_plus('ServiceKey'): '인증키 (URL - Encode)', quote_plus('numOfRows'): '10', quote_plus('pageNo'): '1', quote_plus('MobileOS'): 'ETC', quote_plus('MobileApp'): 'AppTest', quote_plus('areaCode'): '1'})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)
