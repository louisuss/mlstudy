# linalg
import numpy as np

# np.linalg.inv
# - 역행렬
# - 모든 차원의 값이 같아야함
x = np.random.rand(3, 3)

# @ 행렬 곱
print(x @ np.linalg.inv(x))
print(np.matmul(x, np.linalg.inv(x)))


# np.linalg.solve
# - Ax = B 형태의 선형대수식 솔루션 제공
A = np.array([[1, 1], [2, 4]])
B = np.array([25, 64])

# [18.  7.]
x = np.linalg.solve(A, B)
print(x)

# 검산 True
print(np.allclose(A@x, B))
