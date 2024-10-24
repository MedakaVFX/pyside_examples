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

        self.r_button_1 = QtWidgets.QRadioButton('Button 1')
        self.r_button_2 = QtWidgets.QRadioButton('Button 2')

        self.r_button_1.setChecked(True)

        self.main_layout.addWidget(self.r_button_1)
        self.main_layout.addWidget(self.r_button_2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = View()
    view.show()
    app.exec()