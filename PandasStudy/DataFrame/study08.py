import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

train_data = pd.read_csv(
    '/Users/louis/Python/AdvancedPython/MachineLearning/PandasStudy/DataFrame/res/train.csv')

# 숫자 데이터와 범주형 데이터

# 숫자형 데이터
# - 연속성을 띄는 숫자로 이루어진 데이터
# - Age, Fare 등

# 범주형 데이터 (범주를 의미)
# - 연속적이지 않은 값(대부분의 경우 숫자를 제외한 나머지 값)을 갖는 데이터 의미
# - Name, Sex. Ticket, Cabin, Embarked
# - 어떤 경우, 숫자형 타입이라 할지라도 개념적으로 범주형으로 처리해야 할 경우가 있음
# - Pclass

# 숫자 데이터의 범주형 데이터화

# astype 사용해서 타입만 변환

# Pclass 변수 변환하기
# int64
print(train_data.info())

train_data['Pclass'] = train_data['Pclass'].astype(str)
# object
print(train_data.info())

# Age 변수 변환하기
# - 변환 로직을 함수로 만든 후, apply 함수 적용


def age_categorize(age):
    # 23 -> 20, 38 -> 30
    if math.isnan(age):
        return -1
    return math.floor(age/10) * 10


print(train_data['Age'].apply(age_categorize))


# 범주형 데이터 전처리하기 (one-hot encoding)
# - 연산이 불가하기 떄문에 숫자형으로 바꿔야 함

# One-hot encoding
# - 범주형 데이터는 분석 단계에서 계산이 어렵기 때문에 숫자형으로 변경이 필요
# - 범주형 데이터의 각 범주를 column 레벨로 변경
# - 해당 범주에 해당하면 1, 아니면 0으로 채우는 인코딩 기법
# - pandas.get_dummies 함수 사용 - drop_first: 첫번째 카테고리 값은 사용안함

#    PassengerId  Survived  ... Embarked_Q  Embarked_S
# 0              1         0  ...          0           1
# 1              2         1  ...          0           0
# 2              3         1  ...          0           1
# 3              4         1  ...          0           1
# 4              5         0  ...          0           1
# ..           ...       ...  ...        ...         ...
# 886          887         0  ...          0           1
# 887          888         1  ...          0           1
# 888          889         0  ...          0           1
# 889          890         1  ...          0           0
# 890          891         0  ...          1           0
print(pd.get_dummies(train_data, columns=[
      'Pclass', 'Sex', 'Embarked'], drop_first=True))
