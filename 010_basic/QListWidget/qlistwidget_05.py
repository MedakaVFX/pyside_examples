"""
QListWidget Examples:
    * This example is an error.

Info:
    * Updated: 2022/09/18
    * Created: 2022/09/18
    * Coding: Tatsuya YAMAGISHI
"""
import sys

from PySide6 import QtCore, QtGui, QtWidgets

ITEMS_1 = ['TEST-A', 'TEST-B', 'TEST-C', 'TEST-D',]
ITEMS_2 = ['TEST-E', 'TEST-F', 'TEST-G',]


class CustomListWidgetItem(QtWidgets.QListWidgetItem):
    """
    Custom ListWidgetItem
    """
    def __init__(self, args, parent=None):
        super().__init__(parent)

        self._value = None

        self.set(args)

    def set(self, value):
        self._value = value

        self.setText(value)

    def get(self):
        return self._value

class CustomListWidget(QtWidgets.QListWidget):
    """
    Custom List Widegt
    """
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.setSelectionMode(
                QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)

        self.init_signals()

    def init_signals(self):
        self.itemClicked.connect(self.item_activated)
        self.currentItemChanged.connect(self.item_activated)

    
    def item_activated(self, item):
        """
        Selected Item
        """
        if item:
            print(item.get())


    def add_items(self, items):
        self.clear()
        
        for item in items:
            new_item = CustomListWidgetItem(item, self)


class Widget(QtWidgets.QWidget):
    """
    Main Widget
    """

    def __init__(self, parent=None):
        """
        Init QListWidget
        """
        super().__init__(parent)

        self.main_layout = QtWidgets.QHBoxLayout(self)

        self.list_1 = CustomListWidget()
        self.main_layout.addWidget(self.list_1)

        self.list_2 = CustomListWidget()
        self.main_layout.addWidget(self.list_2)



    def button_clicked(self):
        items = []
        for index in range(self.list.count()):
            items.append(self.list.item(index))

        for item in items:
            print(item.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = Widget()
    view.list_1.add_items(ITEMS_1)
    view.list_2.add_items(ITEMS_2)
    view.show()
    app.exec()