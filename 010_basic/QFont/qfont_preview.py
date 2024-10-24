"""
Info:
    updated : 2024.10.24 Tatsuya Yamagishi
    created : 2021.12.04 Tatsuya Yamagishi
    client :  'Python 3.7.9 & PySide6'

"""
_name = 'QFont Preview'
_version = 'v1.1.0'

import sys
import logging

from PySide6 import QtCore, QtGui, QtWidgets

##########################################################
# Reference from:
# https://kiwamiden.com/how-to-make-intslidergrp-modki-with-pyside
##########################################################

logging.basicConfig(
        level = logging.DEBUG,
        format='[%(levelname)s][%(asctime)s][%(filename)s][%(funcName)s:%(lineno)s]\n%(message)s'
    )
logger = logging.getLogger(__name__)

class FontPreviewQt(QtWidgets.QWidget):
    def __init__(self, logger, parent=None):
        super().__init__(parent)

        self.logger = logger

        self.initUi()
        self.setupSingals()
        self.setFont('Times New Roman')

    #===========================================#
    # init Ui
    #===========================================#
    def initUi(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self._font = QtWidgets.QFontComboBox()
        layout.addWidget(self._font)

        layout_1 = QtWidgets.QHBoxLayout()
        layout.addLayout(layout_1)

        self._size = QtWidgets.QSpinBox()
        self._size.setMinimumWidth(50)
        layout_1.addWidget(self._size)

        self._slider = QtWidgets.QSlider()
        self._slider.setMaximum(100)
        self._slider.setOrientation(QtCore.Qt.Horizontal)
        layout_1.addWidget(self._slider)

        self._text = QtWidgets.QPlainTextEdit('ABCDE')
        layout.addWidget(self._text)

        self._code = QtWidgets.QPlainTextEdit()
        font = QtGui.QFont()
        font.setFamily('Courier New')
        font.setPointSize(11)
        self._code.setFont(font)
        layout.addWidget(self._code)

    #===========================================#
    # Setup Signals
    #===========================================#
    def setupSingals(self):
        self._size.valueChanged.connect(self.updateUi)
        self._slider.valueChanged.connect(self.updateUi)
        self._font.currentFontChanged.connect(self.updateUi)

    #===========================================#
    # Setup Signals
    #===========================================#
    def updateUi(self):
        self.logger.info('Update UI')

        self._slider.blockSignals(True)
        self._size.blockSignals(True)
        self._font.blockSignals(True)
        self._text.blockSignals(True)

        sender = self.sender()

        if sender == self._size:
            value = self._size.value()
            self._slider.setValue(value)

        elif sender == self._slider:
            value = self._slider.value()
            self._size.setValue(value)

        font = self._font.currentFont()
        size = self._size.value()
        font_type = font.family()
        font.setPointSize(size)

        self.logger.debug(f'Font: {font_type}\nSize: {size}')

        self._text.setFont(font)

        # Code
        code = f"font = QtGui.QFont()\nfont.setFamily('{font_type}')\nfont.setPointSize({size})"
        self._code.setPlainText(code)

        # Clipoboard
        clipboard = QtGui.QClipboard()
        clipboard.setText(font_type)

        self._slider.blockSignals(False)
        self._size.blockSignals(False)
        self._font.blockSignals(False)
        self._text.blockSignals(False)

    #===========================================#
    # Set / Get
    #===========================================#
    def setSize(self, size):
        self._size.setValue(size)

    def setFont(self, font):
        font = QtGui.QFont(font)
        self._font.setCurrentFont(font)


class View(QtWidgets.QDialog):
    def __init__(self, logger, parent=None):
        super().__init__(parent)
        self.logger = logger

        self.resize(420, 250)
        self.setWindowTitle(f'{_name} {_version}')

        layout = QtWidgets.QVBoxLayout(self)
        self.ui = FontPreviewQt(self.logger, self)
        layout.addWidget(self.ui)

        self.setup()

    #===========================================#
    # Setup
    #===========================================#
    def setup(self):
        self.ui.setSize(11)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = View(logger)
    view.show() 
    sys.exit(app.exec())