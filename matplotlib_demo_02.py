import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)  # x轴定义为-3.14~3.14 中间间隔100个元素
plt.plot(x, np.sin(x))
# 显示绘制的图
plt.show()
