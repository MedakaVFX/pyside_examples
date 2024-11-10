import sys

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QDialog, QListWidget,
    QPushButton, QSplitter, QWidget, QVBoxLayout,
)

class MyWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # スプリッター作成/水平分割
        self.splitter = QSplitter()
        self.splitter.setOrientation(Qt.Horizontal)


        # 左側用ウィジェット
        self.widget_1 = QListWidget()


        # 右側用ウィジェット
        self.widget_2 = QWidget()
        self.layout_2 = QVBoxLayout(self.widget_2)

        self.button_1 = QPushButton('Button 1')
        self.button_2 = QPushButton('Button 2')
        self.button_3 = QPushButton('Button 3')


        # ウィジェットセット
        self.layout_2.addWidget(self.button_1)
        self.layout_2.addWidget(self.button_2)
        self.layout_2.addWidget(self.button_3)

        self.splitter.addWidget(self.widget_1)
        self.splitter.addWidget(self.widget_2)
        self.splitter.setSizes([244, 151])
        self.main_layout.addWidget(self.splitter)


        # シグナル
        self.splitter.splitterMoved.connect(
            lambda: self.splitter_moved(self.splitter))


    def splitter_moved(self, splitter):
        print(splitter.sizes())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MyWidget()
    view.resize(400, 200)
    view.show()
    app.exec()