import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(5)
sns.set_theme(style="whitegrid")

majors = ["CNTT"]*80 + ["Kinh Tế"]*80 + ["Ngôn Ngữ"]*80
scores = np.concatenate([
    np.clip(np.random.normal(7.5, 0.8, 80), 0, 10),   # CNTT
    np.clip(np.random.normal(7.0, 1.2, 80), 0, 10),   # Kinh Tế
    np.clip(np.random.normal(6.8, 1.5, 80), 0, 10)    # Ngôn Ngữ
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
