import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog
)

# QDialogクラスを継承してカスタムクラスを作成
class MyWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # ウィンドウタイトルの設定
        self.setWindowTitle('MyWidget')
        
        # ウィンドウサイズの変更
        self.resize(300, 200)


app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()