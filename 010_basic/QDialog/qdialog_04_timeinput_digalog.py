""" 時間入力ダイアログ
Info:
    Coding: Python 3.12.4 & PySide6
    Created: 2025-02-09 Tatsuya Yamagishi
    Updated: 2025-02-09
"""
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTimeEdit, QPushButton
from PySide6.QtCore import QTime

class TimeInputDialog(QDialog):
    def __init__(self, parent=None, initial_time=None):
        super().__init__(parent)

        if initial_time is None:
            # initial_time = QTime.currentTime()
            initial_time = QTime(0, 0, 10)


        self.setWindowTitle("Select Time")

        self.layout = QVBoxLayout(self)

        # QTimeEdit ウィジェット
        self.time_edit = QTimeEdit(self)
        self.time_edit.setTime(initial_time)
        self.time_edit.setDisplayFormat('hh:mm:ss')
        self.layout.addWidget(self.time_edit)

        # OK ボタン
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

        # キャンセル ボタン
        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.reject)
        self.layout.addWidget(self.cancel_button)

    def get_time(self):
        return self.time_edit.time()

# 使い方
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    dialog = TimeInputDialog()
    if dialog.exec():
        selected_time = dialog.get_time()
        total_seconds = selected_time.msecsSinceStartOfDay() // 1000
        print(f"Selected Time: {selected_time.toString()}")
        print(f"Selected Time: {total_seconds}")

    app.exec()