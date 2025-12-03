import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 300)
y1 = x
y2 = x**2
y3 = x**3

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y1, label='y = x', color='C0')
ax.plot(x, y2, label='y = x²', color='C1')
ax.plot(x, y3, label='y = x³', color='C2')
ax.set_title("Bài 4: y, y², y³")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
