from PySide6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dialog = QtWidgets.QDialog()
    result = dialog.exec()
    print(result)