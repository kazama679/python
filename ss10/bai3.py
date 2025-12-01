import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(2)
sns.set_theme(style="whitegrid")

hours = np.random.randint(1, 11, size=150)
noise = np.random.normal(0, 1.0, size=hours.size)
score = np.clip(hours * 1.2 + noise, 0, 10)
df = pd.DataFrame({"hours": hours, "score": score})

plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="hours", y="score", alpha=0.7)
sns.regplot(data=df, x="hours", y="score", scatter=False, color="red")
plt.title("Bài 3: Scatterplot Hours vs Score")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.tight_layout()
plt.show()

print("Nhận xét: có xu hướng tương quan dương — điểm tăng khi hours tăng.")
