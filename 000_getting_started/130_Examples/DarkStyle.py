import sys

from PySide6.QtWidgets import (
    QApplication, QTextEdit, QVBoxLayout, QWidget
)

import qdarkstyle

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_layout = QVBoxLayout(self)

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlainText('Test')
        self.main_layout.addWidget(self.text_edit)

        self.setWindowTitle('MyWidget')
        self.resize(300, 120)

app = QApplication(sys.argv)

# Set DarkStyel StyelSheet
dark_stylesheet = qdarkstyle.load_stylesheet_PySide6()
app.setStyleSheet(dark_stylesheet)

view = MyWidget()
view.show()

app.exec()