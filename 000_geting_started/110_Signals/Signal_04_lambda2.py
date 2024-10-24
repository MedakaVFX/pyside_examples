import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout
)

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ボタンを作成
        name = 'A'
        self.button_a = QPushButton(name, self)
        self.button_a.clicked.connect(
                lambda func=self.button_pressed, value=name: func(value))
        self.main_layout.addWidget(self.button_a)

        name = 'B'
        self.button_b = QPushButton(name, self)
        self.button_b.clicked.connect(
                lambda func=self.button_pressed, value=name: func(value))
        self.main_layout.addWidget(self.button_b)

        name = 'C'
        self.button_c = QPushButton(name, self)
        self.button_c.clicked.connect(
                lambda func=self.button_pressed, value=name: func(value))
        self.main_layout.addWidget(self.button_c)


    def button_pressed(self, text):
        print(f'Push {text}')
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()