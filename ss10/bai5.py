import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(4)
sns.set_theme(style="whitegrid")

classes = np.random.choice(["A", "B", "C"], size=90)
scores = np.clip(np.random.normal(7.0, 1.2, 90) + (classes == "C")*0.4, 0, 10)
df = pd.DataFrame({"class": classes, "score": scores})

plt.figure(figsize=(6, 5))
sns.barplot(data=df, x="class", y="score",
            estimator=np.mean, ci=95, palette="muted")
plt.title("Bài 5: So sánh điểm trung bình theo lớp")
plt.tight_layout()
plt.show()

print("Trung bình theo lớp:\n", df.groupby("class")["score"].mean())
print("Nhận xét: so sánh cột để xác định lớp có điểm cao/ thấp.")
