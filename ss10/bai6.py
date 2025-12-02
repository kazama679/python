import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(5)
sns.set_theme(style="whitegrid")

majors = ["CNTT"]*80 + ["Kinh Tế"]*80 + ["Ngôn Ngữ"]*80
scores = np.concatenate([
    np.clip(np.random.normal(7.5, 0.8, 80), 0, 10),
    np.clip(np.random.normal(7.0, 1.2, 80), 0, 10),
    np.clip(np.random.normal(6.8, 1.5, 80), 0, 10)
])
df = pd.DataFrame({"major": majors, "score": scores})

plt.figure(figsize=(6, 5))
sns.boxplot(data=df, x="major", y="score", palette="Set2")
plt.title("Bài 6: Boxplot theo ngành")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 5))
sns.violinplot(data=df, x="major", y="score", palette="Set2", inner="quartile")
plt.title("Bài 6: Violinplot theo ngành")
plt.tight_layout()
plt.show()

grouped = df.groupby("major")["score"].agg(["median", "mean", "std"])
print("Thống kê theo ngành:\n", grouped)
print("Nhận xét ngắn: kiểm tra median và IQR/độ lệch chuẩn để biết ngành phân tán hay tập trung hơn.")


x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color='C0')
ax.set_title("Bài 6: y = sin(x)")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.grid(linestyle='--', alpha=0.6)

xp = np.pi/2
yp = np.sin(xp)
ax.annotate("Cực đại (x=π/2)", xy=(xp, yp), xytext=(xp+0.8, yp-0.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.8))

plt.tight_layout()
plt.show()
