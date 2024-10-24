import sys

from PySide6 import QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)

        self.button_1 = QtWidgets.QPushButton('Button 1', self)        
        self.button_1.clicked.connect(self.button_1_clicked)

        layout.addWidget(self.button_1)


    def button_1_clicked(self):
        print('Button 1')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWidget()
    view.show()
    app.exec()