import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0, 10, 200)
y = x**2 + 2*x

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color='C0', linewidth=2)
ax.set_title("Biểu đồ đầu tay của Học viên")
ax.set_xlabel("Trục x")
ax.set_ylabel("Trục y")
ax.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
