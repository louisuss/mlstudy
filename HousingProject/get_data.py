import os
import ssl
import tarfile
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from zlib import crc32
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
import joblib

# DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml2/blob/master/" - raw data 여야 에러 안나는듯?
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


# 데이터 다운로드
def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):

    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
            getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")

    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

# 다운로드 된 데이터 읽기


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

# 무작위로 샘플 선택해서 데이터셋의 20% 정도를 떼어놓음
# 불완전 - 다음번에 업데이트된 데이터셋을 사용하려면 문제가 됨


def split_train_test(data, test_ratio):
    # 길이만큼 무작위 조합
    shuffled_indices = np.random.permutation(len(data))
    # 테스트셋 크기
    test_set_size = int(len(data) * test_ratio)

    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    # iloc: 행번호를 통해 행 데이터 가져옴
    return data.iloc[train_indices], data.iloc[test_indices]


# 샘플의 식별자를 사용하여 테스트 세트로 보낼지 말지 정함. 샘플이 고유하고 변경 불가능한 식별자를 가지고 있다고 가정
# 해시값 계산하여 해시 최댓값의 20%보다 작거나 같은 샘플만 테스트 세트로 지정 가능 - 갱신시에도 테스트 세트가 동일하게 유지
def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2 ** 32

# 식별자 대신 행의 인덱스를 ID로 사용


def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

# <1H OCEAN     9136
# INLAND        6551
# NEAR OCEAN    2658
# NEAR BAY      2290
# ISLAND           5
# Name: ocean_proximity, dtype: int64
# print(housing['ocean_proximity'].value_counts())

# print(housing.describe())
# housing.hist(bins=50, figsize=(20, 15))
# plt.show()
# --------- 순수한 무작위 샘플링 방식 ---------------
# 데이터셋이 충분히 크면 괜찮지만, 아니면 샘플링 편향 가능성 큼


fetch_housing_data()
housing = load_housing_data()
train_set, test_set = split_train_test(housing, 0.2)

# 인덱스 열이 추가된 데이터 프레임 반환
housing_with_id = housing.reset_index()
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

# 행의 인덱스를 고유 식별자로 사용할 때 새 데이터는 데이터셋의 끝에 추가되어야 함. 어떤 데이터도 삭제되지 않아야 함.
# 이것이 불가능할 때 고유 식별자를 만드는 데 안전한 특성 사용
# ex) 위도, 경도는 몇백 년 후까지 안정적이므로 두 값을 연결하여 ID 만듬
housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")

# 사이킷런은 데이터셋을 여러 서브셋으로 나누는 다양한 방법 제공 - train_test_split
# 1. random_state 매개변수 : 난수 초깃값 지정
# 2. 행의 개수가 같은 여러 개의 데이터셋을 넘겨서 같은 인덱스를 기반으로 나눌 수 있음
# (데이터 프레임이 레이블에 따라 여러 개로 나뉘어 있을 때 매우 유용)
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

housing["income_cat"] = pd.cut(housing["median_income"], bins=[
                               0., 1.5, 3.0, 4.5, 6., np.inf], labels=[1, 2, 3, 4, 5])
# housing["income_cat"].hist()
# plt.show()

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

# 전체 데이터셋에 있는 소득 카테고리의 비율 측정
# 전체 데이터셋과 계층 샘플링으로 만든 테스트 세트에서 소득 카테고리 비율을 비교
# print(strat_test_set["income_cat"].value_counts()/len(strat_test_set))

# income_cat 특성을 삭제해서 데이터를 원래 상태로 돌림
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)

housing = strat_train_set.copy()
# housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
# housing.plot(kind="scatter", x='longitude', y="latitude", alpha=0.4,
#  s=housing["population"]/100, label="population", figsize=(10, 7), c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,)
# plt.legend()
# plt.show()

# 표준 상관계수
# corr_matrix = housing.corr()
# print(corr_matrix["median_house_value"].sort_values(ascending=False))

# 숫자형 특성 사이에 산점도를 그려줌
# attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
# scatter_matrix(housing[attributes], figsize=(12,8))
# plt.show()

# 상관 관계가 매우 강함
# housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)
# plt.show()

# 가구당 방 개수
# housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
# 전체 침대 개수
# housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
# 가구당 인원
# housing["population_per_household"] = housing["population"]/housing["households"]

