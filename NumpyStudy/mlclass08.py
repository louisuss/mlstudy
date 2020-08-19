# broadcasting
# - shape 같은 ndarray 에 대한 연산은 각 원소별로 진행
# - 연산되는 두 ndarray가 다른 shape를 갖는 경우 shape를 맞춤

import numpy as np

x = np.arange(15).reshape(3, 5)
y = np.random.rand(15).reshape(3, 5)
# print(x+y)

# 상수와의 연산
print(x+2)

# shape 다른 경우
# 뒤 부터 비교
a = np.arange(12).reshape(4, 3)
b = np.arange(100, 103)
c = np.arange(1000, 1004)
d = b.reshape(1, 3)
print(a.shape)
print(b.shape)
# 4, 3 비교 하므로 오류
print(c.shape)

# (1,3) (4,3) 뒤 부터 맞추므로 연산 가능
print(a+d)
