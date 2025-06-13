class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def show_info(self):
        print(f"{self.username} - {self.email} - {self.password}")

import data_io

class UserDatabase:
    def __init__(self):
        # Danh sách dạng object
        self.users_list = list()
        # Danh sách dạng dictionary
        self.users_dict = data_io.load_json_data()

    # Chuyển đổi dữ liệu từ json sang object
    def load_data(self):
        new_users = []
        for user_data in self.users_dict:
            user = User(username = user_data["username"],
                        email = user_data["email"],
                        password = user_data["password"])
            new_users.append(user)
        self.users_list = new_users

    # Chuyển đổi từ object sang json
    def items_to_data(self):
        json_data = list()
        for user in self.users_list:
            json_data.append(user.__dict__)
        return json_data
    
    # Hàm hiển thị tất cả
    def show_all(self):
        for user in self.users_list:
            user.show_info()