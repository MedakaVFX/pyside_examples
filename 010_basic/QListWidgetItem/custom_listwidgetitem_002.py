"""
Reference From:
https://doc-snapshots.qt.io/qtforpython/PySide6/QtWidgets/QListWidgetItem.html#PySide6.QtWidgets.PySide6.QtWidgets.QListWidgetItem.setBackground

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
from PySide6 import QtGui, QtWidgets


ITEMS = [
    ('Red', (255, 100, 100), ),
    ('Green', (100, 255, 100),),
    ('Blue', (100, 100, 255), ),
]

class Item(QtWidgets.QListWidgetItem):
    def __init__(self, item, parent=None):
        super().__init__(parent)

        self.item = item
        self.setText(item[0])
        self.setBackground(QtGui.QColor(*item[1]))


class View(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Parent=selfで self.setLayout(layout) を省略
        self.main_layout = QtWidgets.QVBoxLayout(self)
        # self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.list = QtWidgets.QListWidget()
        self.main_layout.addWidget(self.list)

    def add_items(self, ITMES):
        self.list.clear()

        for ITEM in ITEMS:           
            item = Item(ITEM, self.list)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = View()
    view.add_items(ITEMS)
    view.show()
    app.exec()