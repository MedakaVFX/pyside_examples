"""QListWidget Examples:
    * フィルタ設定

Info:
    * Updated: 2023/02/04
    * Created: 2023/02/04
    * Coding: Tatsuya YAMAGISHI
    * Python 3.9 & PySide6
"""
import sys

from PySide6 import QtCore, QtGui, QtWidgets

ITEMS = ['TEST-A', 'TEST-B', 'TEST-C', 'TEST-D', 'MAYA2020', 'MAYA2021', 'MAYA2022', 'MAYA2023']
    
class Widget(QtWidgets.QWidget):
    """
    Main Widget
    """

    def __init__(self, parent=None):
        """
        Init QListWidget
        """
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.filter = QtWidgets.QLineEdit('<filter>')
        self.main_layout.addWidget(self.filter)

        self.list = QtWidgets.QListWidget()
        self.list.setSortingEnabled(True)
        self.list.setAlternatingRowColors(True)
        self.main_layout.addWidget(self.list)

        self.filter.textEdited.connect(self.filter_list)


    def filter_list(self, text):
        for item in self.get_all_items():
            if text.lower() in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)


    def get_all_items(self):
        return [self.list.item(index) for index in range(self.list.count())]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = Widget()
    view.list.addItems(ITEMS)
    view.show()
    app.exec()