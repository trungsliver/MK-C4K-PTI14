# DICTIONARY & MAP
# Bài 1: Cho 1 danh sách gồm tên của học sinh (viết hoa lộn xộn)
# Yêu cầu: Dùng map() để chuyển đổi danh sách trên viết hoa tất cả chữ
# Ví dụ: tRunG -> TRUNG
pti14 = ['xUan tU', 'qUang Huy', 'DUc MiNh', 'MinH NhAt', 'hOANg BacH']
    # cách 1
def convert_name(name):
    return name.upper()
pti14_1 = map(convert_name, pti14)
print(list(pti14_1))
    # cách 2
pti14_2 = map(lambda name: name.upper(), pti14)
print(list(pti14_2))

# Bài 2: Quản lý thông tin sinh viên
# #Yêu cầu: Tạo một dictionary lưu trữ thông tin sinh viên với các khóa: name, age, và grade. 
# Thực hiện các thao tác sau:
# 1. Thêm sinh viên với thông tin name = "John", age = 22, và grade = "A".
student = {
    "name": "John",
    "age": 22,
    "grade": "A"
}
# 2. Cập nhật grade của sinh viên thành "A+".
student["grade"] = "A+"
# 3. Xóa thông tin age của sinh viên.
del student["age"]
# 4. Kiểm tra xem name có trong dictionary không.
print("name" in student)

# Bài 3: Đếm Số Lần Xuất Hiện Của Từ Trong Chuỗi
# Yêu cầu: Viết chương trình nhận vào một chuỗi và trả về một dictionary đếm số lần xuất hiện của mỗi từ trong chuỗi.
sentence = 'this is a test this is only a test'

def count_words(sentence):
    # strip(): xóa khoảng trắng ở đầu và cuối
    # split(): tách chuỗi thành danh sách
    words = sentence.strip().split()
    # Khai báo dictionary để lưu dữ liệu
    word_count = {}
    # Duyệt qua danh sách từ
    for word in words:          
        if word in word_count:  # word đã có trong dictionary
            word_count[word] += 1
        else:                   # word chưa có trong dictionary
            word_count[word] = 1
    return word_count
print(count_words(sentence))

# Bài 4: Gộp Hai Dictionary
# Yêu cầu: Cho hai dictionary A và B. Viết chương trình gộp chúng lại. Nếu một key xuất hiện ở cả hai dictionary, cộng giá trị của chúng lại.
A = {'a': 100, 'b': 200, 'c': 300}
B = {'b': 250, 'c': 150, 'd': 400}

def merge1(dict1, dict2):
    # Tạo bản sao của dict1 để không bị thay đổi dữ liệu
    merge_dict = dict1.copy()
    # Duyệt dict2
    for key, value in dict2.items():
        if key in merge_dict:
            merge_dict[key] += value
        else:
            merge_dict[key] = value
    return merge_dict
print(merge1(A, B))

# Bài 5: Tìm Key Có Giá Trị Lớn Nhất
# Yêu cầu: Cho một dictionary có các cặp {key: value}. Viết chương trình để tìm key có giá trị lớn nhất.
    

# Bài 6: Sắp Xếp Dictionary Theo Giá Trị
# Yêu cầu: Viết chương trình để sắp xếp một dictionary theo giá trị từ cao đến thấp.

# Bài 7: Nhóm Các Phần Tử Theo Giá Trị
# Yêu cầu: Viết chương trình để nhóm các phần tử của một dictionary dựa trên giá trị của chúng. Ví dụ, các phần tử có cùng giá trị sẽ được đưa vào một danh sách.

# Bài 8: Tạo Dictionary Từ Danh Sách
# Yêu cầu: Viết chương trình tạo một dictionary từ hai danh sách: một danh sách chứa key và một danh sách chứa value tương ứng.