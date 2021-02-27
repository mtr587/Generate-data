from die import Die
import pygal

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies =[]
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist.title = 'Results of rolling D6 and D10 1000 times.'
xs = []
for value in range(2, max_result + 1):
    xs.append(value)
hist.x_labels = xs
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)
print(sum(frequencies))
