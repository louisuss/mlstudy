import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

train_data = pd.read_csv(
    '/Users/louis/Python/AdvancedPython/MachineLearning/PandasStudy/DataFrame/res/train.csv')

# transform 함수

#         PassengerId  Survived        Age     SibSp     Parch       Fare
# Pclass
# 1        461.597222  0.629630  38.233441  0.416667  0.356481  84.154687
# 2        445.956522  0.472826  29.877630  0.402174  0.380435  20.662183
# 3        439.154786  0.242363  25.140620  0.615071  0.393075  13.675550
# 기존 데이터 프레임과 다른 데이터 프레임이 됨 -> transform 사용
print(train_data.groupby('Pclass').mean())


#      PassengerId  Survived        Age     SibSp     Parch       Fare
# 0     439.154786  0.242363  25.140620  0.615071  0.393075  13.675550
# 1     461.597222  0.629630  38.233441  0.416667  0.356481  84.154687
# 2     439.154786  0.242363  25.140620  0.615071  0.393075  13.675550
# 3     461.597222  0.629630  38.233441  0.416667  0.356481  84.154687
# 4     439.154786  0.242363  25.140620  0.615071  0.393075  13.675550
# ..           ...       ...        ...       ...       ...        ...
# 886   445.956522  0.472826  29.877630  0.402174  0.380435  20.662183
# 887   461.597222  0.629630  38.233441  0.416667  0.356481  84.154687
# 888   439.154786  0.242363  25.140620  0.615071  0.393075  13.675550
# 889   461.597222  0.629630  38.233441  0.416667  0.356481  84.154687
# 890   439.154786  0.242363  25.140620  0.615071  0.393075  13.675550
# 원본 인덱스 유지하면서 각 그룹별 통계치를 구함
# 원본의 데이터와 인덱스가 같기 때문에 원본데이터에 데이터 추가가 용이
print(train_data.groupby('Pclass').transform(np.mean))

train_data['Age2'] = train_data.groupby('Pclass').transform(np.mean)['Age']

#       PassengerId  Survived  Pclass  ... Cabin Embarked      Age2
# 0              1         0       3  ...   NaN        S  25.140620
# 1              2         1       1  ...   C85        C  38.233441
# 2              3         1       3  ...   NaN        S  25.140620
# 3              4         1       1  ...  C123        S  38.233441
# 4              5         0       3  ...   NaN        S  25.140620
# ..           ...       ...     ...  ...   ...      ...        ...
# 886          887         0       2  ...   NaN        S  29.877630
# 887          888         1       1  ...   B42        S  38.233441
# 888          889         0       3  ...   NaN        S  25.140620
# 889          890         1       1  ...  C148        C  38.233441
# 890          891         0       3  ...   NaN        Q  25.140620

# [891 rows x 13 columns]
# print(train_data)

# print(train_data.groupby(['Pclass', 'Sex']).mean())
# print(train_data.groupby(['Pclass', 'Sex']).transform(np.mean))


### pivot(index, column, value) / pivot_table

df = pd.DataFrame({
    '지역': ['서울', '부산', '경기', '부산'],
    '요일': ['월', '화', '수', '목'],
    '강수량': [100, 80, 70, 50],
    '강수확률': [80, 70, 90, 10],
})

#    지역 요일 강수량 강수확률
# 0  서울  월  100    80
# 1  부산  화   80    70
# 2  경기  수   70    90
# 3  부산  월   50    10
# print(df)

#     강수량               강수확률
# 요일     수      월     화     수     월     화
# 지역
# 경기  70.0    NaN   NaN  90.0   NaN   NaN
# 부산   NaN   50.0  80.0   NaN  10.0  70.0
# 서울   NaN  100.0   NaN   NaN  80.0   NaN
# print(df.pivot('지역', '요일'))

# 강수량               강수확률
# 지역    경기    부산     서울    경기    부산    서울
# 요일
# 수   70.0   NaN    NaN  90.0   NaN   NaN
# 월    NaN  50.0  100.0   NaN  10.0  80.0
# 화    NaN  80.0    NaN   NaN  70.0   NaN

# print(df.pivot('요일', '지역'))

# 지역    경기    부산     서울
# 요일
# 수   70.0   NaN    NaN
# 월    NaN  50.0  100.0
# 화    NaN  80.0    NaN

# print(df.pivot('요일', '지역', '강수량'))

# 부산 -> 화 두 개로 변경

# 중복 허용 후 호출
# 인덱스가 중복.. 값이 두개라 어떤거 사용할지 모름. 오류
# print(df.pivot('요일', '지역'))

# 강수량               강수확률
# 지역    경기    부산     서울    경기    부산    서울
# 요일
# 수     70.0   NaN    NaN  90.0   NaN   NaN
# 월      NaN   NaN  100.0   NaN   NaN  80.0
# 화      NaN  65.0    NaN   NaN  40.0   NaN
# 중복되는 부분을 평균값으로 채움
print(pd.pivot_table(df, index='요일', columns='지역', aggfunc=np.mean))

new_df = df.set_index(['지역', '요일'])

#        강수량  강수확률
# 지역 요일
# 서울 월   100    80
# 부산 화    80    70
# 경기 수    70    90
# 부산 목    50    10
# print(new_df)
# MultiIndex
# print(new_df.index)

# 지역 인덱스 -> 컬럼레벨

#       강수량               강수확률
# 지역    경기    부산     서울    경기    부산    서울
# 요일
# 목    NaN  50.0    NaN   NaN  10.0   NaN
# 수   70.0   NaN    NaN  90.0   NaN   NaN
# 월    NaN   NaN  100.0   NaN   NaN  80.0
# 화    NaN  80.0    NaN   NaN  70.0   NaN
print(new_df.unstack(0))
# 요일 인덱스 -> 컬럼레벨
# new_df.unstack(1)


# 지역         경기    부산     서울
# 요일
# 목  강수량    NaN  50.0    NaN
#   강수확률   NaN  10.0    NaN
# 수  강수량   70.0   NaN    NaN
#   강수확률  90.0   NaN    NaN
# 월  강수량    NaN   NaN  100.0
#   강수확률   NaN   NaN   80.0
# 화  강수량    NaN  80.0    NaN
#   강수확률   NaN  70.0    NaN
print(new_df.unstack(0).stack(0))

#          강수량  강수확률
# 요일 지역
# 목  부산   50.0  10.0
# 수  경기   70.0  90.0
# 월  서울  100.0  80.0
# 화  부산   80.0  70.0
print(new_df.unstack(0).stack(1))
