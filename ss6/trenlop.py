import numpy as np

array = [10, 20, 30, 40, 50, 60]

print(f"array ban đầu: {array}")
print(f"Lấy ra phần tử vị trí cuối: {array[-1]}")
print(f"Lấy ra các phần tử vị trí 2: {array[-3:-1]}")
print(f"Lấy ra các phần tử vị trí 3: {array[::2]}")

np_array = np.array(array)
print(f"Lấy ra tất cả phần tử lớn hơn 30: {np_array > 30}")
print(f"Lấy ra tất cả phần tử lớn hơn 30: {np_array[np_array > 30]}")

firstNumber = 10
result = np_array*firstNumber
print(f"{result}")

print(f"{np_array+10}")
print(f"{np.sum(np_array)}")

