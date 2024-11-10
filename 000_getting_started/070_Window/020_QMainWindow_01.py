import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィジェットオブジェクト作成
window = QMainWindow()

# ウィンドウタイトルを変更
window.setWindowTitle('Main Window')

# ウィンドウサイズの変更
window.resize(300, 200)

# ウィジェットの表示
window.show()

# アプリケーションメインループ開始
app.exec()