import random
import sys


from PySide6 import QtCore, QtGui, QtWidgets

major_cities_japan = [
    "東京",  # Tokyo
    "大阪",  # Osaka
    "名古屋",  # Nagoya
    "札幌",  # Sapporo
    "福岡",  # Fukuoka
    "横浜",  # Yokohama
    "神戸",  # Kobe
    "京都",  # Kyoto
    "仙台",  # Sendai
    "広島",  # Hiroshima
    "川崎",  # Kawasaki
    "さいたま",  # Saitama
    "千葉",  # Chiba
    "静岡",  # Shizuoka
    "熊本",  # Kumamoto
    "那覇",  # Naha (Okinawa)
]


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.setWindowTitle("行先サイコロ")

        self.init_ui()

        self._state = False
        self.button.clicked.connect(self.roll_dice)


    def init_ui(self):
        self._main_widget = QtWidgets.QWidget(self)
        self._main_layout = QtWidgets.QVBoxLayout(self._main_widget)

        self.label = QtWidgets.QLabel("行先を決めるサイコロ", self)
        self.button = QtWidgets.QPushButton("サイコロを振る", self)
        self.label_location = QtWidgets.QLabel("行先: 未決定", self)

        _font = QtGui.QFont()
        _font.setPointSize(32)

        self.label.setFont(_font)
        self.button.setFont(_font)
        self.label_location.setFont(_font)

        self._main_layout.addWidget(self.label)
        self._main_layout.addWidget(self.button)
        self._main_layout.addWidget(self.label_location)

        self.setCentralWidget(self._main_widget)

    def roll_dice(self):
        if not self._state:
            self._state = True
            self.button.setEnabled(False)

            # Simulate rolling the dice
            selected_city = random.choice(major_cities_japan)
            self.label_location.setText(f"行先: {selected_city}")

            self._state = False
            self.button.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MainWidget()
    view.show()
    app.exec()