# corr_matrix = housing.corr()
# print(corr_matrix["median_house_value"].sort_values(ascending=False))

housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()
# 누락된 특성 처리
# 해당 구역 제거
housing.dropna(subset=["total_bedrooms"])
# 전체 특성 삭제
housing.drop("total_bedrooms", axis=1)
# 훈련 세트에 중간값을 계산하고 누락된 값을 이 값으로 채워 넣어야함
median = housing["total_bedrooms"].median()
housing["total_bedrooms"].fillna(median, inplace=True)
# 누락된 값을 특성의 중간값으로 대체
imputer = SimpleImputer(strategy="median")
# 중간값이 수치형 특성에서만 계산 가능. ocean_proximity를 제외한 데이터 복사본 생성
housing_num = housing.drop("ocean_proximity", axis=1)
# 훈련 데이터에 적용
imputer.fit(housing_num)
# imputer는 각 특성의 중간값을 계산해서 그 결과를 객체의 statistics_ 속성에 저장
# print(imputer.statistics_)
# print(housing_num.median().values)

# 변형된 특성들이 들어 있는 넘파이 배열
X = imputer.transform(housing_num)
housing_tr = pd.DataFrame(
    X, columns=housing_num.columns, index=housing_num.index)

# 텍스트/범주형 특성 다루기
housing_cat = housing[["ocean_proximity"]]
# housing_cat.head(5)
ordinal_encoder = OrdinalEncoder()
housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
# print(housing_cat_encoded[:5])
# print(ordinal_encoder.categories_)
cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
# 희소행렬. 수천 개의 카테고리가 있는 범주형 특성일 경우 효율적
# 0이 아닌 원소의 위치만 저장
# print(housing_cat_1hot.toarray())


rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

# 변환기 만들기


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)
# print(housing_extra_attribs)

# 변환 파이프라인
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
])

housing_num_tr = num_pipeline.fit_transform(housing_num)

# 수치형 열이름 리스트
num_attribs = list(housing_num)
# 범주형 열이름 리스트
cat_attribs = ["ocean_proximity"]

full_pipeline = ColumnTransformer([
    # 이름, 변환기, 변환기가 적용될 열 이름(인덱스)
    ("num", num_pipeline, num_attribs),
    ("cat", OneHotEncoder(), cat_attribs),
])
housing_prepared = full_pipeline.fit_transform(housing)
lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)

some_data = housing.iloc[:5]
some_labels = housing_labels.iloc[:5]
some_data_prepared = full_pipeline.transform(some_data)
# print("Guess: ", lin_reg.predict(some_data_prepared))
# print("Label: ", list(some_labels))

housing_predictions = lin_reg.predict(housing_prepared)
lin_mse = mean_squared_error(housing_labels, housing_predictions)
lin_rmse = np.sqrt(lin_mse)
# 과소적합
# print(lin_rmse)

tree_reg = DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_labels)
housing_predictions = tree_reg.predict(housing_prepared)
tree_mse = mean_squared_error(housing_labels, housing_predictions)
tree_rmse = np.sqrt(tree_mse)
# 과적합
# print(tree_rmse)

scores = cross_val_score(tree_reg, housing_prepared,
                         housing_labels, scoring="neg_mean_squared_error", cv=10)
tree_rmse_scores = np.sqrt(-scores)


def display_scores(scores):
    print("점수: ", scores)
    print("평균: ", scores.mean())
    print("표준편차: ", scores.std())

# display_scores(tree_rmse_scores)


lin_scores = cross_val_score(
    lin_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
lin_rmse_scores = np.sqrt(-lin_scores)
# display_scores(lin_rmse_scores)

forest_reg = RandomForestRegressor()
forest_reg.fit(housing_prepared, housing_labels)
forest_scores = cross_val_score(
    forest_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
forest_rmse_scores = np.sqrt(-forest_scores)
# display_scores(forest_rmse_scores)

# 실험 모델 저장
# 교차 검증 점수와 실제 예측값, 하이퍼파라미터와 훈련된 모델 파라미터 모두 저장
# 여러 모델의 점수와 모델이 만든 오차를 쉽게 비교 가능
joblib.dump(my_model, "my_model.pkl")
my_model_load = joblib.load("my_model.pkl")
