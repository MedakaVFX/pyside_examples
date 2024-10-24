import sys

from PySide6 import QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWidget()
    view.show()
    app.exec()