# Series - Boolean

import numpy as np
import pandas as pd

s = pd.Series(np.arange(10), np.arange(10)+1)

# 1     False
# 2     False
# 3     False
# 4     False
# 5     False
# 6     False
# 7      True
# 8      True
# 9      True
# 10     True
# dtype: bool
print(s > 5)

# 7     6
# 8     7
# 9     8
# 10    9
# dtype: int64
print(s[s > 5])

# 1    0
# 3    2
# 5    4
# 7    6
# 9    8
# dtype: int64
print(s[s % 2 == 0])

# 6     5
# 7     6
# 8     7
# 9     8
# 10    9
# dtype: int64
print(s[s.index > 5])

# 7    6
# 8    7
# dtype: int64
print(s[(s > 5) & (s < 8)])

# 3
# 24
print((s >= 7).sum())
print(s[s >= 7].sum())
