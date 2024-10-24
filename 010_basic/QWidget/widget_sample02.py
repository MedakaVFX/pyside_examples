import sys

from PySide6 import QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self, core, parent=None):
        super().__init__(parent)

        self.core = core

if __name__ == '__main__':
    core = None

    app = QtWidgets.QApplication(sys.argv)

    view = MyWidget(core)
    view.show()

    app.exec()