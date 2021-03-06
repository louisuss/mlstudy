import pandas as pd
import numpy as np


train_data = pd.read_csv(
    '/Users/louis/Python/AdvancedPython/MachineLearning/PandasStudy/DataFrame/res/train.csv')

# PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 0            1         0       3  ...   7.2500   NaN         S
# 1            2         1       1  ...  71.2833   C85         C
# 2            3         1       3  ...   7.9250   NaN         S
# 3            4         1       1  ...  53.1000  C123         S
# 4            5         0       3  ...   8.0500   NaN         S

# print(train_data.head())

### Boolean Selection
class_ = train_data['Pclass'] == 1
age_ = ((train_data['Age'] >= 30) & (train_data['Age'] < 40))

#     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
# 1              2         1       1  ...   71.2833          C85         C
# 3              4         1       1  ...   53.1000         C123         S
# 61            62         1       1  ...   80.0000          B28       NaN
# 137          138         0       1  ...   53.1000         C123         S
# 215          216         1       1  ...  113.2750          D36         C
# 218          219         1       1  ...   76.2917          D15         C
# 224          225         1       1  ...   90.0000          C93         S
# 230          231         1       1  ...   83.4750          C83         S
# 248          249         1       1  ...   52.5542          D35         S
# 257          258         1       1  ...   86.5000          B77         S
# 258          259         1       1  ...  512.3292          NaN         C
# 269          270         1       1  ...  135.6333          C99         S
# 273          274         0       1  ...   29.7000         C118         C
# 309          310         1       1  ...   56.9292          E36         C
# 318          319         1       1  ...  164.8667           C7         S
# 325          326         1       1  ...  135.6333          C32         C
# 332          333         0       1  ...  153.4625          C91         S
# 383          384         1       1  ...   52.0000          NaN         S
# 390          391         1       1  ...  120.0000      B96 B98         S
# 412          413         1       1  ...   90.0000          C78         Q
# 447          448         1       1  ...   26.5500          NaN         S
# 452          453         0       1  ...   27.7500         C111         C
# 486          487         1       1  ...   90.0000          C93         S
# 512          513         1       1  ...   26.2875          E25         S
# 520          521         1       1  ...   93.5000          B73         S
# 537          538         1       1  ...  106.4250          NaN         C
# 540          541         1       1  ...   71.0000          B22         S
# 558          559         1       1  ...   79.6500          E67         S
# 572          573         1       1  ...   26.3875          E25         S
# 577          578         1       1  ...   55.9000          E44         S
# 581          582         1       1  ...  110.8833          C68         C
# 583          584         0       1  ...   40.1250          A10         C
# 604          605         1       1  ...   26.5500          NaN         C
# 632          633         1       1  ...   30.5000          B50         C
# 671          672         0       1  ...   52.0000          B71         S
# 679          680         1       1  ...  512.3292  B51 B53 B55         C
# 690          691         1       1  ...   57.0000          B20         S
# 701          702         1       1  ...   26.2875          E24         S
# 716          717         1       1  ...  227.5250          C45         C
# 737          738         1       1  ...  512.3292         B101         C
# 741          742         0       1  ...   78.8500          C46         S
# 759          760         1       1  ...   86.5000          B77         S
# 763          764         1       1  ...  120.0000      B96 B98         S
# 806          807         0       1  ...    0.0000          A36         S
# 809          810         1       1  ...   53.1000           E8         S
# 822          823         0       1  ...    0.0000          NaN         S
# 835          836         1       1  ...   83.1583          E49         C
# 842          843         1       1  ...   31.0000          NaN         C
# 867          868         0       1  ...   50.4958          A24         S
# 872          873         0       1  ...    5.0000  B51 B53 B55         S

# [50 rows x 12 columns]
print(train_data[class_ & age_])
