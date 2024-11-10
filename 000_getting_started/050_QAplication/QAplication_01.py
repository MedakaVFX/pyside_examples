import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィジェットオブジェクト作成
window = QWidget()

# ウィジェットの表示
window.show()

# アプリケーションメインループ開始
app.exec()