""" Cutsom TreeWidgetItem
Reference form : Customize QTreeWidgetItem PySide6
https://stackoverflow.com/questions/62264577/customize-qtreewidgetitem-PySide6

Python 3.7.9 & PySide6
"""

import dataclasses

from PySide6 import QtWidgets, QtCore, QtGui

DATA = [
    {'name': 'Yamada', 'age': 20, 'category': 'A01'},
    {'name': 'Tanaka', 'age': 24, 'category': 'A01'},
    {'name': 'Akimoto', 'age': 24, 'category': 'A02'},
    {'name': 'Yoshizawa', 'age': 35, 'category': 'A03'},
    {'name': 'Yamagishi', 'age': 28, 'category': 'B01'},
    {'name': 'Sakamoto', 'age': 32, 'category': 'B02'},
]

# 辞書型のままでもいいが、遊びでDataclass使ってみた
@dataclasses.dataclass
class Data:
    name: str
    age: int
    category: str


class MyItemWidget(QtWidgets.QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.data = data

        self.init_ui()
        self.update_style()

    
    def init_ui(self):
        # 引数にparentを渡すことで widget.setLayout(layout) を省略可
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.label_name = QtWidgets.QLabel(self.data.name)
        self.label_name.setFixedWidth(100)
        self.main_layout.addWidget(self.label_name)

        self.label_age = QtWidgets.QLabel('Age:')
        self.label_age.setFixedWidth(50)
        self.main_layout.addWidget(self.label_age)

        self.spinner = QtWidgets.QSpinBox()
        self.spinner.setMinimumWidth(50)
        self.spinner.setValue(self.data.age)
        self.main_layout.addWidget(self.spinner)

    def update_style(self):
        color = (255, 100, 50)

        style = f'background-color: rgb({color[0]}, {color[1]}, {color[2]});'

        if self.data.age > 29:
            self.setStyleSheet(style)

    def get_data(self):
        return self.data


class MyTreeWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.NAME = 'MyTreeWidget'
        self.VERSION = 'v1.1.1'
        self.HEADERS = ['Person', 'Description']
        self.SORTED_BY_COLUMN = 0
        self.HEADE1_SIZE = 200
        self.WINDOW_SIZE = [400, 400]

        self.init_ui()

        # Init Signals
        self.tree_widget.itemClicked.connect(self.item_activated)

    def init_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        # self.main_layout.setContentsMargins(0, 0, 0, 0)

        # TreeWidget
        self.tree_widget = QtWidgets.QTreeWidget()
        self.tree_widget.setColumnCount(len(self.HEADERS))
        self.tree_widget.setHeaderLabels(self.HEADERS)
        self.tree_widget.header().resizeSection(0, self.HEADE1_SIZE)
        self.tree_widget.setSortingEnabled(True)
        self.tree_widget.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.tree_widget.setRootIsDecorated(False)
        self.main_layout.addWidget(self.tree_widget)

        self.setWindowTitle(f'{self.NAME} {self.VERSION}')
        self.resize(*self.WINDOW_SIZE)


    def set_data(self, data_dict: dict):
        ui = self.tree_widget
        ui.clear()

        for d in data_dict:
            data = Data(**d)

            # Top Item
            top_item = self.get_top_item(data.category)

            # Item
            item = QtWidgets.QTreeWidgetItem(top_item)
            widget = MyItemWidget(data)
            ui.setItemWidget(item, 0, widget)

        ui.sortByColumn(self.SORTED_BY_COLUMN, QtCore.Qt.AscendingOrder)
        ui.expandToDepth(0)


    def get_top_item(self, name):
        ui = self.tree_widget
        num = ui.topLevelItemCount()
        result = None

        if num:
            for i in range(num):
                item = ui.topLevelItem(i)
                if item.text(0) == name:
                    result = item
                    break
        
        if result is None:
            result = QtWidgets.QTreeWidgetItem(ui)
            result.setText(0, name)

        return result


    def item_activated(self, item):
        if item:
            widget = self.tree_widget.itemWidget(item, 0)
            print(widget)
            print(widget.get_data())

app = QtWidgets.QApplication([])
view = MyTreeWidget()
view.set_data(DATA)
view.show()
app.exec()