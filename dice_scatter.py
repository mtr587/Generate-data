import matplotlib.pyplot as plt
from die import Die

# 15-10未完成

# 创建两个D6
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies =[]
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
plt.plot(list(range(1, max_result+1)), frequencies, linewidth=2)
plt.title = ('Result of rolling two D6 for 1000 times.')
plt.xlabel = ('Result')
plt.ylabel = ('Square of D6 1000 times')
plt.show()
