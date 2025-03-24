import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y, color='red', marker='*', s=100)

plt.title("Scatter Plot of X vs Y")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True)

plt.show()