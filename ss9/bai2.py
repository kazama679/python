import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y = x**3
plt.figure()
plt.plot(x, y, color='red', linewidth=3)
plt.title("Đồ thị hàm bậc ba y = x³")
plt.xlabel("Giá trị x")
plt.ylabel("Giá trị y")
plt.grid(linestyle='--', alpha=0.6)
