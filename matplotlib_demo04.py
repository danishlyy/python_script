
import matplotlib.pyplot as plt
import numpy as np

# 绘制散点图
x = np.arange(1, 10)
y = x
fig = plt.figure()

plt.scatter(x, y, c='r', marker='o')  # r 表示颜色红色，maker='o' 表示散点为圆形
plt.show()
