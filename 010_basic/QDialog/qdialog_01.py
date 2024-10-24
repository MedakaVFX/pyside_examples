import sys

from PySide6 import QtCore, QtGui, QtWidgets
#=======================================#
# Referenced from:
# http://blawat2015.no-ip.com/~mieki256/diary/201611192.html
#=======================================#

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(400, 100)
        self.setWindowTitle('Please enter the text.')

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

    def get_text(self):
        return self.lineEdit.text()

    @staticmethod
    def getDate(parent = None):
        dialog = MyDialog(parent)
        result = dialog.exec()
        
        return (
            dialog.get_text(),
            result == QtWidgets.QDialog.Accepted
        )

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    result = MyDialog.getDate()
    print(result)
    app.exec()