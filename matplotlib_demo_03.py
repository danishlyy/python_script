import matplotlib.pyplot as plt

# 直方图
plt.figure(1, dpi=50)
data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
plt.hist(data)
plt.show()