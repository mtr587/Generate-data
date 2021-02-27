import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_value, squares, linewidth = 5)   # 前两个函数分别为（输入值，输出值）或（x,y）

# 设置图表标题
plt.title('Square Numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Value', fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize = 14)

plt.show()

