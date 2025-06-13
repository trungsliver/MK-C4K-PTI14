import oop

# Khởi tạo data
dtb = oop.UserDatabase()

# Test data dạng dictionary (file json)
print(len(dtb.users_dict))

# Test data dạng object
dtb.load_data()
print(len(dtb.users_list))

# Hiển thị dữ liệu
dtb.show_all()