import pandas as pd

# DataFrame 생성
# - 일반적으로 분석을 위한 데이터는 다른 데이터 소스(database, 외부파일)을 통해 dataframe 생성
# - dummy 데이터 생성 방법

train_data = pd.read_csv(
    '/Users/louis/Python/AdvancedPython/MachineLearning/PandasStudy/DataFrame/res/train.csv')

# dict 생성
# - key = col
data = {'a': 100, 'b': 200, 'c': 300}
a = pd.DataFrame(data, index=['x', 'y', 'z'])

# a    b    c
# x  100  200  300
# y  100  200  300
# z  100  200  300
print(a)

# a  b  c
# 0  1  4  7
# 1  2  5  8
# 2  3  6  9
# 인덱스 길이 맞아야 함
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
b = pd.DataFrame(data, index=[0, 1, 2])
print(b)

# Series로 부터 생성
# - Series 인덱스 -> column

# a      b      c      d      e
# 100  100.0  200.0  300.0    NaN    NaN
# 101  101.0  201.0    NaN  301.0    NaN
# 102  110.0  210.0    NaN    NaN  310.0
c = pd.Series([100, 200, 300], ['a', 'b', 'c'])
e = pd.Series([101, 201, 301], ['a', 'b', 'd'])
f = pd.Series([110, 210, 310], ['a', 'b', 'e'])

i = pd.DataFrame([c, e, f], index=[100, 101, 102])
print(i)
