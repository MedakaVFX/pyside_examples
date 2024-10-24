from PySide6.QtWidgets import (
    QApplication,
    QMessageBox,
    QInputDialog
)

if __name__ == '__main__':
    app = QApplication([])
    # dialog = QMessageBox.information(
    #     None, 'Title', 'testtesttesttest',
    # )
    # print(dialog)

    dialog = QInputDialog.getText(
        None, 'Inpuit', 'Input Text:', text='Yamagishi'
    )
    print(dialog)