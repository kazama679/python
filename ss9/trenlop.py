import matplotlib.pyplot as plt

# chuẩn bị về mặt dữ liệu
months = [1, 2, 3, 4, 5, 6]
sales = [2500, 3000, 2800, 3500, 4000, 4200]

# khai báo figures và axes
fig, ax = plt.subplots()

# khai báo dạng lướt
plt.grid()

ax.plot(months, sales, color='blue', marker='o', linestyle='dashed')

plt.scatter(months, sales, color='red')

# đặt nhãn, tiêu đề cho biểu đồ
ax.set_title('Biểu đồ doanh thu quý 2 năm 2025')
ax.set_xlabel('Thời gian')
ax.set_ylabel('Doanh thu')

# xuất sơ đồ
plt.savefig('doanhthu_quy2_2025.png', pdi=300, transparent=True)

# hiển thị được biểu đồ
plt.show()
