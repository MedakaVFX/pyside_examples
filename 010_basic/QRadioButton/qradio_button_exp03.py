"""
* QRadioButton Example
* Coding : Python3.7.9 & PySide6
* Coding by : Tatsuya Yamagishi

Release:
    v1.0.0 2023/02/13 Tatsuya YAMAGISHI
        * Add New
"""

import sys

from PySide6 import QtCore, QtGui, QtWidgets

class View(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_layout = QtWidgets.QHBoxLayout(self)

        self.button_group = QtWidgets.QButtonGroup()
        

        self.r_button_1 = QtWidgets.QRadioButton('Button 1')
        self.r_button_2 = QtWidgets.QRadioButton('Button 2')

        self.r_button_1.setChecked(True)

        self.p_button_1 = QtWidgets.QPushButton('Push')
        
        self.button_group.addButton(self.r_button_1, 1)
        self.button_group.addButton(self.r_button_2)

        self.main_layout.addWidget(self.r_button_1)
        self.main_layout.addWidget(self.r_button_2)
        self.main_layout.addWidget(self.p_button_1)

        # self.main_layout.addLayout(self.button_group)

        self.p_button_1.clicked.connect(self.p_button1_clicked)
        self.button_group.buttonClicked.connect(self.button_group_clicked)


    def p_button1_clicked(self):
        print(self.button_group.checkedId())


    def button_group_clicked(self, item):
        print(item.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = View()
    view.show()
    app.exec()