import sys
import webbrowser

from PySide6 import QtGui, QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(400, 150)
        self.setWindowTitle('MyMainWinodw')

        self.setup()

    def setup(self):
        self.setupMenuBar()
        self.setupCentralWidget()
        self.setupStatusBar()

    #--------------------------------------#
    # Setup CentralWidget
    #--------------------------------------#
    def setupCentralWidget(self):
        layout = QtWidgets.QVBoxLayout()
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(layout)

        # QPushButton
        self.button = QtWidgets.QPushButton('Push Button')
        layout.addWidget(self.button)

        self.setCentralWidget(self.widget)

    #--------------------------------------#
    # Setup Status Bar
    #--------------------------------------#
    def setupStatusBar(self):
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

    #--------------------------------------#
    # Setup MenuBar
    #--------------------------------------#
    def setupMenuBar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menubar)
        
        self.menu_file = QtWidgets.QMenu('File', self)
        self.menubar.addAction(self.menu_file.menuAction())

        action = QtGui.QAction('Action1', self)
        action.setShortcut(QtGui.QKeySequence('Ctrl+1'))
        action.triggered.connect(self.action_1_event)
        self.menu_file.addAction(action)

        action = QtGui.QAction('Action2', self)
        action.triggered.connect(lambda: self.action_event('Action2'))
        self.menu_file.addAction(action)

        self.menu_file.addSeparator()

        submenu_helps = QtWidgets.QMenu('Helps', self)
        self.menu_file.addAction(submenu_helps.menuAction())

        tools = {
            'ZBursh': 'https://www.zbrushcentral.com/',
            'Houdini': 'https://www.sidefx.com/',
            'UE': 'https://www.unrealengine.com/en-US/',
        }

        for tool in tools:
            action = QtGui.QAction(tool, self)
            action.triggered.connect(lambda func=self.open_url, key=tool: func(tools[key]))
            submenu_helps.addAction(action)

        self.menu_file.addSeparator()

        action = QtGui.QAction('Exit', self)
        action.triggered.connect(self.exit_event)
        self.menu_file.addAction(action)

    #--------------------------------------#
    # Function
    #--------------------------------------#
    def open_url(self, url):
        webbrowser.open(url, new=2)

    #--------------------------------------#
    # Event
    #--------------------------------------#
    def action_event(self, text):
        print(text)

    def action_1_event(self):
        print('Action1')

    def exit_event(self):
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWindow()
    view.show()
    
    app.exec()