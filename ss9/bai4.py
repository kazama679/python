import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 200)
plt.figure()
plt.plot(x, np.sin(x), color='green', linestyle='-', label='sin(x)')
plt.plot(x, np.cos(x), color='red', linestyle='--', label='cos(x)')
plt.title("So sánh sin(x) và cos(x)")
plt.xlabel("x")
plt.ylabel("Giá trị")
plt.legend()
plt.grid(linestyle='--', alpha=0.6)
