# https://numpy.org/doc/stable/numpy-ref.pdf

import numpy as np

x = np.arange(15).reshape(3, 5)
y = np.random.rand(15).reshape(3, 5)
# print(x)
# print(y)

# 연산함수
# add, subtract, multiply, divide
# +, -, *, /
# x, y 행렬 크기 같아야함
print(np.add(x, y))
print(np.subtract(x, y))
print(x+y)
print(x-y)

### 통계 함수
# 평균, 분산, 중앙, 최대, 최대값 인덱스, 최소, 최소값 인덱스
print(np.mean(x))

# 최대값 인덱스 (2차 행렬이여도 flatten한 상태의 인덱스 가져옴)
print(np.argmax(x))

# 분산
print(np.var(x))

# 평균
print(np.median(x))

# 표준편차
print(np.std(x))

# 집계함수
# sum, cumsum(누적합계)

# axis 축
print(np.sum(y))
print(np.cumsum(y))

### any, all
# any: 특정 조건 만족하는 것이 하나라도 있으면 True, 아니면 False
# all: 모든 원소가 특정 조건 만족 True, 아니면 False
z = np.random.randn(10)
# True
print(np.any(z>0))
# False
print(np.all(z>0))

### where
# 조건에 따라 선별적으로 값을 선택
print(np.where(z > 0, z, 0))