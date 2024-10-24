import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィジェットオブジェクト作成
view = QWidget()

# ウィンドウタイトルを変更
view.setWindowTitle('Main Window')

# ウィンドウサイズの変更
view.resize(300, 200)

# ウィジェットの表示
view.show()

# アプリケーションメインループ開始
app.exec()