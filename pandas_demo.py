from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 5, 6, - 7])
# 0    4
# 1    5
# 2    6
# 3   -7
# dtype: int64
print(obj)
print(obj.index)  # RangeIndex(start=0, stop=4, step=1)
print(obj.values)  # [ 4  5  6 -7]

# d    4
# b    7
# c   -5
# a    3
# dtype: int64
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'c', 'a'])
print(obj2)

obj2['c'] = 6
# d    4
# b    7
# c    6
# a    3
# dtype: int64
print(obj2)

print('a' in obj2)  # True

# 字典 -> Series
dic = {"beijing": 1000, "shanghai": 30000, "guangzhou": 5000, "shenzhen": 8000}
obj4 = Series(dic)
# beijing       1000
# shanghai     30000
# guangzhou     5000
# shenzhen      8000
# dtype: int64
print(obj4)

obj4.index = ['bj', 'sh', 'gz', 'sz']
# bj     1000
# sh    30000
# gz     5000
# sz     8000
# dtype: int64
print(obj4)
