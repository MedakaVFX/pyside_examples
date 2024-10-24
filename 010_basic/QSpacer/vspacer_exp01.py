"""
* Vertical Layout Example
* Horizontalとの違いはQSizePolicyの定義が逆。

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

        layout = QtWidgets.QVBoxLayout(self)

        self.button_1 = QtWidgets.QPushButton('PushButton')
        self.button_2 = QtWidgets.QPushButton('PushButton')
        self.button_3 = QtWidgets.QPushButton('PushButton')
        
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        layout.addWidget(self.button_3)


        """
        vertical spacer
        """
        self.vspacer = QtWidgets.QSpacerItem(
            40, 20, 
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding)
            
        layout.addItem(self.vspacer)


        self.resize(300, 300)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = View()
    view.show()
    app.exec()