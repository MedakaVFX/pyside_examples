"""StackWidget Example01
Info:
    * Version : v1.0.0
    * Updated : 2023-02-16 Tatsuya YAMAGISHI
    * Created : 2023-02-16 Tatsuya YAMAGISHI
    * Coding : Python 3.7.9 & PySide6
"""

import sys

from PySide6 import QtWidgets

class MyWidget(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(300, 300)

        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.list = QtWidgets.QComboBox()
        self.list.setFixedWidth(80)
        self.list.addItems(['Page1', 'Page2', 'Page3'])
        self.main_layout.addWidget(self.list)


        self.widget_1 = QtWidgets.QLabel('Stack1')
        self.widget_2 = QtWidgets.QLabel('Stack2')
        self.widget_3 = QtWidgets.QLabel('Stack3')

        self.stack = QtWidgets.QStackedWidget()
        self.stack.addWidget(self.widget_1)    
        self.stack.addWidget(self.widget_2)    
        self.stack.addWidget(self.widget_3)

        self.main_layout.addWidget(self.stack)

        self.list.activated.connect(self.list_activated)


    def list_activated(self, index):
        self.stack.setCurrentIndex(index)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWidget()
    view.show()
    app.exec()