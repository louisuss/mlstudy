# 사용률 낮음
# Series 데이터


import numpy as np
import pandas as pd

# 0    1
# 1    2
# 2    3
# dtype: int64
s1 = pd.Series([1, 2, 3])
print(s1)

# 0    a
# 1    b
# 2    c
# dtype: object
s2 = pd.Series(['a', 'b', 'c'])
print(s2)


# 0        0
# 1        1
# 2        2
# 3        3
# 4        4
# ...
# 195    195
# 196    196
# 197    197
# 198    198
# 199    199
# Length: 200, dtype: int64
s3 = pd.Series(np.arange(200))
print(s3)

# 1    0
# 2    1
# 3    2
# dtype: int64
s4 = pd.Series(np.arange(3), (1, 2, 3))
print(s4)

# a    0
# b    1
# c    2
# dtype: int64
s5 = pd.Series(np.arange(3), ('a', 'b', 'c'))
print(s5)

# 100    0
# 101    1
# 102    2
# 103    3
# 104    4
# dtype: int32
s6 = pd.Series(np.arange(5), np.arange(100, 105), dtype=np.int32)
print(s6)
# Int64Index([100, 101, 102, 103, 104], dtype='int64')
print(s6.index)
# [0 1 2 3 4]
print(s6.values)


# 인덱스 통한 데이터 접근
print(s6[100])

# 인덱스 데이터 업데이트
s6[104] = 60
print(s6[104])

# 100     0
# 101     1
# 102     2
# 103     3
# 104    60
# 106    90
# dtype: int64
# 인덱스 에러 뜨지 않음 - 그냥 추가
s6[106] = 90
s6[107] = 90
print(s6)

# 인덱스 재사용

# 100    0
# 101    1
# 102    2
# 103    3
# 104    4
# 106    5
# 107    6
# dtype: int64
s7 = pd.Series(np.arange(7), s6.index)
print(s7)

# 인덱스 활용해서 여러 값에 접근
# 100    0
# 101    1
# dtype: int64
# [[]] 형식
print(s7[[100, 101]])
