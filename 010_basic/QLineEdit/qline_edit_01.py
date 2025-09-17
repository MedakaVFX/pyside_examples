"""
QListWidget Examples

Info:
    * Created: 2022/08/29
    * Coding: Tatsuya YAMAGISHI
"""
import sys

from PySide6 import QtCore, QtGui, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._main_layout = QtWidgets.QVBoxLayout(self)

        self._text = QtWidgets.QLineEdit()
        self._text.setPlaceholderText("Type something and press Enter")
        
        # 入力制限
        regex = QtCore.QRegularExpression('^[A-Za-z0-9_-]+$')  # 英数字のみ
        validator = QtGui.QRegularExpressionValidator(regex)
        self._text.setValidator(validator)

        self._main_layout.addWidget(self._text)

        self._text.returnPressed.connect(self._on_return_pressed)

    def _on_return_pressed(self):
        text = self._text.text()
        if text:
            print(f"Text entered: {text}")
            self._text.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWidget()
    view.show()
    app.exec()