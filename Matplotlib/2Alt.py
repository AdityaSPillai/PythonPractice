import matplotlib.pyplot as plt
import numpy as np

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [100, 250, 150, 300]
colors = plt.cm.coolwarm(np.linspace(0, 1, len(products)))
plt.bar(products, sales, color=colors)

plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data for Different Products")

plt.show()