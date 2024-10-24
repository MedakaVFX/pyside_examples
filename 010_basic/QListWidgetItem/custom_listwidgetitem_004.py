"""
Reference From:
https://stackoverflow.com/questions/25187444/pyqt-qlistwidget-custom-items

Version:
    * version = 'v1.0.0',
    * updated = '2022-06-20',
    * created = '2022-06-20',
    * updated_by = 'Tatsuya YAMAGISHI',
    * created_by = 'Tatsuya YAMAGISHI',
    * coding = 'Python 3.7.9 & PySide6',
"""
import sys

# from PySide6 import QtCore, QtGui, QtWidgets
from PySide6 import QtWidgets

ITEMS = [
    ('No.1', 'Tatsuya', ),
    ('No.2', 'Akira',),
    ('No.3', 'Naoto', ),
]

class MyWidget(QtWidgets.QWidget):
    def __init__(self, item, parent = None):
        super().__init__(parent)

        self.init_ui()
        self.set_item(item)


    def init_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.label_1 = QtWidgets.QLabel('Label_1')
        self.label_1.setStyleSheet('color: rgb(0, 0, 255);')

        self.label_2 = QtWidgets.QLabel('Label_2')
        self.label_2.setStyleSheet('color: rgb(255, 0, 0);')

        self.button = QtWidgets.QPushButton('Test')
        self.button.clicked.connect(self.button_clicked)


        self.main_layout.addWidget(self.label_1)
        self.main_layout.addWidget(self.label_2)
        self.main_layout.addWidget(self.button)

        
    def set_item(self, item):
        self.item = item

        self.label_1.setText(item[0])      
        self.label_2.setText(item[1])
        

    def button_clicked(self):
        print(f'Name: {self.get_name()}')


    def get_name(self):
        return self.item[1]

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.list = QtWidgets.QListWidget(self)
        self.list.itemClicked.connect(self.list_activated)

        layout = QtWidgets.QVBoxLayout(self)
        
        layout.addWidget(self.list)


    def addListItem(self, items):
        self.list.clear()

        for item in items:
            list_widget_item = QtWidgets.QListWidgetItem(self.list)
            my_widget = MyWidget(item)
            
            # Set SizeHintでサイズヒントの設定忘れないように
            list_widget_item.setSizeHint(my_widget.sizeHint())
            # ListWidgetItemにウィジェット設定
            self.list.setItemWidget(list_widget_item, my_widget)


    def list_activated(self, item):
        if item:
            widget = self.list.itemWidget(item)
            print(f'QWidget Slot : {widget.get_name()}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.addListItem(ITEMS)
    window.resize(300,300)
    window.show()
    app.exec()