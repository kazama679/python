import matplotlib.pyplot as plt
import numpy as np

#  lấy ra các tháng từ 1 đến 12
months = np.arange(1, 13)

# lượng mưa trong năm
rainfall = [10, 15, 30, 120, 200, 250, 280, 220, 150, 80, 30, 15]

# nhiệt độ trong năm
temperature = [20, 22, 25, 28, 30, 32, 31, 30, 28, 26, 23, 21]

# tạo figure và axes
fig, ax = plt.subplots(figsize=(10, 6))

# vẽ biểu đồ thể hiện nhiệt độ
ax.plot(months, temperature, color='red', marker='o', label='Nhiệt độ (°C)')

ax.scatter(months, temperature, color='blue')

plt.grid()
plt.show()
