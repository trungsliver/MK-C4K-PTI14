import data_io

class Player:
    def __init__(self, id, name, dob, region, club, rating=None, worth=None):
        self.id = id
        self.name = name
        self.dob = dob
        self.region = region
        self.club = club
        # Nếu có thì định dạng float, không có thì mặc định = 0
        self.rating = float(rating) if rating else 0
        self.worth = float(worth) if worth else 0

    def update(self, new_data:dict):
        for key, value in new_data.items():
            # Chỉ khi nào có thuộc tính thì mới update
            if value:
                setattr(self, key, value)

    def show_info(self):
        print(f"""====================
ID: {self.id}
Name: {self.name}
DOB: {self.dob}
Region: {self.region}
Club: {self.club}
Rating: {self.rating}
Worth: {self.worth}
====================""")
        
class PlayerDatabase:
    def __init__(self):
        # Tạo danh sách chứa các player - dạng object
        self.players_list = list()
        # Đọc dữ liệu khi khởi tạo - dạng dict
        self.players_dict = data_io.load_json_data()

    # Chuyển đổi từ json / dictionary => object
    def convert_to_object(self):
        new_players = []
        for player_data in self.players_dict:
            player = Player(id = player_data["id"],
                            name = player_data['name'],
                            dob = player_data['dob'],
                            region = player_data['region'],
                            club = player_data['club'],
                            rating = player_data['rating'],
                            worth = player_data['worth'])
            new_players.append(player)
        self.players_list = new_players

    # Chuyển từ object => dictionary / json
    def convert_to_dict(self):
        json_data = list()
        for player in self.players_list:
            json_data.append(player.__dict__)
        return json_data

    # Hiển thị tất cả
    def show_all(self):
        for player in self.players_list:
            player.show_info()
