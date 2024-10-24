"""
* Horizontal Layout Example

Info:
    * Version: v1.0.0

Release Note:
    2022/08/01 Tatsuya YAMAGISHI
        * Add New
"""

import sys

from PySide6 import QtCore, QtGui, QtWidgets

class View(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QHBoxLayout(self)

        self.label = QtWidgets.QLabel('Name:')
        self.text = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton('Push')
        
        layout.addWidget(self.label)
        layout.addWidget(self.text)
        layout.addWidget(self.button)

        """
        horizontal spacer
        """
        self.hspacer = QtWidgets.QSpacerItem(
            40, 20, 
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum)
            
        layout.addItem(self.hspacer)


        self.resize(600, 150)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = View()
    view.show()
    app.exec()