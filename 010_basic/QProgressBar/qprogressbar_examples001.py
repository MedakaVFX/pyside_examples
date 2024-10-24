import sys
from PySide6.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QVBoxLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # プログレスバーの作成
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        # ボタンの作成
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        # レイアウトの設定
        vbox = QVBoxLayout()
        vbox.addWidget(self.pbar)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

        # ウィンドウの設定
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('ProgressBar')
        self.show()

    def doAction(self):
        # プログレスバーの値を0に設定
        self.pbar.setValue(0)

        # ループを使用してプログレスバーを更新
        for i in range(101):
            self.pbar.setValue(i)
            QApplication.processEvents() # GUIの更新

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())