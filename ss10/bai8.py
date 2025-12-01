import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(7)
sns.set_theme(style="whitegrid")

months = np.tile(np.arange(1, 13), 3)
categories = np.repeat(["Shoes", "Clothes", "Bags"], 12)
revenue = []
for cat in ["Shoes", "Clothes", "Bags"]:
    base = 300 if cat == "Shoes" else (220 if cat == "Clothes" else 150)
    trend = np.linspace(0, 60, 12)
    rev = base + trend + np.random.normal(0, 30, 12)
    revenue += list(np.clip(rev, 0, None))

df = pd.DataFrame(
    {"month": months, "category": categories, "revenue": revenue})

plt.figure(figsize=(8, 4))
sns.lineplot(data=df, x="month", y="revenue", hue="category", marker="o")
plt.title("Doanh thu theo tháng và nhóm")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.violinplot(data=df, x="category", y="revenue",
               inner="quartile", palette="Set3")
plt.title("Phân phối doanh thu theo nhóm")
plt.tight_layout()
plt.show()

monthly = df.groupby("month")["revenue"].sum().reset_index()
plt.figure(figsize=(6, 4))
sns.regplot(data=monthly, x="month", y="revenue",
            ci=None, scatter_kws={'s': 40})
plt.title("Tổng doanh thu theo tháng (regression)")
plt.tight_layout()
plt.show()

print("Phân tích ngắn (ví dụ): nhóm Shoes có doanh thu cao nhất; Bags biến động nhất; xu hướng tổng thể có hơi tăng do trend nhẹ.")
