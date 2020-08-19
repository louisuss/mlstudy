# Series 값 변경

import numpy as np
import pandas as pd


### Series 값 변경
# - 변경: 인덱스 이용
# - 삭제: drop 함수 사용
s = pd.Series(np.arange(100,105), ['a','b','c','d','e'])

s['k'] = 300

# a    100
# b    101
# c    102
# d    103
# e    104
# dtype: int64
# a    100
# b    101
# c    102
# d    103
# e    104
# k    300
# dtype: int64
# drop -> s에 영향 없음
print(s.drop('k'))
print(s)

# None
# a    100
# b    101
# c    102
# d    103
# e    104
# dtype: int64
print(s.drop('k', inplace=True))
print(s)

# 여러 값 한번에 변경
# a    300
# b    900
# c    102
# d    103
# e    104
# dtype: int64
s[['a','b']] = [300, 900]
print(s)

### 슬라이싱
s1 = pd.Series(np.arange(100, 105))

# 숫자 슬라이싱 - 마지막 포함 안됨
# 1    101
# 2    102
# dtype: int64
print(s1[1:3])

# b    101
# c    102
# dtype: int64
s2 = pd.Series(np.arange(100, 105), ['a', 'b', 'c', 'd', 'e'])
print(s2[1:3])

# 문자열 인덱스는 마지막도 포함됨
# b    101
# c    102
# d    103
# dtype: int64
print(s2['b':'d'])
