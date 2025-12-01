import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_theme(style="whitegrid")

dataSource = np.random.normal(loc=50, scale=15, size=500)

plt.figure(figsize=(10, 6))

sns.histplot(
    dataSource,
    bins=30,
    color="red"
)

plt.title("Biểu đồ phân phối dữ liệu mẫu", fontsize=16)
plt.xlabel("Giá trị", fontsize=14)
plt.ylabel("Tần số", fontsize=14)

plt.show()
