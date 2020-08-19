import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train_data = pd.read_csv(
    '/Users/louis/Python/AdvancedPython/MachineLearning/PandasStudy/DataFrame/res/train.csv')

# 새 col 추가
# - [] 사용해서 추가
# - insert 함수 사용해서 원하는 위치에 추가

train_data['Age_double'] = train_data['Age']*2

train_data['Age_tripple'] = train_data['Age_double'] + train_data['Age']

train_data.insert(3, 'Fare10', train_data['Fare']/10)

# col 삭제
# - drop

# 원본데이터 삭제는 안함
train_data.drop('Age_tripple', axis=1)
train_data.drop(['Age_double', 'Age_tripple'], axis=1)
# 원본데이터 삭제
train_data.drop(['Age_double', 'Age_tripple'], axis=1, inplace=True)


# 컬럼 간 상관관계 계산
# corr 함수 통해 상관계수 연산(-1,1 사이의 결과)
# - 연속성(숫자형) 데이터에 대해서만 연산
# - 인과 관계를 의미하지는 않음

# PassengerId  Survived  ...     Parch      Fare
# PassengerId     1.000000 - 0.005007  ... -0.001652  0.012658
# Survived - 0.005007  1.000000  ...  0.081629  0.257307
# Pclass - 0.035144 - 0.338481  ...  0.018443 - 0.549500
# Fare10          0.012658  0.257307  ...  0.216225  1.000000
# Age             0.036847 - 0.077221  ... -0.189119  0.096067
# SibSp - 0.057527 - 0.035322  ...  0.414838  0.159651
# Parch - 0.001652  0.081629  ...  1.000000  0.216225
# Fare            0.012658  0.257307  ...  0.216225  1.000000
# print(train_data.corr())

plt.matshow(train_data.corr())
# plt.show()

# NaN 데이터 처리


# NaN 값 확인
# - info 함수 통해 개수 확인
# - isna 함수 통해 boolean 타입으로 확인
train_data.info()

train_data.isna()

train_data['Age'].isna()

# NaN 처리 방법
# - 데이터 삭제 - dropna 함수
# - 다른값 치환 - fillna 함수
train_data.dropna()
# 'Age' 중에 NaN 만 드랍
train_data.dropna(subset=['Age', 'Cabin'])

# col 레벨로 dropna -> 컬럼에 NaN 있으면 컬럼 삭제
train_data.dropna(axis=1)

# 평균으로 대체
train_data['Age'].fillna(train_data['Age'].mean())

# 생존자/사망자 별 평균으로 대체
# 생존자 나이 평균
mean1 = train_data[train_data['Survived'] == 1]['Age'].mean()

# 사망자 나이 평균
mean0 = train_data[train_data['Survived'] == 0]['Age'].mean()

print(mean1, mean0)

# 생존자 평균을 살아있는 사람 중에 NaN 값인 나이에 채워짐
train_data[train_data['Survived'] == 1]['Age'].fillna(mean1)
# 사망자 평균을 살아있는 사람 중에 NaN 값인 나이에 채워짐
train_data[train_data['Survived'] == 0]['Age'].fillna(mean0)

train_data.loc[train_data['Survived'] == 1,
               'Age'] = train_data[train_data['Survived'] == 1]['Age'].fillna(mean1)

train_data.loc[train_data['Survived'] == 0,
               'Age'] = train_data[train_data['Survived'] == 0]['Age'].fillna(mean0)

print(train_data)