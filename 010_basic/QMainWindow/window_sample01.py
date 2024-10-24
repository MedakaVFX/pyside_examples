"""
PySide6 QMainWindow simple example:

Updated : v1.0.1 2022/06/13

Created : 2022/06/13
"""
import sys

from PySide6 import QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWindow()
    view.show()
    app.exec()