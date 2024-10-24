import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ダイアログオブジェクト作成
dialog = QDialog()

# ウィンドウタイトルを変更
dialog.setWindowTitle('My Dialog')

# ウィンドウサイズの変更
dialog.resize(300, 200)

# ダイアログでメインループ開始
result = dialog.exec()

print(result)