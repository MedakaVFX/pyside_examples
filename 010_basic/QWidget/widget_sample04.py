import sys

from PySide6 import QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    view = MyWidget()
    view.show()

    app.exec()