import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

train_data = pd.read_csv(
    '/Users/louis/Python/AdvancedPython/MachineLearning/PandasStudy/DataFrame/res/train.csv')

df1 = pd.DataFrame({'key1': np.arange(3), 'value1': np.random.randn(3)})
df2 = pd.DataFrame({'key1': np.arange(3), 'value1': np.random.randn(3)})

# concat

#    key1    value1
# 0     0  0.395862
# 1     1  2.263196
# 2     2 - 0.402268
# 0     0  0.096614
# 1     1  1.143715
# 2     2 - 0.867969

# 병합을 해도 인덱스가 유지
# print(pd.concat([df1, df2]))

#    key1    value1
# 0     0 - 0.173534
# 1     1  1.374693
# 2     2  0.155230
# 3     0 - 0.563960
# 4     1 - 1.268976
# 5     2 - 0.706688
# print(pd.concat([df1, df2], ignore_index=True))

#    key1    value1  key1    value1
# 0     0  0.837840     0  0.250193
# 1     1  0.555851     1 - 0.688510
# 2     2 - 0.483115    2  0.196533

# 사용 별로 안함
# print(pd.concat([df1, df2], axis=1))

#     key1    value1  key2    value2
# 0   0.0 - 0.941417   NaN       NaN
# 1   1.0  1.280393   NaN       NaN
# 2   2.0 - 0.401973   NaN       NaN
# 0   NaN       NaN   0.0  1.354766
# 1   NaN       NaN   1.0 - 0.103879
# 2   NaN       NaN   2.0  0.906303
df3 = pd.DataFrame({'key2': np.arange(3), 'value2': np.random.randn(3)})
print(pd.concat([df1, df3]))

#    key1    value1  key2    value2
# 0     0 - 0.283707     0 - 0.659178
# 1     1 - 2.088215     1  0.301073
# 2     2  0.738975     2 - 0.232669
print(pd.concat([df1, df3], axis=1))


# DataFrame Merge

customer = pd.DataFrame({
    'customer_id': np.arange(6),
    'name': ['철수', '영희', '길동', '영수', '수민', '동건'],
    '나이': [40, 20, 21, 30, 31, 17]
})

orders = pd.DataFrame({
    'customer_id': [1, 1, 2, 2, 2, 3, 3, 1, 4, 9],
    'item': ['치약', '칫솔', '이어폰', '수건', '생수', '수건', '치약', '케이스', '치약', '케이스'],
    'quantity': [1, 2, 3, 1, 4, 12, 3, 4, 5, 6],
})

# print(customer)
# print(orders)

# on
# - join 대상이 되는 컬럼 명시

#    customer_id name  나이  item  quantity
# 0            1   영희  20   치약         1
# 1            1   영희  20   칫솔         2
# 2            1   영희  20  케이스         4
# 3            2   길동  21  이어폰         3
# 4            2   길동  21   수건         1
# 5            2   길동  21   생수         4
# 6            3   영수  30   수건        12
# 7            3   영수  30   치약         3
# 8            4   수민  31   치약         5

# inner join - 동건, 9번 표시안됨
print(pd.merge(customer, orders, on='customer_id', how='inner'))

#    customer_id name  나이 item  quantity
# 0             0   철수  40  NaN       NaN
# 1             1   영희  20   치약       1.0
# 2             1   영희  20   칫솔       2.0
# 3             1   영희  20  케이스       4.0
# 4             2   길동  21  이어폰       3.0
# 5             2   길동  21   수건       1.0
# 6             2   길동  21   생수       4.0
# 7             3   영수  30   수건      12.0
# 8             3   영수  30   치약       3.0
# 9             4   수민  31   치약       5.0
# 10            5   동건  17  NaN       NaN

# 철수, 동건 생김
print(pd.merge(customer, orders, on='customer_id', how='left'))

#     customer_id name   나이  item   quantity
# 0            1   영희  20.0   치약         1
# 1            1   영희  20.0   칫솔         2
# 2            1   영희  20.0  케이스         4
# 3            2   길동  21.0  이어폰         3
# 4            2   길동  21.0   수건         1
# 5            2   길동  21.0   생수         4
# 6            3   영수  30.0   수건        12
# 7            3   영수  30.0   치약         3
# 8            4   수민  31.0   치약         5
# 9            9  NaN   NaN  케이스         6

# 9번 생김
print(pd.merge(customer, orders, on='customer_id', how='right'))

