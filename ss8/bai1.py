# Tạo list gồm 10 số bất kỳ
lst = [1, 2, 3, 2, 5, 1, 7, 9, 9, 4]

print("List ban đầu:", lst)

# Lấy các phần tử ở vị trí chẵn (index 0,2,4,6,8)
even_index_elements = lst[0::2]
print("Các vị trí chẵn:", even_index_elements)

# Chuyển list thành tuple
tpl = tuple(lst)
print("Tuple:", tpl)

# Tạo dict theo dạng {vị trí: giá trị}
dict_comp = {i: v for i, v in enumerate(lst)}
print("Dict:", dict_comp)

# Tạo set từ list và tính số phần tử bị loại trùng
set_data = set(lst)
removed_count = len(lst) - len(set_data)

print("Set:", set_data)
print("Số phần tử bị loại trùng:", removed_count)
