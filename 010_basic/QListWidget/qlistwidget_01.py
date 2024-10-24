"""
QListWidget Examples

Info:
    * Created: 2022/08/29
    * Coding: Tatsuya YAMAGISHI
"""
import sys

from PySide6 import QtCore, QtGui, QtWidgets

ITEMS = ['TEST-A', 'TEST-B', 'TEST-C', 'TEST-D',]


class Widget(QtWidgets.QListWidget):
    """
    Custom ListWidget
    """

    def __init__(self, parent=None):
        """
        Init QListWidget
        """
        super().__init__(parent)

        # Methods
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)

        # PySide2
        # self.setSelectionMode(self.ExtendedSelection)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)

        # Signals
        self.itemClicked.connect(self.item_activated)
        self.currentItemChanged.connect(self.item_activated)

    
    def item_activated(self, item):
        """
        Selected Item
        """
        if item:
            print(item.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = Widget()
    view.addItems(sorted(ITEMS))
    view.show()
    app.exec()