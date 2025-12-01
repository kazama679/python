import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(1)
sns.set_theme(style="whitegrid")

subjects = np.random.choice(["Toán", "Lý", "Hóa"], size=180)
scores = np.clip(np.random.normal(7, 1.2, size=180) +
                 (subjects == "Toán")*0.3, 0, 10)
df = pd.DataFrame({"subject": subjects, "score": scores})

g = sns.displot(data=df, x="score", hue="subject",
                kind="kde", height=4, aspect=1.6)
g.fig.suptitle("Bài 2: KDE phân phối theo môn", y=1.03)
plt.show()

means = df.groupby("subject")["score"].mean()
print("Trung bình theo môn:\n", means)
print("Nhận xét: môn có đường KDE dịch sang phải có điểm cao hơn.")
