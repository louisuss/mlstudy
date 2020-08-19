import numpy as np

# random 서브 모듈

# rand 함수
# - 0, 1 사이의 분포로 랜덤한 ndarray 생성
# 2행 3열
print(np.random.rand(2, 3))
print(np.random.rand(10))
print(np.random.rand(4, 5, 3))

# randn 함수
# - n: normal distribution (정규분포)
# - 정규 분포로 샘플링 된 랜덤 ndarray 생성
print(np.random.randn(3, 4))
print(np.random.randn(3, 4, 2))
print(np.random.randn(5))

# randint 함수
# - 특정 정수 사이에서 랜덤하게 샘플링
print(np.random.randint(1, 100, size=(3, 5)))
print(np.random.randint(1, 100, size=(5,)))

# seed 함수
# - 랜덤한 값을 동일하게 다시 생성하고자 할때 사용

np.random.seed(100)
print(np.random.randn(3,4))

# choice
# - 주어진 1차원 ndarray로 부터 랜덤으로 샘플링
# - 정수가 주어진 경우, np.arange(해당 숫자)로 간주
print(np.random.choice(100, size=(3,4)))
x = np.array([1,2,3,4, 1.5, 2.6])
print(np.random.choice(x, size=(2,2)))
# replace -> 중복값없앰
print(np.random.choice(x, size=(2, 2), replace=False))

y = np.array([1, 2])
# replace 조건 만족할 수 없음 숫자개수가 모자르기때문에
# print(np.random.choice(y, size=(2, 2), replace=False))

# 확률 분포에 따른 ndarray 생성
# - uniform
# - normal
print(np.random.uniform(1.0, 3.0, size=(4,5)))
print(np.random.normal(size=(4,5)))
# = np.random.randn(3,4)