#     customer_id  name   나이 item  quantity
# 0             0   철수  40.0  NaN       NaN
# 1             1   영희  20.0   치약       1.0
# 2             1   영희  20.0   칫솔       2.0
# 3             1   영희  20.0  케이스       4.0
# 4             2   길동  21.0  이어폰       3.0
# 5             2   길동  21.0   수건       1.0
# 6             2   길동  21.0   생수       4.0
# 7             3   영수  30.0   수건      12.0
# 8             3   영수  30.0   치약       3.0
# 9             4   수민  31.0   치약       5.0
# 10            5   동건  17.0  NaN       NaN
# 11            9  NaN   NaN  케이스       6.0
print(pd.merge(customer, orders, on='customer_id', how='outer'))


# left_index, right_index 파라미터
# index 기준으로 join 하기
c1 = customer.set_index('customer_id')
o1 = orders.set_index('customer_id')

#             name  나이
# customer_id
# 0             철수  40
# 1             영희  20
# 2             길동  21
# 3             영수  30
# 4             수민  31
# 5             동건  17
# print(c1)

#              item  quantity
# customer_id
# 1             치약         1
# 1             칫솔         2
# 2            이어폰         3
# 2             수건         1
# 2             생수         4
# 3             수건        12
# 3             치약         3
# 1            케이스         4
# 4             치약         5
# 9            케이스         6
# print(o1)

#              name  나이 item  quantity
# customer_id
# 1             영희  20   치약         1
# 1             영희  20   칫솔         2
# 1             영희  20  케이스         4
# 2             길동  21  이어폰         3
# 2             길동  21   수건         1
# 2             길동  21   생수         4
# 3             영수  30   수건        12
# 3             영수  30   치약         3
# 4             수민  31   치약         5
# 굳이 on 명시할 필요 없음. 둘다 인덱스로 merge한다 명시했기 때문
# print(pd.merge(c1, o1, left_index=True, right_index=True))

# 가장 많이 팔린 아이템?

#        customer_id  나이  quantity
# item
# 수건              5  51        13
# 치약              8  81         9
# 생수              2  21         4
# 케이스             1  20         4
# 이어폰             2  21         3
# 칫솔              1  20         2
print(pd.merge(customer, orders, on='customer_id').groupby(
    'item').sum().sort_values(by='quantity', ascending=False))

#           customer_id  나이  quantity
# name item
# 영수   수건              3  30        12
# 수민   치약              4  31         5
# 길동   생수              2  21         4
# 영희   케이스             1  20         4
# 길동   이어폰             2  21         3
# 영수   치약              3  30         3
# 영희   칫솔              1  20         2
# 길동   수건              2  21         1
# 영희   치약              1  20         1
print(pd.merge(customer, orders, on='customer_id').groupby(
    ['name', 'item']).sum().sort_values(by='quantity', ascending=False))

#        customer_id  나이  quantity
# item
# 케이스             1  20         4
# 칫솔              1  20         2
# 치약              1  20         1
print(pd.merge(customer, orders, on='customer_id').groupby(
    ['name', 'item']).sum().loc['영희'].sort_values(by='quantity', ascending=False))

# item
# 치약     1
# 칫솔     2
# 케이스    4
# Name: quantity, dtype: int64
print(pd.merge(customer, orders, on='customer_id').groupby(
    ['name', 'item']).sum().loc['영희', 'quantity'])

# join 함수

#             name  나이 item  quantity
# customer_id
# 0             철수  40  NaN       NaN
# 1             영희  20   치약       1.0
# 1             영희  20   칫솔       2.0
# 1             영희  20  케이스       4.0
# 2             길동  21  이어폰       3.0
# 2             길동  21   수건       1.0
# 2             길동  21   생수       4.0
# 3             영수  30   수건      12.0
# 3             영수  30   치약       3.0
# 4             수민  31   치약       5.0
# 5             동건  17  NaN       NaN
print(c1.join(o1))

#             name  나이 item  quantity
# customer_id
# 1             영희  20   치약         1
# 1             영희  20   칫솔         2
# 1             영희  20  케이스         4
# 2             길동  21  이어폰         3
# 2             길동  21   수건         1
# 2             길동  21   생수         4
# 3             영수  30   수건        12
# 3             영수  30   치약         3
# 4             수민  31   치약         5
print(c1.join(o1, how='inner'))
