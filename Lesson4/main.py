import oop

# Khởi tạo dữ liệu (database)
dtb = oop.PlayerDatabase()

# Load data vào danh sách object
dtb.convert_to_object()

# Kiểm tra dữ liệu
print("players_dict:", len(dtb.players_dict))
print("players_list:", len(dtb.players_list))
# dtb.show_all()

# Test hàm tìm kiếm theo tên
find1 = dtb.find_player_by_name("Cristiano Ronaldo")
find2 = dtb.find_player_by_name("Duc Trung")

    # Tìm thấy
if find1 != False:
    print(find1.show_info())
else:
    print("Không tìm thấy player nào")

    # Không tìm thấy
if find2 != False:
    print(find2.show_info())
else:
    print("Không tìm thấy player nào")

# Thêm 1 data mới
new_player = {
        "id": 16,
        "name": "Duc Minh",
        "dob": "14/09/2012",
        "region": "Vietnam",
        "club": "Roblox",
        "rating": 1.0,
        "worth": 1
}
dtb.add_player(new_player)

# Sửa thông tin
edit_player = {
        "id": 10,
        "name": "Khai Hung",
        "dob": "16/10/2011",
        "region": "Vietnam",
        "club": "Roblox",
        "rating": 1.0,
        "worth": 2
}
dtb.edit_player('Khai Hung', edit_player)

# Xóa thông tin
dtb.delete_player('Khai Hung')