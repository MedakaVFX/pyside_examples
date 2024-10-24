import sys

from PySide6.QtCore import Qt

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


        self.text_edit = QTextEdit(self)
        self.text_edit.setPlainText('Test')
        self.text_edit.setDisabled(True)

        self.main_layout.addWidget(self.text_edit)


        # レイアウト1を作成
        self.layout_1 = QHBoxLayout()

        self.setWindowTitle('MyWidget')
        self.resize(300, 200)

app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()