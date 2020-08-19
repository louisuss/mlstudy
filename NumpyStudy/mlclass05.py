import numpy as np

### ravel, np.raval
# - 다차원 배열 1차원으로 변경
# - 'order' 파라미터
# > 'C' - row 우선 변경
# > 'F' - column 우선 변경

# [[0  1  2  3  4]
#  [5  6  7  8  9]
#  [10 11 12 13 14]]
x = np.arange(15).reshape(3, 5)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14] - 행기준
print(np.ravel(x))
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(x.ravel())

# [ 0  5 10  1  6 11  2  7 12  3  8 13  4  9 14] - 열기준
print(np.ravel(x, order='F'))


# flatten
# - 다차원 배열을 1차원으로 변경
# ravel 차이점: copy를 생성하여 변경(즉 원본 데이터가 아닌 복사본 반환)
# 'order' 파라미터
# > 'C' - row 우선 변경
# > 'F' - column 우선 변경

# [[0  1  2  3  4]
#  [5  6  7  8  9]
#  [10 11 12 13 14]]
y = np.arange(15).reshape(3, 5)
print(y)

# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14] - 행기준
print(y.flatten())

# [ 0  5 10  1  6 11  2  7 12  3  8 13  4  9 14] - 열기준
print(y.flatten(order='F'))

temp = x.ravel()
temp[0] = 100

# [100   1   2   3   4   5   6   7   8   9  10  11  12  13  14]
print(temp)

# [[100   1   2   3   4]
#  [5   6   7   8   9]
#  [10  11  12  13  14]]
print(x)

temp2 = y.flatten()
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(temp2)
temp2[0] = 100

# [[0  1  2  3  4]
#  [5  6  7  8  9]
#  [10 11 12 13 14]]
print(y)

z = np.arange(30).reshape(6, 5)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# 24 25 26 27 28 29]
print(z.ravel())

k = np.arange(36).reshape(3, 3, -1)
print(k)

# (3, 3, 4)
print(k.shape)

# 3
print(k.ndim)
