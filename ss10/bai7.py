import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(4)
mat = np.random.rand(10, 10)

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(mat, annot=True, fmt=".2f", cmap='viridis', ax=ax)
ax.set_title("Bài 7: Heatmap ma trận 10x10")
ax.set_xlabel("Cột")
ax.set_ylabel("Hàng")
plt.tight_layout()
plt.show()

np.random.seed(6)
sns.set_theme(style="whitegrid")

n = 500
majors = np.random.choice(["A", "B", "C"], size=n)
hours = np.random.uniform(1, 10, size=n)
noise = np.random.normal(0, 1.1, size=n)
score = np.clip(hours * 1.1 + noise + (majors == "A")*0.2, 0, 10)
df = pd.DataFrame({"hours": hours, "score": score, "major": majors})

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
sns.histplot(df["score"], bins=25, kde=True, ax=axes[0], color="C0")
axes[0].set_title("Phân phối điểm")
sns.scatterplot(data=df, x="hours", y="score",
                hue="major", alpha=0.6, ax=axes[1])
axes[1].set_title("Hours vs Score")
sns.boxplot(data=df, x="major", y="score", palette="pastel", ax=axes[2])
axes[2].set_title("So sánh theo major")
plt.tight_layout()
plt.show()

print("Kết luận ví dụ:")
print("1) Phân phối: khoảng trung tâm và spread nhìn thấy trên histogram.")
print("2) Quan hệ: có tương quan dương nhẹ giữa hours và score.")
print("3) Nhóm: boxplot cho thấy sự khác biệt về trung vị và độ phân tán giữa các major.")
