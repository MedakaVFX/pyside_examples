import sys

from PySide6.QtGui import (
    QAction,
    QKeySequence
)

from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QMenu, QMenuBar, QStatusBar,
)

# Qアプリケーション作成
app = QApplication(sys.argv)

# ウィンドウオブジェクト作成
window = QMainWindow()


#--------------------------#
# メニューバーの作成
#--------------------------#
"""
 * QMainWindow.menuBar()でもメニューバーを作成出来る。

menubar = window.menuBar()
"""
menubar = QMenuBar()
window.setMenuBar(menubar)

# ファイルメニューの作成
menu_file = QMenu('File')
menubar.addAction(menu_file.menuAction())

# # ファイルメニュー内にアクションを追加
action = QAction('Exit')
action.setShortcut(QKeySequence('Ctrl+Q'))
action.triggered.connect(window.close)
menu_file.addAction(action)


#--------------------------#
# ステータスバーの作成
#--------------------------#
"""
 * QMainWindow.statuBar()でもステータスバーを作成出来る。

statusbar = window.statusBar()
"""
statusbar = QStatusBar(window)
window.setStatusBar(statusbar)
statusbar.showMessage('Status Bar') 
# statusbar.showMessage('Status Bar', 5000) # timeout: int=0 (ms)

# ウィンドウタイトルを変更
window.setWindowTitle('Main Window')

# ウィンドウサイズの変更
window.resize(300, 200)

# ウィンドウの表示
window.show()

# アプリケーションメインループ開始
app.exec()