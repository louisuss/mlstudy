import pandas as pd

# DataFrame 생성
# - 일반적으로 분석을 위한 데이터는 다른 데이터 소스(database, 외부파일)을 통해 dataframe 생성
# - dummy 데이터 생성 방법


# read_csv 함수
# - sep: 각 데이터 값을 구별하기 위한 구분자 설정
# - header: header를 무시 할 경우, None 설정
# - index_col: index로 사용 할 column 설정
# - usecols: 실제로 dataframe에 로딩 할 columns만 설정

train_data = pd.read_csv(
    '/Users/louis/Python/AdvancedPython/MachineLearning/PandasStudy/DataFrame/res/train.csv', index_col='PassengerId', usecols=['PassengerId', 'Survived', 'Name'])

# Survived  Pclass  ... Cabin Embarked
# PassengerId                    ...
# 1                   0       3  ...   NaN        S
# 2                   1       1  ...   C85        C
# 3                   1       3  ...   NaN        S
# 4                   1       1  ...  C123        S
# 5                   0       3  ...   NaN        S
print(train_data.head())

# 5 rows x 11 columns]
#     Index(['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
#            'Fare', 'Cabin', 'Embarked'],
# dtype = 'object')
print(train_data.columns)

