import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 20)
y = 2 * x + 3
plt.figure()
plt.plot(x, y, color='green', linewidth=3)
plt.title("Đường thẳng y = 2x + 3")
plt.xlabel("Giá trị x")
plt.ylabel("Giá trị y")
plt.grid(linestyle='--', alpha=0.6)
