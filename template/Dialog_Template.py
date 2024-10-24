import sys

from PySide6 import QtCore, QtGui, QtWidgets

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(400, 100)

        layout  = QtWidgets.QVBoxLayout(self)

        self.lineEdit = QtWidgets.QLineEdit(self)
        layout.addWidget(self.lineEdit)

        buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyDialog()
    result = view.exec()
    print(result)
