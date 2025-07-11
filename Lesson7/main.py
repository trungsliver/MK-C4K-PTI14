import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# xử lý
app = QApplication(sys.argv)
arr = ['Bảo Lâm', 'Khải Hoàng', 'Gia Bảo', 'Minh Nhật', 'Xuân Tú', 'Quang Huy']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lesson7.ui', self)
        # Thêm danh sách để hiển thị trên listWidget
        self.listWidget.addItems(arr)
        # Khai báo sự kiện ấn các nút
        self.btn_add.clicked.connect(self.add_item)
        self.btn_edit.clicked.connect(self.edit_item)
        self.btn_delete.clicked.connect(self.delete_item)
        self.btn_search.clicked.connect(self.search_item)

    def add_item(self):
        # lấy text ở LineEdit
        text = self.lineEdit.text().strip()
        # Thêm phần tử vào danh sách
        arr.append(str(text))
        # Xóa hết các phần tử cũ trên widget
        self.listWidget.clear()
        # Thêm lại danh sách
        self.listWidget.addItems(arr)
        # Xóa dữ liệu ở lineEdit
        self.lineEdit.setText('')
        
    def edit_item(self):
        # Lấy index dòng đang chọn trên listWidget
        cur = self.listWidget.currentRow()
        # Lấy text ở LineEdit
        text = self.lineEdit.text().strip()
        # Thay thế phần tử tại vị trí index
        if cur >= 0 and text != '':
            arr[cur] = str(text)
            msg_box("Sửa thành công", f'Đã sửa thành {text}')
        else:
            msg_box("Lỗi", "Bạn chưa chọn phần tử hoặc chưa ghi nội dung")
        # Xóa hết các phần tử trên widget
        self.listWidget.clear()
        # Thêm lại danh sách
        self.listWidget.addItems(arr)
        # Xóa dữ liệu ở lineEdit
        self.lineEdit.setText('')

    def delete_item(self):
        # Lấy index dòng đang chọn trên list widget
        cur = self.listWidget.currentRow()
        # Lấy text ở lineEdit
        text = self.lineEdit.text()
        # Kiểm tra index và xóa
        if 0 <= cur <= len(arr):
            arr.pop(cur)
            msg_box('Thành công','Đã xóa đối tượng khỏi danh sách')
        else:
            msg_box('Lỗi', 'Chưa chọn đối tượng để xóa!')
        # Xóa hết các phần tử trên widget
        self.listWidget.clear()
        # Thêm lại danh sách
        self.listWidget.addItems(arr)
        # Xóa dữ liệu ở lineEdit
        self.lineEdit.setText('')

    def search_item(self):
        cur = self.listWidget.currentRow()
        insert_txt = self.lineEdit.text()
        check = False
        check_list = []
        for item in arr:
            if insert_txt in item:
                check = True
                check_list.append(item)
        
        # Xóa hết các phần tử ở trên widget
        self.listWidget.clear()
        # add lại cả danh sách vào list widget
        if check == True:
            msg_box('Thành công', f'Có {len(check_list)} kết quả!')
        else:
            check_list.append('item not found')
        self.listWidget.addItems(check_list)

def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

# Run app
window = MainWindow()
window.show()
sys.exit(app.exec())