from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone, BaseEstimator
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, precision_recall_curve, roc_curve, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import ssl
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

# dict_keys(['data', 'target', 'frame', 'categories', 'feature_names',
    #    'target_names', 'DESCR', 'details', 'url'])
mnist = fetch_openml('mnist_784', version=1)
# print(mnist.keys())
X, y = mnist["data"], mnist["target"]
# (70000, 784)
# (70000,)
# print(X.shape)
# print(y.shape)

some_digit = X[0]
some_digit_image = some_digit.reshape(28, 28)

# plt.imshow(some_digit_image, cmap="binary")
# plt.axis("off")
# plt.show()
# print(y[0])
y = y.astype(np.uint8)
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

# 이진 분류기
y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5)
# [ True]
# print(sgd_clf.predict([some_digit]))

# 교차 검증을 사용한 정확도 측정

# 교차 검증 구현
# 1. 클래스별 비율이 유지되도록 폴드를 만들기 위해 계층적 샘플링 수행
# skfolds = StratifiedKFold(n_splits=3, random_state=42)

# 0.95035
# 0.96035
# 0.9604
# 매 반복에서 분류기 객체를 복제하여 훈련 폴드로 훈련시키고 테스트 폴드로 예측
# 올바른 예측의 수를 세어 정확한 예측의 비율 출력

# for train_index, test_index in skfolds.split(X_train, y_train_5):
#     clone_clf = clone(sgd_clf)
#     X_train_folds = X_train[train_index]
#     y_train_folds = y_train_5[train_index]
#     X_test_fold = X_train[test_index]
#     y_test_fold = y_train_5[test_index]

#     clone_clf.fit(X_train_folds, y_train_folds)
#     y_pred = clone_clf.predict(X_test_fold)
#     n_correct = sum(y_pred == y_test_fold)
#     print(n_correct / len(y_pred))

# 2. cross_val_score()
# [0.95035 0.96035 0.9604 ]
# print(cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring="accuracy"))

# 3. 5 아님 클래스로 분류


class Never5Classifier(BaseEstimator):
    def fit(self, X, y=None):
        return self

    def predict(self, X):
        return np.zeros((len(X), 1), dtype=bool)


never_5_clf = Never5Classifier()
# [0.91125 0.90855 0.90915]
# print(cross_val_score(never_5_clf, X_train, y_train_5, cv=3, scoring="accuracy"))

# 오차 행렬
# 더 나은 방법임. 클래스 A의 샘플이 클래스 B로 분류된 횟수를 세는 것
# 실제 타깃과 비교할 수 있도록 먼저 예측값 만들어야함
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)
# [[53892   687]
#  [1891  3530]]
# 완벽한 분류기라면 대각선 부분만 0이 아닌 값
# print(confusion_matrix(y_train_5, y_train_pred))

# 정밀도와 재현율
# 4096/(4096+1522)
# 0.8370879772350012
# print(precision_score(y_train_5, y_train_pred))
# 4096/(4096+1325)
# 0.6511713705958311
# print(recall_score(y_train_5, y_train_pred))
# 0.7325171197343846
# print(f1_score(y_train_5, y_train_pred))

# 정밀도/재현율 트레이드오프
# 임계값 지정
y_scores = sgd_clf.decision_function([some_digit])
# [2164.22030239]
# print(y_scores)
threshold = 0
y_some_digit_pred = (y_scores > threshold)
# [True]
# print(y_some_digit_pred)

threshold = 8000
y_some_digit_pred = (y_scores > threshold)
# [False]
# print(y_some_digit_pred)

# 훈련세트에 있는 모든 샘플의 점수를 구함. 결정 점수를 반환받도록 지정
y_scores = cross_val_predict(
    sgd_clf, X_train, y_train_5, cv=3, method="decision_function")
# [1200.93051237 - 26883.79202424 - 33072.03475406 ...  13272.12718981
#  - 7258.47203373 - 16877.50840447]
# print(y_scores)

