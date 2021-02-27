import matplotlib.pyplot as plt

# First cube
x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

plt.title('Cube Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 8, 0, 150])

plt.show()

