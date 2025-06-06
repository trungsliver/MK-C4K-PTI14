# Lập trình hướng đối tượng
# OOP - Object oriented programming

# Tổng quát: OOP là cách mà ta mô phỏng thế giới thực vào chương trình máy tính

# Class (lớp):          Đối tượng tổng quát
# Object (đối tượng):   Đối tượng cụ thể

# Attribute (thuộc tính):   đặc điểm của đối tượng
# Method (phương thức):     hành động của đối tượng

# Khai báo class (đối tượng tổng quát)
class Human:
    # Hàm khởi tạo 
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (attributes)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức - hành động (Method)
    #  Phương thức giới thiệu bản thân
    def introduce(self):
        print(f"Xin chào, tôi là {self.name}, {self.age} tuổi")

    # Phương thức hát
    def sing(self, song):
        print(f"{self.name} đang hát {song}")

    # Phương thức tìm năm sinh
    def get_dob(self, year:int):
        return year - int(self.age)

# Khởi tạo object (đối tượng)
h1 = Human('Duc Minh', 13, 'male')
h1.introduce()
h1.sing('Baby Shark')
print('Năm sinh:', h1.get_dob(2025))