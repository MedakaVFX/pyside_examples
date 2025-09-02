""" トグルボタンサンプル
Info:
    Coding: Python 3.12.4 & PySide6
    Coding by: 2024-12-16 Tatsuya Yamagishi
    Updated: 2025-02-03
"""

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Toggle Button Example")
        
        # ボタンの作成
        self.toggle_button = QPushButton("Toggle Button")
        self.toggle_button.setCheckable(True)  # トグル動作を有効化
        self.toggle_button.clicked.connect(self.on_toggle_button_clicked)
        
        # ラベルの作成
        self.label = QLabel("Button is OFF")
        
        # レイアウトの作成
        layout = QVBoxLayout()
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.label)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def on_toggle_button_clicked(self):
        # ボタンの状態を確認
        if self.toggle_button.isChecked():
            self.label.setText("Button is ON")
            self.toggle_button.setText("ON")
        else:
            self.label.setText("Button is OFF")
            self.toggle_button.setText("OFF")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())