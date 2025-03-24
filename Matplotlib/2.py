import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [100, 250, 150, 300]

fig, ax = plt.subplots()

for i, (product, sale) in enumerate(zip(products, sales)):
    gradient = np.linspace(0, 1, 256).reshape(256, 1)
    gradient = np.repeat(gradient, 20, axis=1)
    
    ax.imshow(gradient, extent=[i - 0.4, i + 0.4, 0, sale], cmap="coolwarm", aspect="auto")

    rect = patches.Rectangle((i - 0.4, 0), 0.8, sale, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(rect)

ax.set_xticks(range(len(products)))
ax.set_xticklabels(products)
ax.set_xlabel("Products")
ax.set_ylabel("Sales")
ax.set_title("Sales Data with Blue-to-Red Gradient Bars")
ax.set_ylim(0, max(sales) + 50)

plt.show()