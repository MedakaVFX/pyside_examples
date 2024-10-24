import sys

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QWidget
)

# QDialogクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # メインレイアウトを作成
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ボタンを作成
        self.button = QPushButton('Button1', self)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.button)


        # レイアウト1を作成
        self.layout_1 = QHBoxLayout()

        # ラベルを作成しレイアウト１に登録
        self.label = QLabel('Name:')
        self.layout_1.addWidget(self.label)

        # ラインエディットを作成しレイアウト１に登録
        self.lineedit = QLineEdit(self)
        self.lineedit.setMinimumWidth(100)
        self.lineedit.setHidden(True)
        self.layout_1.addWidget(self.lineedit)

        # ボタンsetを作成しレイアウト１に登録
        self.button_set = QPushButton('Set', self)
        self.layout_1.addWidget(self.button_set)

        # レイアウト１をメインレイアウトにセット
        self.main_layout.addLayout(self.layout_1)

        self.setWindowTitle('MyWidget')
        self.resize(300, 200)

app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()