precisions, recalls, thresholds = precision_recall_curve(y_train_5, y_scores)


def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], "b--", label="정밀도")
    plt.plot(thresholds, recalls[:-1], "g-", label="재현율")

# plot_precision_recall_vs_threshold(precisions, recalls, thresholds)
# plt.show()
# np.argmax() : 최댓값의 첫번째 인덱스 반환
# threshold_90_precision = thresholds[np.argmax(precisions >= 0.90)]
# 훈련 세트에 대한 예측 만듬
# y_train_pred_90 = (y_scores >= threshold_90_precision)

# 0.9000345901072293
# 0.4799852425751706
# print(precision_score(y_train_5, y_train_pred_90))
# print(recall_score(y_train_5, y_train_pred_90))

# ROC 곡선

# fpr: 거짓 양성 비율 / tpr: 진짜 양성 비율


fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)


def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
# ROC곡선: 민감도(재현율)에 대한 1-특이도 그래프
# plot_roc_curve(fpr, tpr)
# plt.show()
# 0.9604938554008616
# print(roc_auc_score(y_train_5, y_scores))


forest_clf = RandomForestClassifier(random_state=42)
y_probas_forest = cross_val_predict(
    forest_clf, X_train, y_train_5, cv=3, method="predict_proba")
y_scores_forest = y_probas_forest[:, 1]
fpr_forest, tpr_forest, thresholds_forest = roc_curve(
    y_train_5, y_scores_forest)

# plt.plot(fpr, tpr, "b:", label="SGD")
# plot_roc_curve(fpr_forest, tpr_forest, "랜덤 포레스트")
# plt.legend(loc="lower right")
# plt.show()
# 0.9983436731328145
# print(roc_auc_score(y_train_5, y_scores_forest))


# 다중 분류
svm_clf = SVC()
svm_clf.fit(X_train, y_train)
print(svm_clf.predict([some_digit]))

some_digit_scores = svm_clf.decision_function([some_digit])
print(some_digit_scores)
print(np.argmax(some_digit_scores))
print(svm_clf.classes_)
print(svm_clf.classes_[5])

ovr_clf = OneVsRestClassifier(SVC())
ovr_clf.fit(X_train, y_train)
print(ovr_clf.predict([some_digit]))
print(len(ovr_clf.estimators_))

print(sgd_clf.fit(X_train, y_train))
print(sgd_clf.predict([some_digit]))
print(sgd_clf.decision_function([some_digit]))
print(cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring="accuracy"))

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train.astype(np.float64))
print(cross_val_score(sgd_clf, X_train_scaled, y_train, cv=3, scoring="accuracy"))

# 에러 분석
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train, cv=3)
conf_mx = confusion_matrix(y_train, y_train_pred)
print(conf_mx)

plt.matshow(conf_mx, cmap=plt.cm.gray)
plt.show()

row_sums = conf_mx.sum(axis=1, keepdims=True)
norm_conf_mx = conf_mx / row_sums

np.fill_diagonal(norm_conf_mx, 0)
plt.matshow(norm_conf_mx, cmap=plt.cm.gray)
plt.show()

y_train_large = (y_train >= 7)
y_train_odd = (y_train % 2 == 1)
y_multilabel = np.c_[y_train_large, y_train_odd]

knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train, y_multilabel)

print(knn_clf.predict([some_digit]))

y_train_knn_pred = cross_val_predict(knn_clf, X_train, y_multilabel, cv=3)
print(f1_score(y_multilabel, y_train_knn_pred, average="macro"))

noise = np.random.randint(0, 100, (len(X_train), 784))
X_train_mod = X_train + noise
noise = np.random.randint(0, 100, (len(X_test), 784))
X_test_mod = X_test + noise
y_train_mod = X_train
y_test_mod = X_test

knn_clf.fit(X_train_mod, y_train_mod)
clean_digit = knn_clf.predict([X_test_mod[some_index]])
plot_digit(clean_digit)
