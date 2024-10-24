"""
ウィジェットを作成し、ドラッグアンドドロップで移動する
"""

import sys
from PySide6 import QtCore, QtGui, QtWidgets


class WidgetItem(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet('border: 2px solid black; background-color: green;')
        self.setFixedSize(128, 32)
        self._drag = False
        self._offset = QtCore.QPoint(0, 0)

    def mousePressEvent(self, event):
        self._drag = True
        self._offset = event.pos()

        print(self.text())


    def mouseReleaseEvent(self, event):
        self._drag = False

    def mouseMoveEvent(self, event):
        if self._drag:
            self.move(self.mapToParent(event.pos() - self._offset)) 
            # self.move(self.mapToParent(event.localPos() - self._offset))
            # print(event.localPos())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    widget = QtWidgets.QWidget()
    widget.setFixedSize(400, 300)
    widget.setLayout(QtWidgets.QVBoxLayout())
    
    layout = widget.layout()

    for i in range(1,5):
        item = WidgetItem(f'Item{i}')
        layout.addWidget(item)

    widget.show()

    app.exec()