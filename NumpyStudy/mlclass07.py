# axis(축) 이해 및 axis 파라미터로 갖는 함수 활용

import numpy as np

x = np.arange(15)

print(np.sum(x))
# 1차원 벡터
print(np.sum(x, axis=0))

# 2차원 행렬에 적용
y = x.reshape(3, 5)

# 행 증가 방향이 0
print(np.sum(y, axis=0))
# 열 증가 방향이 1
print(np.sum(y, axis=1))

# 3차원
z = np.arange(36).reshape(3, 4, 3)
# [[[0  1  2]
#   [3  4  5]
#   [6  7  8]
#   [9 10 11]]

#  [[12 13 14]
#   [15 16 17]
#   [18 19 20]
#   [21 22 23]]

#  [[24 25 26]
#   [27 28 29]
#   [30 31 32]
#   [33 34 35]]]
print(z)

# 3차원 상자 포갬
# [[36 39 42]
#  [45 48 51]
#  [54 57 60]
#  [63 66 69]]
print(np.sum(z, axis=0))

# 행 더하기
# [[18  22  26]
#  [66  70  74]
#  [114 118 122]]
print(np.sum(z, axis=1))

# 열 더하기
# [[3  12  21  30]
#  [39  48  57  66]
#  [75  84  93 102]]
print(np.sum(z, axis=2))


# axis 튜플
# [198 210 222]
print(np.sum(z, axis=(0, 1)))
# [117 144 171 198]
print(np.sum(z, axis=(0, 2)))
