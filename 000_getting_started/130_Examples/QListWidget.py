import sys

from PySide6.QtWidgets import (
    QApplication, QDialog, QListWidget,
    QPushButton, QVBoxLayout,
)

ITEMS = ['CharaA', 'CharaB', 'CharaC', 'CharaD',]

class MyWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)


        # ボタン作成
        self.button = QPushButton('Clear')


        # ListWidget作成
        self.list = QListWidget()
        # Item追加
        self.list.addItems(ITEMS)
        # ソート機能
        self.list.setSortingEnabled(True)
        # 隔行で色変更
        self.list.setAlternatingRowColors(True)
        # 複数選択モード
        self.list.setSelectionMode(QListWidget.ExtendedSelection)


        # シグナル設定
        self.list.itemClicked.connect(self.list_activated)
        self.button.clicked.connect(self.button_clicked)


        # レイアウト
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.list)


    def list_activated(self, item):
        if item:
            print(item.text())


    def button_clicked(self):
        self.list.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MyWidget()
    view.resize(150, 200)
    view.show()
    app.exec()