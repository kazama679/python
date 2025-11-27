import numpy as np
import matplotlib.pyplot as plt
products = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Tất"]
sales = [150, 120, 200, 90, 65, 80]
x_pos = np.arange(len(products))
plt.figure()
bars = plt.bar(x_pos, sales, color='green', edgecolor='black')
plt.xticks(x_pos, products)
plt.title("Doanh số bán hàng tháng 10/2025")
plt.ylabel("Doanh số (triệu)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
# In giá trị doanh số lên đầu mỗi cột (chữ trắng, đậm)
for bar, val in zip(bars, sales):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height - 5, str(val),
             ha='center', va='bottom', color='white', fontweight='bold')

plt.tight_layout()
plt.show()
