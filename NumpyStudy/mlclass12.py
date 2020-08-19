# 로또 번호 생성기
import numpy as np
import matplotlib.pyplot as plt

# 중복됨
# lotto = np.random.randint(1, 45, 6)
# replace = 중복여부


def generate_lotto_nums():
    lotto = np.random.choice(np.arange(1, 46), size=6, replace=False)
    return lotto


print(generate_lotto_nums())

# pi 값 계산 - 몬테 카를로 방법 이용 (난수 발생해서 어떤값의 근사치 추정)


# pi/4 : 1 = (4분원 안에 생성된 점 개수) : 전체 시도 횟수
# pi = 4 * (4분원 안 생성 점 개수) / 1e7
total = int(1e7)
# 0~1 사이 값
# 2 -> x, y
# total -> 각 점
points = np.random.rand(total, 2)
# 전체 개수 중 4분원 안에 들어있는 점개수
print(np.sum(np.sum(points**2, axis=1) < 1))
pi = 4 * (np.sum(np.sum(points**2, axis=1) < 1)) / total
print(pi)
