import sys

from PySide6.QtWidgets import (
    QApplication,
    QPushButton
)

# QPushButtonクラスを継承してカスタムクラスを作成
class MyWidget(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # ウィンドウタイトルの設定
        self.setWindowTitle('MyWidget')
        
        # ウィンドウサイズの変更
        self.resize(300, 200)


app = QApplication(sys.argv)
# QPushButtonの第一引数はボタンラベル名
view = MyWidget('Push')
view.show()
app.exec()