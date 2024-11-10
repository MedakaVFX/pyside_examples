import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QVBoxLayout
)

# QDialogクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        """
        setLayoutでparentの定義もされるので引数のselfを省略しても問題ない。
        self.main_layout = QVBoxLayout()
        """
        # 縦レイアウトを作成
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ボタンを作成
        self.button_1 = QPushButton('Button1', self)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.button_1)


        # ボタン2を作成
        self.button_2 = QPushButton('Button2', self)
        self.main_layout.addWidget(self.button_2)

        self.setWindowTitle('MyWidget')
        self.resize(300, 200)

app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()