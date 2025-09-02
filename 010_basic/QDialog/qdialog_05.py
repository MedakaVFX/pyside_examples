from PySide6 import QtWidgets

class CustomDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Custom Dialog")
        self.resize(300, 200)

        label = QtWidgets.QLabel("This is a custom dialog.", self)
        self.splinner = QtWidgets.QSpinBox(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.splinner)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def get_value(self) -> int:
        return self.splinner.value()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dialog = CustomDialog()
    result = dialog.exec()

    if result == QtWidgets.QDialog.Accepted:
        _value = dialog.get_value()

        print(result, _value)