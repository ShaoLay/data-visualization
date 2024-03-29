import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# 设置图标标题, 并给坐标轴加上标签
plt.title("Squares values")
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
