# CRUD: Create - Read - Update - Delete

# Create
dict1 = {}
dict2 = {
    # Các cặp key - value
    'name': 'Quang Huy',
    'age': 14,
    'gender': 'male'
}

# Read - Duyệt, hiện phần tử
    # Duyệt toàn bộ key-value
for key, value in dict2.items():
    print(f"{key}: {value}")
    # Truy cập bằng key
print('Tên:', dict2['name'])
    # Sử dụng phương thức get()
print('Tên:', dict2.get('name'))
        # Nếu không tồn tại key => None / Giá trị mặc định
print('Money:', dict2.get('money'))
print('Girlfriend:', dict2.get('gf', '404 not found'))

# Update - chỉnh sửa
    # Thêm cặp key - value
dict2['laptop'] = 'MSI'
    # Chỉnh sửa value
dict2['name'] = 'Huy Quần Hoa'
print(dict2)

# Delete - Xóa 
    # Xóa theo key - del
del dict2['laptop']
    # Xóa theo key, trả về value - pop()
# dict2.pop('gender')
print(dict2.pop('gender'))

# Kiểm tra key tồn tại
print('name' in dict2)          # True
print('girlfriend' in dict2)    # False

# Lấy tất cả cặp key - value: items()
print(dict2.items())
# Lấy tất cả key: keys()
print(dict2.keys())
# Lấy tất cả value: values()
print(dict2.values())

# Hàm map(function, itertable)
    # function: hàm biến đổi dữ liệu
    # itertable: bảng dữ liệu

# Ví dụ: Cho danh sách tên học sinh
# Yêu cầu: dùng map() để thêm tên lớp vào sau tên hs
arr = ['Tú', 'Huy', 'Lâm', 'Bách', 'Minh', 'Bảo', 'Nhật']
    # Cách 1: Dùng hàm xác định
def convert_name(student, class_name = 'PTI14'):
    return f"{student} {class_name}"
arr1 = map(convert_name, arr)
print(list(arr1))

    # Cách 2: Dùng lambda - hàm ẩn danh / không xác định
arr2 = map(lambda name: str(name) + ' PTI14', arr )
print(list(arr2))

        # Giải thích cách 2
arr3 = []
for name in arr:
    new_name = str(name) + ' PTI14'
    arr3.append(new_name)
print(arr3)

# Bài tập: Cho 1 danh sách điểm hệ số 10 (thang điểm 10)
# Yêu cầu: dùng map() để chuyển đổi toàn bộ phần tử danh sách sang điểm hệ số 4 (thang 4)
gpa_10 = [5, 7, 8, 10, 9]
    # Cách 1: Dùng hàm xác định
def convert_gpa(score):
    return round((score / 10) * 4, 2)
gpa_4 = list(map(convert_gpa, gpa_10))
print(gpa_4)

    # Cách 2: Dùng hàm không xác định
gpa_4_2 = map(lambda gpa: round((gpa / 10) * 4, 2), gpa_10)
print(list(gpa_4_2))
