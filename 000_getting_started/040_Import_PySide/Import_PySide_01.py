from PySide6.QtCore import (
    QPoint, QRect, QSize, QTime, QUrl, Qt
)
from PySide6.QtGui import (
    QBrush, QColor, QKeySequence
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)


import PySide6.QtCore

# Prints PySide version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)