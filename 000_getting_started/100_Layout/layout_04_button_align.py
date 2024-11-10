import sys

from PySide6.QtCore import Qt

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
        # 位置合わせ
        self.main_layout.setAlignment(Qt.AlignHCenter)
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ボタンを作成
        self.button_1 = QPushButton('Button1', self)
        # 固定サイズを設定
        self.button_1.setFixedSize(200, 50)

        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.button_1)


        # ボタン2を作成
        self.button_2 = QPushButton('Button2', self)
        # 最大幅設定
        self.button_2.setMaximumWidth(100)
        self.main_layout.addWidget(self.button_2)

        self.setWindowTitle('MyWidget')
        self.resize(300, 200)

app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()