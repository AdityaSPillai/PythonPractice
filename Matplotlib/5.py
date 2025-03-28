import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

axes[0].plot(x, y, color='blue', linewidth=2)
axes[0].set_title("Sine Wave")
axes[0].set_xlabel("X values")
axes[0].set_ylabel("sin(X)")
axes[0].grid(True)

cities = ["Denver", "Kathmandu", "La Paz", "Mexico City", "Zurich"]
heights = [1609, 1400, 3640, 2250, 408]

axes[1].bar(cities, heights, color='green')
axes[1].set_title("Heights of Cities")
axes[1].set_xlabel("Cities")
axes[1].set_ylabel("Height (m)")

plt.tight_layout()
plt.show()