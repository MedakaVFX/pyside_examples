import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget,
)

# QDialogクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.button = QPushButton('Push', self)
        self.button.setGeometry(50, 80, 200, 30)

        self.setWindowTitle('MyWidget')
        self.resize(300, 200)

app = QApplication(sys.argv)
view = MyWidget()
view.show()
app.exec()