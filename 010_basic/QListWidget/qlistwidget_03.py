"""
QListWidget Examples

Info:
    * Updated: 2022/09/03
    * Created: 2022/08/29
    * Coding: Tatsuya YAMAGISHI
"""
import sys

from PySide6 import QtCore, QtGui, QtWidgets

ITEMS = ['TEST-A', 'TEST-B', 'TEST-C', 'TEST-D',]


class Widget(QtWidgets.QWidget):
    """
    Custom ListWidget
    """

    def __init__(self, parent=None):
        """
        Init QListWidget
        """
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.list = QtWidgets.QListWidget()
        self.main_layout.addWidget(self.list)

        self.list.setSortingEnabled(True)
        self.list.setAlternatingRowColors(True)
        self.list.setAlternatingRowColors(True)
        self.list.setSelectionMode(
                QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)


        self.button = QtWidgets.QPushButton('Push')
        self.main_layout.addWidget(self.button)

        # Signals
        self.list.itemClicked.connect(self.activated)
        self.list.currentItemChanged.connect(self.activated)

        self.button.clicked.connect(self.button_clicked)

    
    def activated(self, item):
        """
        Selected Item
        """
        if item:
            print(item.text())


    def button_clicked(self):
        items = []
        for index in range(self.list.count()):
            items.append(self.list.item(index))

        for item in items:
            print(item.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = Widget()
    view.list.addItems(ITEMS)
    view.show()
    app.exec()