# Series 데이터 연산

import numpy as np
import pandas as pd

# a    1
# b    2
# c    3
# d    4
# dtype: int64
# d    5
# c    4
# b    3
# a    2
# dtype: int64
# a    3
# b    5
# c    7
# d    9
# dtype: int64
s1 = pd.Series(np.arange(1,5), ['a','b','c','d'])
s2 = pd.Series(np.arange(5,1,-1), ['d','c','b','a'])

print(s1)
print(s2)
print(s1+s2)

print(s1**2)

### index pair 맞이 않는 경우
# 해당 인덱스 NaN 값 생성

# a    3.0
# b    5.0
# c    7.0
# d    9.0
# k    NaN
# q    NaN
# dtype: float64
s1['k'] = 7
s2['q'] = 8
print(s1+s2)
