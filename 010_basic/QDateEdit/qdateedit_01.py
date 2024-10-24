"""
QDateEdit Example

Info:
    * Created: 2023/11/11
    * Coding: Tatsuya YAMAGISHI
"""

import sys

from PySide6 import QtCore, QtGui, QtWidgets


class DateWidget(QtWidgets.QDateEdit):
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = DateWidget()
    view.show()

    print(view.date())
    print(view.dateTime())

    # QtCore.QDate(y, m, d)
    view.setDate(QtCore.QDate(2023, 11, 11))

    app.exec()