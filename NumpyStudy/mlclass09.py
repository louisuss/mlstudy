### Boolean Indexing
# - ndarray 인덱싱 시 bool 리스트 전달하여 True인 경우만 필터링
import numpy as np

x = np.random.randint(1, 100, size=10)
# [66 71 60 39 35 32  8 15 99 54]
# [True False  True False False  True  True False False  True]
print(x)
print(x%2 == 0)

even_mask = x % 2 == 0

### bool mask
print(even_mask)
print(x[even_mask])
print(x[x%2==0])
print(x[x>30])

### 다중 조건
# - and, or, not 사용 불가
# &, | 사용
# x % 2 == 0
# x < 30
print(x[(x%2==0) & (x < 30)])
print(x[(x<30) | (x > 50)])