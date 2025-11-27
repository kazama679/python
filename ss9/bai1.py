import matplotlib.pyplot as plt
import numpy as np

# tạo bảng từ 0-10
x = np.linspace(0, 10, 50)
y = x**2

# khai báo figure và axes
fig, ax = plt.subplots(figsize=(8, 4))

ax.set_title('Biểu đồ hàm số y = x^2')
ax.set_xlabel('Trục x', fontsize=14)
ax.set_ylabel('Trục y', fontsize=14)
ax.plot(x, y)
# mở biểu đồ
plt.show()
