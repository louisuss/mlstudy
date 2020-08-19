import pandas as pd
import numpy as np

# 원하는 컬럼만 선택
train_data = pd.read_csv(
    '/Users/louis/Python/AdvancedPython/MachineLearning/PandasStudy/DataFrame/res/train.csv')

# 컬럼 하나
# Series 데이터
print(train_data['Survived'])
# 복수 컬럼
# 데이터 프레임 데이터
print(train_data[['Survived', 'Name']])


# 원하는 로우만 선택

# 데이터 프레임 슬라이싱
# - row 레벨로 지원

# PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 7            8         0       3  ...  21.0750   NaN         S
# 8            9         1       3  ...  11.1333   NaN         S
# 9           10         1       2  ...  30.0708   NaN         C

# [3 rows x 12 columns]

print(train_data[7:10])

# row 선택하기
# - Series 경우 []로 선택 가능, 데이터 프레임은 기본적으로 col 선택하도록 설계
# loc - 인덱스 자체 사용
# iloc - 0 based index 사용
# 이 두 함수는 ,를 사용하여 column 선택도 가능

# 891개 데이터
print(train_data.info())

#     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 100            1         0       3  ...   7.2500   NaN         S
# 101            2         1       1  ...  71.2833   C85         C
# 102            3         1       3  ...   7.9250   NaN         S
# 103            4         1       1  ...  53.1000  C123         S
# 104            5         0       3  ...   8.0500   NaN         S

# [5 rows x 12 columns]
train_data.index = np.arange(100, 991)
print(train_data.head())

# PassengerId                      887
# Survived                           0
# Pclass                             2
# Name           Montvila, Rev. Juozas
# Sex                             male
# Age                               27
# SibSp                              0
# Parch                              0
# Ticket                        211536
# Fare                              13
# Cabin                            NaN
# Embarked                           S
# Name: 986, dtype: object
print(train_data.loc[986])

# PassengerId  Survived  Pclass  ...   Fare Cabin  Embarked
# 986          887         0       2  ...  13.00   NaN         S
# 100            1         0       3  ...   7.25   NaN         S
print(train_data.loc[[986, 100]])

# [2 rows x 12 columns]
# Survived                     Name   Age
# 986         0    Montvila, Rev. Juozas  27.0
# 100         0  Braund, Mr. Owen Harris  22.0
print(train_data.loc[[986, 100], ['Survived', 'Name', 'Age']])

# [2 rows x 12 columns]
# PassengerId                          1
# Survived                             0
# Pclass                               3
# Name           Braund, Mr. Owen Harris
# Sex                               male
# Age                                 22
# SibSp                                1
# Parch                                0
# Ticket                       A/5 21171
# Fare                              7.25
# Cabin                              NaN
# Embarked                             S
# Name: 100, dtype: object
print(train_data.iloc[0])

# Survived     Sex   Age
# 201         0    male   NaN
# 200         0  female  28.0
print(train_data.iloc[[101, 100], [1, 4, 5]])
