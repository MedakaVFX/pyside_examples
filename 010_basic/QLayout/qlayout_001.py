import sys

from PySide6 import QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        self.button_1 = QtWidgets.QPushButton('Button 1')
        self.button_2 = QtWidgets.QPushButton('Button 2')
        self.button_3 = QtWidgets.QPushButton('Button 3')

        self.main_layout.addWidget(self.button_1)
        self.main_layout.addWidget(self.button_2)

        # Inserted Widget
        self.main_layout.insertWidget(1, self.button_3)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWidget()
    view.show()
    app.exec()