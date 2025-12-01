import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
np.random.seed(0)

data = np.random.normal(7, 1.5, 200)

plt.figure(figsize=(8, 5))
sns.histplot(data, bins=20, kde=True, color='C0')
plt.title("Bài 1: Histogram + KDE điểm thi")
plt.xlabel("Điểm")
plt.ylabel("Mật độ")
plt.tight_layout()
plt.show()

print("Nhận xét: Phần lớn điểm tập trung khoảng 6–8.")