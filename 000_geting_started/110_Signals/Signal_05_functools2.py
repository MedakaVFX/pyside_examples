import functools
import sys

from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QVBoxLayout
)

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ボタンを作成
        button_name_list = ['A', 'B', 'C',]

        for button_name in sorted(button_name_list):
            button = QPushButton(button_name, self)
            button.clicked.connect(
                functools.partial(self.button_pressed, button_name)
            )
            self.main_layout.addWidget(button)


    def button_pressed(self, text):
        print(f'Push {text}')
        
app = QApplication(sys.argv)
view = MyWidget()
view.resize(300, 200)
view.show()
app.exec()