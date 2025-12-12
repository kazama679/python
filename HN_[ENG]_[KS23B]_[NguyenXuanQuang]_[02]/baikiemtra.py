import json
import csv
import os
import matplotlib.pyplot as plt

DATA_FILE = "data.json"

# 1. Tải dữ liệu


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# 2. Lưu dữ liệu


def save_data(products):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

# Tính trạng thái sản phẩm


def tinh_trang_thai(so_luong):
    if so_luong <= 5:
        return "Cần nhập"
    elif so_luong > 50:
        return "Khó bán"
    else:
        return "Bình thường"

# 3. Hiển thị danh sách


def show_products(products):
    if not products:
        print("Kho đang trống!")
        return
    print("\n===== DANH SÁCH SẢN PHẨM =====")
    print("{:<10} {:<25} {:<12} {:<10} {:<15} {:<12}".format(
        "Mã SP", "Tên SP", "Giá bán", "SL", "Giá trị tồn", "Trạng thái"))
    for sp in products:
        print("{:<10} {:<25} {:<12} {:<10} {:<15} {:<12}".format(
            sp["masp"], sp["ten_sp"], sp["gia_ban"], sp["so_luong"],
            sp["gia_tri_ton"], sp["trang_thai"]
        ))

# 4. Thêm sản phẩm mới


def add_product(products):
    masp = input("Nhập mã sản phẩm: ").upper()
    for sp in products:
        if sp["masp"] == masp:
            print("Mã sản phẩm đã tồn tại!")
            return
    ten_sp = input("Nhập tên sản phẩm: ")
    try:
        gia_ban = int(input("Nhập giá bán: "))
        so_luong = int(input("Nhập số lượng: "))
    except:
        print("Giá bán và số lượng phải là số!")
        return
    if gia_ban <= 0 or so_luong <= 0:
        print("Giá bán và số lượng phải > 0!")
        return

    gia_tri_ton = gia_ban * so_luong
    trang_thai = tinh_trang_thai(so_luong)

    products.append({
        "masp": masp,
        "ten_sp": ten_sp,
        "gia_ban": gia_ban,
        "so_luong": so_luong,
        "gia_tri_ton": gia_tri_ton,
        "trang_thai": trang_thai
    })
    print("✔ Thêm sản phẩm thành công!")

# 5. Cập nhật sản phẩm


def update_product(products):
    masp = input("Nhập mã sản phẩm cần cập nhật: ").upper()
    for sp in products:
        if sp["masp"] == masp:
            print("Tìm thấy sản phẩm:", sp["ten_sp"])
            try:
                sp["gia_ban"] = int(input("Nhập giá bán mới: "))
                sp["so_luong"] = int(input("Nhập số lượng mới: "))
            except:
                print("Giá bán và số lượng phải là số!")
                return
            sp["gia_tri_ton"] = sp["gia_ban"] * sp["so_luong"]
            sp["trang_thai"] = tinh_trang_thai(sp["so_luong"])
            print("✔ Cập nhật thành công!")
            return
    print("Không tìm thấy mã sản phẩm!")

# 6. Xóa sản phẩm


def delete_product(products):
    masp = input("Nhập mã sản phẩm cần xóa: ").upper()

    for sp in products:
        if sp["masp"] == masp:
            confirm = input("Bạn có chắc muốn xóa? (y/n): ").lower()
            if confirm == 'y':
                products.remove(sp)
                print("Đã xóa!")
            else:
                print("Đã hủy thao tác.")
            return
    print("Không tìm thấy sản phẩm!")

# 7. Tìm kiếm sản phẩm


def search_product(products):
    keyword = input("Nhập tên hoặc mã SP cần tìm: ").lower()
    results = [
        sp for sp in products
        if keyword in sp["masp"].lower() or keyword in sp["ten_sp"].lower()
    ]
    if results:
        show_products(results)
    else:
        print("Không tìm thấy sản phẩm nào!")

# 8. Sắp xếp sản phẩm


def sort_products(products):
    print("1. Giá bán tăng dần")
    print("2. Giá trị tồn giảm dần")
    choice = input("Chọn kiểu sắp xếp: ")

    if choice == "1":
        products.sort(key=lambda x: x["gia_ban"])
        print("✔ Đã sắp xếp theo giá bán tăng dần")
    elif choice == "2":
        products.sort(key=lambda x: x["gia_tri_ton"], reverse=True)
        print("✔ Đã sắp xếp theo giá trị tồn giảm dần")
    else:
        print("Lựa chọn không hợp lệ!")

# 9. Thống kê kho hàng


def thong_ke(products):
    stats = {"Cần nhập": 0, "Bình thường": 0, "Khó bán": 0}

    for sp in products:
        stats[sp["trang_thai"]] += 1

    print("\n===== THỐNG KÊ =====")
    for k, v in stats.items():
        print(f"{k}: {v}")

    return stats

# 10. Vẽ biểu đồ


def ve_bieu_do(stats):
    labels = stats.keys()
    values = stats.values()

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Biểu đồ trạng thái kho hàng")
    plt.show()

# MENU CHÍNH


def main():
    products = load_data()

    while True:
        print("\n========== MENU ==========")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm mới sản phẩm")
        print("3. Cập nhật thông tin sản phẩm")
        print("4. Xoá sản phẩm")
        print("5. Tìm kiếm sản phẩm")
        print("6. Sắp xếp danh sách sản phẩm")
        print("7. Thống kê kho hàng")
        print("8. Vẽ biểu đồ thống kê")
        print("9. Lưu vào file")
        print("0. Thoát")
        print("==========================")
        choice = input("Chọn chức năng: ")
        if choice == "1":
            print("Hien thi du lieu san pham")
            print("Va luu vao file data.json")
            show_products(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            update_product(products)
        elif choice == "4":
            delete_product(products)
        elif choice == "5":
            search_product(products)
        elif choice == "6":
            sort_products(products)
        elif choice == "7":
            thong_ke(products)
        elif choice == "8":
            stats = thong_ke(products)
            ve_bieu_do(stats)
        elif choice == "9":
            save_data(products)
            print("✔ Đã lưu dữ liệu vào file!")
        elif choice == "0":
            save_data(products)
            print("✔ Đã lưu và thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


# if __name__ == "__main__":
#     main()

main()
