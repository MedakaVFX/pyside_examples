import sys

from PySide6.QtWidgets import (
    QApplication, QDialog,
    QPushButton, QLineEdit, QWidget, QVBoxLayout
)

# QWidgetクラスを継承してカスタムクラスを作成
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # メインレイアウト
        self.main_layout = QVBoxLayout()
        # Widgetにレイアウトをセット
        self.setLayout(self.main_layout)


        # ラベルを作成
        self.line_edit = QLineEdit(self)
        # シグナルをスロットに接続
        self.line_edit.textEdited.connect(self.line_edit_edited)
        # レイアウトにボタンを追加
        self.main_layout.addWidget(self.line_edit)


        # ボタンを作成
        """
        QPushButtonもLineEditと同じように
            * QPushButton.clicked
            * QPushButton.pressed
        というボタンを押した系のシグナルがある。
        クリックと右クリックのみの違いだったようだ
        """
        self.button = QPushButton('Push', self)
        self.button.clicked.connect(self.button_clicked)
        self.main_layout.addWidget(self.button)

        self.setWindowTitle('MyWidget')

    # シグナルの接続先関数
    def line_edit_edited(self, arg):
        """ line_edit.textEdited

         * ここにLineEditが編集された際の処理を記述
        
        """

        print(type(arg))
        print(arg)

    # ボタンを押した時のスロット
    def button_clicked(self):
        """ button.clicked

         * ここにボタンが押された際の処理を記述
        
        """
        self.line_edit.setText('')

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        self.widget_1 = MyWidget(self)
        self.main_layout.addWidget(self.widget_1)

        self.widget_2 = MyWidget(self)
        self.main_layout.addWidget(self.widget_2)

        self.setWindowTitle(self.__class__.__name__)
        self.resize(300, 200)

app = QApplication(sys.argv)
dialog = MyDialog()
result = dialog.exec()

"""
ダイアログだが普通のWindowとして表示したい場合

app = QApplication(sys.argv)
dialog = MyDialog()
dialog.show()
app.exec()
"""