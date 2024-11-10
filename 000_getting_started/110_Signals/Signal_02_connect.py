import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout
)

# QDialogクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ラベルを作成
        self.line_edit = QLineEdit(self)
        self.line_edit.textEdited.connect(self.line_edit_edited)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.line_edit)


        # ボタンを作成
        self.button = QPushButton('Push', self)
        self.main_layout.addWidget(self.button)

        self.setWindowTitle('MyWidget')

    def line_edit_edited(self):
        print('Test')
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()