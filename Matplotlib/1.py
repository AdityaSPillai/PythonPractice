import matplotlib.pyplot as plt

x = []
y = []

for i in range(11):
    x.append(i)
    y.append(i*i)

plt.plot(x, y, label="Class A", color="purple", linestyle="-", marker="o")

plt.title("Square of a number")
plt.xlabel("Number")
plt.ylabel("Square")

plt.show()