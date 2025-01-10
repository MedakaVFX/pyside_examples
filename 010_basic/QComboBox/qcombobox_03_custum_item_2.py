"""
QComboBox Example

Info:
    * Created: 2025/01/10
    * Coding: Tatsuya YAMAGISHI
    * Coding: Python 3.12.4 & PySide6
"""
import sys

from PySide6 import QtCore, QtGui, QtWidgets

ITEMS = [
    {'name': 'HD', 'width': 1920, 'height': 1080},
    {'name': '2K', 'width': 2048, 'height': 1152},
    {'name': 'UHD', 'width': 3840, 'height': 2160},
]


class Item(QtGui.QStandardItem):
    def __init__(self, value, parent=None):
        super().__init__(parent)

        self._value = value

        self.setText(self._value.get('name'))

    def get_size(self) -> tuple:
        return (self._value.get('width'), self._value.get('height'))


    def get_value(self) -> dict:
        return self._value


class ComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        
        self.item_model = QtGui.QStandardItemModel()
        self.setModel(self.item_model)

        self.activated.connect(self.activate_item)

    
    def activate_item(self, index):
        item = self.item_model.item(index)
        print(item)

        print(item.get_size())


    def add_items(self, items):
        for value in items:
            item = Item(value)

            self.item_model.appendRow(item)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = ComboBox()
    view.add_items(ITEMS)
    view.show()
    app.exec()