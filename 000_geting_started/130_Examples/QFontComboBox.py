import sys

from PySide6.QtGui import QFont

from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QTextEdit,
    QLabel, QLineEdit, QPushButton, QFontComboBox,
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


        self.font_combobox =  QFontComboBox(self)
        self.main_layout.addWidget(self.font_combobox)

        font = self.font_combobox.currentFont()

        self.setWindowTitle('MyWidget')
        # self.resize(300, 200)

app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()