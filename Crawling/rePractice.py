import re

# search 활용
# 찾고자하는 패턴 / 특정 문자열
# 패턴 없는 경우 None 반환
m = re.search(r'abc', '123abcdef')
# match 객체 - m.start(), m.end(), m.group()

# <class 're.Match' >
# 3
# 6
# abc
print(type(m))
print(m.start())
print(m.end())
print(m.group())

# 숫자 2개가 나란히 있는 것이 있는지
# search 는 가장먼저 찾는 패턴을 출력
m = re.search(r'\d\d\w', '112abcdef119')
print(m)

m = re.search(r'..\w\w', '@#!@ABCDabcd')
print(m)

print(re.search(r'[cbm]at', 'cat'))
print(re.search(r'[cbm]at', 'bat'))
print(re.search(r'[0-3]haha', '1haha'))
print(re.search(r'[abc.^]aron', '^aron'))
print(re.search(r'[^abc]aron', 'daron'))

# b로 시작하고 어떤 숫자나 문자가 1번이상 반복 후 a로 끝남
# <re.Match object; span=(0, 6), match='banana'>
print(re.search(r'b\w+a', 'banana'))
# ii 출력 - 문자열 첫번째 인덱스부터 시작해서 가장 빨리 매치되는 것만 찾음
re.search(r'i+', 'piigiii')

# 검출 실패
re.search(r'pi+g', 'pg')
# 검출 성공
re.search(r'pi*g', 'pg')

# s가 한번 있거나 없거나
re.search(r'https?', 'https://www.naver.com')

# <re.Match object; span=(2, 6), match='bana'>
print(re.search(r'b\w+a', 'cabana'))

# 문자열 시작이 c이므로 검출안됨
print(re.search(r'^b\w+a', 'cabana'))

# b로 시작하고 a로 끝나는 문자
print(re.search(r'b\w+a$', 'cabana'))

# <re.Match object; span=(0, 14), match='test@gmail.com'>
print(re.search(r'\w+@.+', 'test@gmail.com'))

# test@gmail.com
# test
# gmail.com
m = re.search(r'(\w+)@(.+)', 'test@gmail.com')
print(m.group(0))
print(m.group(1))
print(m.group(2))


# None
print(re.search('pi{3}g', 'piiiig'))
# <re.Match object; span=(0, 5), match='piiig'>
print(re.search('pi{3}g', 'piiig'))

# None
print(re.search('pi{3,5}g', 'piiiiiig'))

# <re.Match object; span=(0, 17), match='<html>haha</html>'>
print(re.search(r'<.+>', '<html>haha</html>'))

# 미니멈 매칭 - <re.Match object; span=(0, 6), match='<html>'>
print(re.search(r'<.+?>', '<html>haha</html>'))

# <re.Match object; span=(0, 5), match='aaaaa'>
# <re.Match object; span=(0, 3), match='aaa'>
print(re.search(r'a{3,5}', 'aaaaa'))
print(re.search(r'a{3,5}?', 'aaaaa'))


# None
# <re.Match object; span=(0, 3), match='123'>
print(re.match(r'\d\d\d', 'my number is 123'))
print(re.match(r'\d\d\d', '123 is my number'))

# ['test@gmail.com', 'test2@gmail.com']
# ['test@gmail', 'test2@gmail']
# [\w.]+ - .이나 어떤 문자의 한번 이상의 반복
print(re.findall(r'[\w-]+@[\w.]+',
                 'test@gmail.com haha test2@gmail.com nice test'))
print(re.findall(r'[\w-]+@[\w]+',
                 'test@gmail.com haha test2@gmail.com nice test'))


# great.com haha great.com nice test
print(re.sub(r'[\w-]+@[\w.]+', 'great',
             'test@gmail.com haha test2@gmail.com nice test'))

# great.com haha test2@gmail.com nice test
print(re.sub(r'[\w-]+@[\w.]+', 'great',
             'test@gmail.com haha test2@gmail.com nice test', count=1))

# <re.Match object; span=(0, 10), match='test@gmail'>

email_reg = re.compile(r'[\w-]+@[\w.]+')
print(email_reg.search('test@gmail.com haha'))


email_reg = re.compile(r'[\w-]+@[\w.]+')

# test@gmail.com. 방지위해 변경
email_reg = re.compile(r'[\w-]+@[\w.]+\w+')

webs = [
    'http://www.test.co.kr',
    'htp://www.test.co.kr',
    'ttp://www.test.co.kr',
    'https://www.test.com',
    'https://www.test.com.',
    'https:/www.test.com',
    'https//www.test.com',
]

# 문자로 한번이상 반복되면서 끝남
web_reg = re.compile(r'https?://[\w.]+\w+$')
# [True, False, False, True, False, False, False]
print(list(map(lambda w: web_reg.search(w) != None, webs)))
