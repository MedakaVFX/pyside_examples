import sys

try:
    from PySide6 import QtCore, QtGui, QtWidgets
except:
    from qtpy import QtCore, QtGui, QtWidgets


class View(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        
        self.checkbox = QtWidgets.QCheckBox('CheckBox')
        self.checkbox.setCheckState(QtCore.Qt.Checked)
        self.main_layout.addWidget(self.checkbox)

        self.button = QtWidgets.QPushButton('Push')
        self.main_layout.addWidget(self.button)
        self.button.clicked.connect(self.button_clicked)


    def button_clicked(self):
        print(self.checkbox.checkState())

        if self.checkbox.checkState() == QtCore.Qt.Checked: # Qt.Unchecked
            print('True')
        else:
            print('False')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = View()
    view.show()
    app.exec()