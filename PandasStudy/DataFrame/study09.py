import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

train_data = pd.read_csv(
    '/Users/louis/Python/AdvancedPython/MachineLearning/PandasStudy/DataFrame/res/train.csv')

# group by
# - 데이터 분할
# - operation 적용
# - 데이터 병합

# 컬럼 전달
class_group = train_data.groupby('Pclass')
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f9e3feb4b20>
# print(class_group)
# print(class_group.groups)

gender_gorup = train_data.groupby('Sex')
# print(gender_gorup)
# print(gender_gorup.groups)

# PassengerId  Survived  Name  ...  Fare  Cabin  Embarked
# Pclass                               ...
# 1               216       216   216  ...   216    176       214
# 2               184       184   184  ...   184     16       184
# 3               491       491   491  ...   491     12       491
# print(class_group.count())


# Pclass
# 1    38.233441
# 2    29.877630
# 3    25.140620
# Name: Age, dtype: float64
print(class_group.mean()['Age'])

# Pclass
# 1    0.629630
# 2    0.472826
# 3    0.242363
# Name: Survived, dtype: float64
print(class_group.mean()['Survived'])

# print(class_group.min())
# print(class_group.max())

# Sex
# female    0.742038
# male      0.188908
# Name: Survived, dtype: float64
print(train_data.groupby('Sex').mean()['Survived'])

# 복수 컬럼으로 그루핑하기
# - groupby에 컬럼 리스트 전달
# - 통계함수를 적용한 결과는 multiindex를 갖는 dataframe

# 클래스와 성별에 따른 생존률 구하기

# MultiIndex([(1, 'female'),
#             (1,   'male'),
#             (2, 'female'),
#             (2,   'male'),
#             (3, 'female'),
#             (3,   'male')],
#            names=['Pclass', 'Sex'])
print(train_data.groupby(['Pclass', 'Sex']).mean().index)


# PassengerId  Survived  ...     Parch        Fare
# Pclass Sex                            ...
# 1      female   469.212766  0.968085  ...  0.457447  106.125798
#          male     455.729508  0.368852  ...  0.278689   67.226127
# 2      female   443.105263  0.921053  ...  0.605263   21.970121
#          male     447.962963  0.157407  ...  0.222222   19.741782
# 3      female   399.729167  0.500000  ...  0.798611   16.118810
#          male     455.515850  0.135447  ...  0.224784   12.661633
print(train_data.groupby(['Pclass', 'Sex']).mean())

# [6 rows x 6 columns]
# PassengerId    443.105263
# Survived         0.921053
# Age             28.722973
# SibSp            0.486842
# Parch            0.605263
# Fare            21.970121
# 인덱싱
# Name: (2, female), dtype: float64
print(train_data.groupby(['Pclass', 'Sex']).mean().loc[(2, 'female')])


# Pclass  Sex
# 1       female    0.968085
#           male      0.368852
# 2       female    0.921053
#           male      0.157407
# 3       female    0.500000
#           male      0.135447
# Name: Survived, dtype: float64
print(train_data.groupby(['Pclass', 'Sex']).mean()['Survived'])


# 인덱스를 이용한 groupby
# - 인덱스가 있는 경우 groupby 함수에 level 사용 가능
# > level은 index의 depth를 의미하며, 가장 왼쪽부터 0부터 증가

# set_index()
# - col 데이터를 인덱스 레벨로 변경

# reset_index()
# - 인덱스 초기화

# 'Pclass'가 인덱스가 됨
train_data.set_index('Pclass')
# 'Pclass', 'Sex'가 멀티 인덱스가 됨
train_data.set_index(['Pclass', 'Sex'])
# 인덱스 있는것을 없앰
train_data.set_index(['Pclass', 'Sex']).reset_index()

# 'Age'가 인덱스 -> level=0 -> 'Age'로 groupby
print(train_data.set_index('Age').groupby(level=0).mean())

# 나이대별 생존율 (10대, 20대...)
# groupby에 함수를 줄 수 있음


def age_categorize(age):
    if math.isnan(age):
        return -1
    return math.floor(age/10) * 10


#       PassengerId  Survived    Pclass     SibSp     Parch       Fare
# # -1   435.581921  0.293785  2.598870  0.564972  0.180791  22.158567
# # 0    424.741935  0.612903  2.629032  1.854839  1.403226  30.576679
# # 10   444.362745  0.401961  2.470588  0.666667  0.470588  32.535132
# # 20   433.231818  0.350000  2.450000  0.322727  0.250000  27.278937
# # 30   472.449102  0.437126  2.113772  0.353293  0.329341  40.377294
# # 40   465.606742  0.382022  1.966292  0.370787  0.471910  38.002297
# # 50   440.187500  0.416667  1.562500  0.291667  0.270833  47.933333
# # 60   433.736842  0.315789  1.473684  0.263158  0.368421  48.367542
# # 70   496.500000  0.000000  1.833333  0.166667  0.166667  30.197233
# # 80   631.000000  1.000000  1.000000  0.000000  0.000000  30.000000
print(train_data.set_index('Age').groupby(age_categorize).mean())

# -1    0.293785
# 0     0.612903
# 10    0.401961
# 20    0.350000
# 30    0.437126
# 40    0.382022
# 50    0.416667
# 60    0.315789
# 70    0.000000
# 80    1.000000
# Name: Survived, dtype: float64
# 나이대별 생존율
print(train_data.set_index('Age').groupby(age_categorize).mean()['Survived'])

# MultiIndex를 이용한 grouping

#                PassengerId  Survived        Age     SibSp     Parch        Fare
# Pclass    Sex
# 1      female   469.212766  0.968085  34.611765  0.553191  0.457447  106.125798
#          male   455.729508  0.368852  41.281386  0.311475  0.278689   67.226127
# 2      female   443.105263  0.921053  28.722973  0.486842  0.605263   21.970121
#          male   447.962963  0.157407  30.740707  0.342593  0.222222   19.741782
# 3      female   399.729167  0.500000  21.750000  0.895833  0.798611   16.118810
#          male   455.515850  0.135447  26.507589  0.498559  0.224784   12.661633
print(train_data.set_index(['Pclass', 'Sex']).groupby(level=[0, 1]).mean())

#       PassengerId               Survived      ... Parch             Fare
# mean     sum amax      mean sum  ...   sum amax        mean        sum      amax
# Pclass    Sex                                            ...
# 1      female  469.212766   44106  888  0.968085  91  ...    43    2  106.125798  9975.8250  512.3292
#          male    455.729508   55599  890  0.368852  45  ...    34    4   67.226127  8201.5875  512.3292
# 2      female  443.105263   33676  881  0.921053  70  ...    46    3   21.970121  1669.7292   65.0000
#          male    447.962963   48380  887  0.157407  17  ...    24    2   19.741782  2132.1125   73.5000
# 3      female  399.729167   57561  889  0.500000  72  ...   115    6   16.118810  2321.1086   69.5500
#          male    455.515850  158064  891  0.135447  47  ...    78    5   12.661633  4393.5865   69.5500

# [6 rows x 18 columns]
# aggregate(집계) 함수 사용
print(train_data.set_index(['Pclass', 'Sex']).groupby(
    level=[0, 1]).aggregate([np.mean, np.sum, np.max]))
