import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# plt.scatter(x_values, y_values, s=200)  # s为点的尺寸

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
# s为点的尺寸；c为点的内在颜色，默认蓝色，也可以用RGB定色；cmap为渐变选择的颜色；edgecolor为数据点轮廓,默认为黑色轮廓
# c=y_values意思是根据y_value而颜色渐变

# 设置图表标题并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])

# 若要自动保存则使用plt.savefig()，否则用plt.show()
plt.savefig('square_plot.png', bbox_inches='tight')
# 第一个实参指定要以什么样的文件名保存图表，这个文件将存储到scatter_squares.py所在的
# 目录中；第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，
# 可省略这个实参。

#plt.show()
