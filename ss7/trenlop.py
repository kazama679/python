import pandas as pd

# Thao tác khởi tạo từ list
myList = [10, 20, 30, 40, 50]
serires = pd.Series(myList)

print(f"{serires}")

# Tạo series với chỉ số tùy chính
seriresCusomeIndex = pd.Series(myList, index=['a', 'b', 'c', 'd', 'e1'])
print(f"{seriresCusomeIndex}")

# khởi tạo series từ dictionary
seriesDictionary = pd.Series({'a': 100, 'b': 200, 'c': 300})
print(f"{seriesDictionary}")

# các thao tác
# 1.thao tác lấy dữ liệu
print(f"Lấy dữ liệu theo chỉ số: {seriesDictionary[1]}")

# thêm phần tử
seriesDictionary['d'] = 400
print(f"Thêm phần tử: {seriesDictionary}")

#  cập nhập
seriesDictionary['c'] = 444
print(f"cậpn nhập phần tử: {seriesDictionary}")

# xóa phần tử
del seriesDictionary['b']
print(f"xóa phần tử: {seriesDictionary}")
