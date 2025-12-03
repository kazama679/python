import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)
data = np.random.normal(loc=0, scale=1, size=1000)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(data, bins=30, color='C1', edgecolor='k', alpha=0.9)
ax.set_title("Bài 3: Histogram từ phân phối chuẩn (1000 giá trị)")
ax.set_xlabel("Giá trị")
ax.set_ylabel("Tần số")
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
