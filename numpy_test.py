import numpy as np

arr1 = np.array([2, 3, 4])
arr2 = np.array([1.2, 3.4, 2.3])
print(arr1)  # [2 3 4]
print(arr2)  # [1.2 3.4 2.3]
print(arr1.dtype)  # int64
print(arr2.dtype)  # float64

arr3 = arr1 + arr2
print(arr3)  # [3.2 6.4 6.3]

# 与标量计算
print(arr2 * 10)  # [12. 34. 23.]

data = [[1, 2, 3], [4, 5, 6]]
arr4 = np.array(data)
# [[1 2 3]
#  [4 5 6]]
# 矩阵
print(arr4)

n = np.zeros(10)
print(n)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(n.dtype)  # float64
# 产生一个3R5C的矩阵
n1 = np.zeros((3, 5))
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
print(n1)
# 生成一个2R3C的全是1的矩阵
n2 = np.ones((2, 3))
# [[1. 1. 1.]
#  [1. 1. 1.]]
print(n2)
n3 = np.empty((3, 4, 2))
# [[[0. 0.]
#   [0. 0.]
#   [0. 0.]
#   [0. 0.]]
#
#  [[0. 0.]
#   [0. 0.]
#   [0. 0.]
#   [0. 0.]]
#
#  [[0. 0.]
#   [0. 0.]
#   [0. 0.]
#   [0. 0.]]]
print(n3)

a1 = np.arange(10)
print(a1)  # [0 1 2 3 4 5 6 7 8 9]
print(a1[5])  # 5
print(a1[5:8])  # [5 6 7]
a1[5:8] = 10
print(a1)  # [ 0  1  2  3  4 10 10 10  8  9]

a_slice = a1[5:8].copy()
a_slice[:] = 15
print(a_slice)  # [15 15 15]
print(a1)  # [ 0  1  2  3  4 10 10 10  8  9]
