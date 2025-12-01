import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(3)
sns.set_theme(style="whitegrid")

classes = ["A"]*50 + ["B"]*50 + ["C"]*50
scores = np.concatenate([
    np.clip(np.random.normal(7.2, 0.9, 50), 0, 10),
    np.clip(np.random.normal(6.7, 1.1, 50), 0, 10),
    np.clip(np.random.normal(7.8, 0.8, 50), 0, 10)
])
df = pd.DataFrame({"class": classes, "score": scores})

plt.figure(figsize=(6, 5))
sns.barplot(data=df, x="class", y="score", ci='sd', palette="pastel")
plt.title("Bài 4: Điểm trung bình theo lớp")
plt.ylabel("Điểm trung bình")
plt.tight_layout()
plt.show()

means = df.groupby("class")["score"].mean()
print("Trung bình theo lớp:\n", means)
print("Nhận xét: lớp có giá trị trung bình cao nhất/ thấp nhất thấy rõ trên bảng trên.")
