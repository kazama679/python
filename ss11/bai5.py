import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
x = np.linspace(0, 10, 100)
y_line1 = x
y_line2 = x**2

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(x, y_line1, color='C0')
axes[0, 0].set_title("Line: y = x")
axes[0, 0].grid(True, linestyle='--', alpha=0.6)

axes[1, 0].plot(x, y_line2, color='C1')
axes[1, 0].set_title("Line: y = x²")
axes[1, 0].grid(True, linestyle='--', alpha=0.6)

x1 = np.random.uniform(0, 10, 100)
y1 = np.random.uniform(0, 10, 100)
axes[0, 1].scatter(x1, y1, color='C2', alpha=0.7)
axes[0, 1].set_title("Scatter 1")
axes[0, 1].grid(True, linestyle='--', alpha=0.5)

x2 = np.random.uniform(0, 10, 100)
y2 = np.random.uniform(0, 10, 100)
axes[1, 1].scatter(x2, y2, color='C3', alpha=0.7)
axes[1, 1].set_title("Scatter 2")
axes[1, 1].grid(True, linestyle='--', alpha=0.5)

for ax in axes.flat:
    ax.set_xlabel("x")
    ax.set_ylabel("y")

plt.tight_layout()
plt.show()
