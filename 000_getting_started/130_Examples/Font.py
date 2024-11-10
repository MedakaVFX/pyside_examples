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


        font = QFont('Arial Black')
        # font.setFamily('Arial Black')
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)


        self.label = QLabel('Test')
        self.label.setFont(font)
        
        self.main_layout.addWidget(self.label)

        self.setWindowTitle('MyWidget')
        # self.resize(300, 200)

app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()