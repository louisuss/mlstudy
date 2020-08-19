import numpy as np

# np.array 함수 생성
# 1차원 벡터 생성
x = np.array([1, 2, 3, 4])
print(x)

# 2차원 벡터
y = np.array([[2, 3, 4], [1, 2, 5]])
print(y)

# np.arange 함수 생성
# range 함수랑 동일
print(np.arange(10))
print(np.arange(1, 10))
print(np.arange(1, 10, 2))


# np.ones / np.zeros
# 모든 원소가 1로 구성된 ndarray

# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]
print(np.ones((4, 5)))

# 3행4열 행렬 2개 생성 - 3차원
print(np.ones((2, 3, 4)))

# 모든 원소가 0으로 구성된 ndarray
print(np.zeros((2, 3, 8)))
print(np.zeros((2, 3, 8, 8)))
print(np.zeros((2, 3)))


# np.empty / np.full
# 임의 값이 들어간 행렬 생성
print(np.empty((3, 4)))

# 특정 값으로 이루어진 행렬 생성
print(np.full((2, 3), 7))
# 리스트는 안됨
# print(np.full((2,3), [1,2]))

# 단위 행렬 - 대각선 부분 다 1 / 나머지 다 0 인 행렬

# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]
print(np.eye(5))

# 3개 출력 / 1과 10사이에 값의 차이가 동일한 값 생성
# [1.   5.5 10.] - 2등분
print(np.linspace(1, 10, 3))
# [ 1.  4.  7. 10.] - 3등분
print(np.linspace(1, 10, 4))
# [1.    3.25  5.5   7.75 10.] - 5등분
print(np.linspace(1, 10, 5))


# ndarray의 형태, 차원을 바꾸기 위해 사용
x = np.arange(1, 16)
print(x)

# (15,)
print(x.shape)

# 2차원 행렬로 바꾸고 싶을 때
print(x.reshape(3, 5))
print(x.reshape(5, 3))
# 개수가 모자르기 때문에 에러
# print(x.reshape(5, 4))
# 5개 3행 1열
print(x.reshape(5, 3, 1))
