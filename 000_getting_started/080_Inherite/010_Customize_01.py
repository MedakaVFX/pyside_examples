import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    # __init__関数。parent=Noneはテンプレート
    def __init__(self, parent=None):

        # parentを継承元に渡すようにする。
        super().__init__(parent)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィジェットオブジェクト作成
view = MyWidget()

# ウィンドウタイトルを変更
view.setWindowTitle('MyWidget')

# ウィンドウサイズの変更
view.resize(300, 200)

# ウィジェットの表示
view.show()

# アプリケーションメインループ開始
app.exec()