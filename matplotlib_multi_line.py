import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi * 2, np.pi * 2, 100)
plt.figure(1, dpi=50)  # 创建图表1
for i in range(1, 5):
    plt.plot(x, np.sin(x / i))
plt.show()
