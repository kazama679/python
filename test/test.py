import csv
import os
import matplotlib.pyplot as plt

# ============================
# CẤU HÌNH FILE
# ============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.csv")

# ============================
# LOAD DATA
# ============================


def load_data():
    products = []
    try:
        with open(DATA_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["gia_ban"] = int(row["gia_ban"])
                row["so_luong"] = int(row["so_luong"])
                row["gia_tri_ton"] = int(row["gia_tri_ton"])
                products.append(row)
    except FileNotFoundError:
        print("Chưa có file data.csv, hệ thống sẽ tự tạo khi lưu!")
    return products

# ============================
# SAVE DATA
# ============================


def save_data(products):
    with open(DATA_FILE, mode='w', encoding='utf-8', newline='') as f:
        fieldnames = ["masp", "ten_sp", "gia_ban",
                      "so_luong", "gia_tri_ton", "trang_thai"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

# ============================
# TÍNH TRẠNG THÁI
# ============================


def tinh_trang_thai(so_luong):
    if so_luong <= 5:
        return "Cần nhập"
    elif so_luong > 50:
        return "Khó bán"
    else:
        return "Bình thường"

# ============================
# HIỂN THỊ
# ============================


def show_products(products):
    if not products:
        print("Kho đang trống!")
        return
    print("\n===== DANH SÁCH SẢN PHẨM =====")
    print("{:<10} {:<25} {:<12} {:<10} {:<15} {:<12}".format(
        "Mã", "Tên sản phẩm", "Giá", "Số lượng", "Tồn kho", "Trạng thái"))
    for sp in products:
        print("{:<10} {:<25} {:<12} {:<10} {:<15} {:<12}".format(
            sp["masp"], sp["ten_sp"], sp["gia_ban"],
            sp["so_luong"], sp["gia_tri_ton"], sp["trang_thai"]
        ))

# ============================
# THÊM
# ============================


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
    print("Thêm sản phẩm thành công!")

# ============================
# CẬP NHẬT
# ============================


def update_product(products):
    masp = input("Nhập mã sản phẩm cần cập nhật: ").upper()
    for sp in products:
        if sp["masp"] == masp:
            try:
                sp["gia_ban"] = int(input("Nhập giá bán mới: "))
                sp["so_luong"] = int(input("Nhập số lượng mới: "))
            except:
                print("Phải nhập số!")
                return

            sp["gia_tri_ton"] = sp["gia_ban"] * sp["so_luong"]
            sp["trang_thai"] = tinh_trang_thai(sp["so_luong"])
            print("Cập nhật thành công!")
            return
    print("Không tìm thấy sản phẩm!")

# ============================
# XÓA
# ============================


def delete_product(products):
    masp = input("Nhập mã sản phẩm cần xóa: ").upper()
    for sp in products:
        if sp["masp"] == masp:
            products.remove(sp)
            print("Đã xóa!")
            return
    print("Không tìm thấy!")

# ============================
# TÌM KIẾM
# ============================


def search_product(products):
    keyword = input("Nhập tên hoặc mã: ").lower()
    results = [sp for sp in products if keyword in sp["masp"].lower()
               or keyword in sp["ten_sp"].lower()]
    if results:
        show_products(results)
    else:
        print("Không tìm thấy!")

# ============================
# SẮP XẾP
# ============================


def sort_products(products):
    print("1. Giá tăng dần")
    print("2. Giá trị tồn giảm dần")
    chon = input("Chọn: ")
    if chon == "1":
        products.sort(key=lambda x: x["gia_ban"])
    elif chon == "2":
        products.sort(key=lambda x: x["gia_tri_ton"], reverse=True)
    print("Đã sắp xếp!")

# ============================
# THỐNG KÊ
# ============================


def thong_ke(products):
    stats = {"Cần nhập": 0, "Bình thường": 0, "Khó bán": 0}
    for sp in products:
        stats[sp["trang_thai"]] += 1
    print(stats)
    return stats

# ============================
# VẼ BIỂU ĐỒ
# ============================


def ve_bieu_do(stats):
    plt.pie(stats.values(), labels=stats.keys(), autopct='%1.1f%%')
    plt.title("Biểu đồ kho hàng")
    plt.show()

# ============================
# MENU CHÍNH
# ============================


def main():
    products = load_data()
    while True:
        print("\n========== MENU ==========")
        print("1. Hiển thị")
        print("2. Thêm")
        print("3. Cập nhật")
        print("4. Xóa")
        print("5. Tìm kiếm")
        print("6. Sắp xếp")
        print("7. Thống kê")
        print("8. Vẽ biểu đồ")
        print("9. Lưu")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
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
            ve_bieu_do(thong_ke(products))
        elif choice == "9":
            save_data(products)
            print("Đã lưu!")
        elif choice == "0":
            save_data(products)
            print("Đã lưu và thoát!")
            break
        else:
            print("Sai lựa chọn!")


# ============================
# CHẠY CHƯƠNG TRÌNH
# ============================
main()
