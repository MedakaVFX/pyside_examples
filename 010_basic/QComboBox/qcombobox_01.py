"""
QComboBox Example

Info:
    * Created: 2022/09/13
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

        self.combobox = QtWidgets.QComboBox()
        self.main_layout.addWidget(self.combobox)
        self.combobox.activated.connect(self.activated)
        self.combobox.currentIndexChanged.connect(self.current_changed)

        

    def add_items(self, items):
        self.combobox.addItems(items)

    #--------------------------------#
    # Slots
    #--------------------------------#
    def activated(self, arg):
        print('Activated')
        print(arg)
        print(self.combobox.currentText())

    def current_changed(self, index):
        print('Current Changed')
        print(index)
        print(self.combobox.currentText())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = Widget()
    view.add_items(sorted(ITEMS))
    view.show()
    app.exec()