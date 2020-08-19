# Series 데이터 심플 분석(개수, 빈도 등 계산)

import numpy as np
import pandas as pd

# size, shape, unique, count, value_counts 함수
s = pd.Series([1, 2, 12, 1, 235, 1, 4, 34, 15, np.NaN])
# 10
# (10,)
print(s.size)
print(s.shape)
# [  1.   2.  12. 235.   4.  34.  15.  nan]
print(s.unique())
# 9
print(s.count())

a = np.array([2,2,2,2, np.NaN])
# nan
print(a.mean())
# 33.888888888888886
print(s.mean())

# 1.0      3
# 15.0     1
# 34.0     1
# 4.0      1
# 235.0    1
# 12.0     1
# 2.0      1
# dtype: int64
print(s.value_counts())


### head, tail 함수
print(s.head())
print(s.head(n=3))
print(s.tail())
