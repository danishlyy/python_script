import pandas as pd
from pandas import DataFrame, Series
from numpy import nan as na
import numpy as np

data = {
    'city': ['shanghai', 'shanghai', 'beijing', 'shanghai', 'beijing'],
    'year': [2016, 2017, 2018, 2017, 2018],
    'prop': [1.5, 1.7, 3.6, 2.4, 2.9]
}

# DataFrame 是一个二维表格
df = DataFrame(data)
#        city  year  prop
# 0  shanghai  2016   1.5
# 1  shanghai  2017   1.7
# 2   beijing  2018   3.6
# 3  shanghai  2017   2.4
# 4   beijing  2018   2.9
print(df)
# 对 DataFrame 进行按列名排序
df1 = DataFrame(data, columns=['year', 'city', 'prop'])
#    year      city  prop
# 0  2016  shanghai   1.5
# 1  2017  shanghai   1.7
# 2  2018   beijing   3.6
# 3  2017  shanghai   2.4
# 4  2018   beijing   2.9
print(df1)
# 0    shanghai
# 1    shanghai
# 2     beijing
# 3    shanghai
# 4     beijing
# Name: city, dtype: object
print(df1['city'])
# 0    shanghai
# 1    shanghai
# 2     beijing
# 3    shanghai
# 4     beijing
# Name: city, dtype: object
print(df1.city)

df1['new'] = 100
#    year      city  prop  new
# 0  2016  shanghai   1.5  100
# 1  2017  shanghai   1.7  100
# 2  2018   beijing   3.6  100
# 3  2017  shanghai   2.4  100
# 4  2018   beijing   2.9  100
print(df1)
df1['cap'] = df1.city == 'beijing'
#    year      city  prop  new    cap
# 0  2016  shanghai   1.5  100  False
# 1  2017  shanghai   1.7  100  False
# 2  2018   beijing   3.6  100   True
# 3  2017  shanghai   2.4  100  False
# 4  2018   beijing   2.9  100   True
print(df1)

pop = {
    "beijing": {2008: 1.5, 2009: 2.0},
    "shanghai": {2008: 2.0, 2009: 3.6}
}
df3 = DataFrame(pop)
#       beijing  shanghai
# 2008      1.5       2.0
# 2009      2.0       3.6
print(df3)

# 行列转置
#           2008  2009
# beijing    1.5   2.0
# shanghai   2.0   3.6
print(df3.T)
obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'c', 'd', 'a'])
# reindex
obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'])
# a    3.6
# b    4.5
# c    7.2
# d   -5.3
# e    NaN
# dtype: float64
print(obj5)
# 默认填充 NaN 对应位置的值
obj6 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
# a    3.6
# b    4.5
# c    7.2
# d   -5.3
# e    0.0
# dtype: float64
print(obj6)

# 用上面的值进行填充
obj7 = Series(['blue', 'red', 'yellow'], index=[0, 2, 4])
# 0      blue
# 2       red
# 4    yellow
# dtype: object
print(obj7)
obj8 = obj7.reindex(range(6), method='ffill')
# 0      blue
# 1      blue
# 2       red
# 3       red
# 4    yellow
# 5    yellow
# dtype: object
print(obj8)

# 用后面得一个值进行填充
obj9 = Series(['a', 'b', 'c'], index=[0, 2, 4])
# 0    a
# 2    b
# 4    c
# dtype: object
print(obj9)
obj10 = obj9.reindex(range(6), method='bfill')
# 0      a
# 1      b
# 2      b
# 3      c
# 4      c
# 5    NaN
# dtype: object
print(obj10)

na1 = Series(['hello', na, 'world'])
# 0    hello
# 1      NaN
# 2    world
# dtype: object
print(na1)
# dtype: object
# 0    hello
# 2    world
print(na1.dropna())
na2 = na1.dropna()
# 0    hello
# 1      NaN
# 2    world
# dtype: object
print(na1)
# 0    hello
# 2    world
# dtype: object
print(na2)

df4 = DataFrame([[1, 2, 3], [4, na, na], [na, 5, na]])
#      0    1    2
# 0  1.0  2.0  3.0
# 1  4.0  NaN  NaN
# 2  NaN  5.0  NaN
print(df4)
#      0    1    2
# 0  1.0  2.0  3.0
print(df4.dropna())
#      0    1    2
# 0  1.0  2.0  3.0
# 1  4.0  NaN  NaN
# 2  NaN  5.0  NaN
print(df4)

df5 = DataFrame([[1, 2, 3], [4, na, na], [na, na, na]])
#      0    1    2
# 0  1.0  2.0  3.0
# 1  4.0  NaN  NaN
# 2  NaN  NaN  NaN
print(df5)
# 删除整行是na的值
#      0    1    2
# 0  1.0  2.0  3.0
# 1  4.0  NaN  NaN
print(df5.dropna(how='all'))
df6 = DataFrame([[1, 2, na], [4, na, na], [na, na, na]])
#      0    1   2
# 0  1.0  2.0 NaN
# 1  4.0  NaN NaN
# 2  NaN  NaN NaN
print(df6)
# 删除某列全是na的
#      0    1
# 0  1.0  2.0
# 1  4.0  NaN
# 2  NaN  NaN
print(df6.dropna(axis=1, how='all'))
#      0    1    2
# 0  1.0  2.0  0.0
# 1  4.0  0.0  0.0
# 2  0.0  0.0  0.0
print(df6.fillna(0))
#      0    1   2
# 0  1.0  2.0 NaN
# 1  4.0  NaN NaN
# 2  NaN  NaN NaN
print(df6)
print(df6.fillna(0, inplace=True))  # None
#      0    1    2
# 0  1.0  2.0  0.0
# 1  4.0  0.0  0.0
# 2  0.0  0.0  0.0
print(df6)


