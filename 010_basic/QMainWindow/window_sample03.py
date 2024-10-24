import sys

from PySide6 import QtGui, QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(400, 150)
        self.setWindowTitle('MyMainWinodw')

        #--------------------------------------#
        # Setup CentralWidget
        #--------------------------------------#
        layout = QtWidgets.QVBoxLayout()
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(layout)

        # QPushButton
        self.button = QtWidgets.QPushButton('Push Button')
        self.button.clicked.connect(self.button_clicked)
        layout.addWidget(self.button)

        self.setCentralWidget(self.widget)

        #--------------------------------------#
        # Setup Status Bar
        #--------------------------------------#
        self.statusbar = self.statusBar()

        #--------------------------------------#
        # menuBar
        #--------------------------------------#
        self.menu_bar = self.menuBar()
        
        self.menu_file = self.menu_bar.addMenu('File')
        self.menu_bar.addAction(self.menu_file.menuAction())

        action = QtGui.QAction('Exit', self)
        self.menu_file.addAction(action)


    #--------------------------------------#
    # Event
    #--------------------------------------#
    def button_clicked(self):
        self.statusbar.showMessage('Button clicked.')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWindow()
    view.show()
    app.exec()