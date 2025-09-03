"""
ウィジェットにカスタムシグナルを設定する例
"""

import sys
from PySide6 import QtCore, QtGui, QtWidgets



class CustomWidget(QtWidgets.QWidget):
    # カスタムシグナルの定義
    text_changed = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._main_layout= QtWidgets.QVBoxLayout(self)
        self._label = QtWidgets.QLabel("TextChanged connect custom signal", self)
        self._text = QtWidgets.QLineEdit()

        self._main_layout.addWidget(self._label)
        self._main_layout.addWidget(self._text)

        self._text.textChanged.connect(self.on_text_changed)

    def on_text_changed(self, text):
        # テキストが変更されたときにカスタムシグナルを発行
        self.text_changed.emit(text)


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._text_1 = CustomWidget()
        self._text_2 = CustomWidget()

        self._label_1 = QtWidgets.QLabel("Label 1")
        self._label_2 = QtWidgets.QLabel("Label 2")

        self._text_1.text_changed.connect(self._label_1.setText)
        self._text_2.text_changed.connect(self._label_2.setText)

        self._main_layout = QtWidgets.QVBoxLayout(self)
        self._main_layout.addWidget(self._text_1)
        self._main_layout.addWidget(self._label_1)
        self._main_layout.addWidget(self._text_2)
        self._main_layout.addWidget(self._label_2)

        self.resize(400, 200)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())