import sys

from PySide6.QtGui import QFont

from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QTextEdit,
    QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QWidget
)

# QDialogクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # メインレイアウトを作成
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)

        # フォント
        font = QFont('Arial Black')
        # font.setFamily('Arial Black')
        font.setPointSize(15)
        font.setItalic(True)

        # スタイルシート：テキストの色
        # style_sheet = 'QLabel { color : red;}'
        # 16進数
        # style_sheet = 'QLabel { color : #ff0000;}'
        # 8bit RGB
        # style_sheet = 'QLabel { color : rgb(255, 0, 0)}'

        # QLabel作成
        self.label = QLabel('Test')
        self.label.setFont(font)
        self.label.setStyleSheet(style_sheet)
        
        self.main_layout.addWidget(self.label)

        self.setWindowTitle('MyWidget')
        # self.resize(300, 200)

app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()