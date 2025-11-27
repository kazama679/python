import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 200)
y1 = 2 * x + 1
y2 = -1 * x + 10
plt.figure()
plt.plot(x, y1, color='green', label="Đường 1")
plt.plot(x, y2, color='orange', label="Đường 2")
plt.title("Giao điểm của hai đường thẳng")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(linestyle='--', alpha=0.6)
plt.legend(loc='upper left')
