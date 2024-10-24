import sys

from PySide6.QtWidgets import (
    QApplication,
    QPushButton
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィジェットオブジェクト作成
view = QPushButton('Push')

# ウィンドウタイトルを変更
view.setWindowTitle('Main Window')

# ウィンドウサイズの変更
view.resize(300, 100)

# ウィジェットの表示
view.show()

# アプリケーションメインループ開始
app.exec()