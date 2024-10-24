#=========================================================#
# Python 3.7.9 & PySide6
# Coding by Tatsuya Yamagishi
#=========================================================#
import sys
import time

from PySide6 import QtCore, QtGui, QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.w = 512
        self.h = 512
        self.BG_COLOR = QtGui.QColor('Blue')
        self.name = 'Drawing UV - paintEvent'
        self.redraw = False

        self.resize(self.w , self.h)
        self.setWindowTitle(self.name)

        #--------------------------------------#
        # Setup CentralWidget
        #--------------------------------------#
        layout = QtWidgets.QVBoxLayout()
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        # Label
        self.title = QtWidgets.QLabel(self.name)
        font = QtGui.QFont()
        font.setFamily('Arial Black')
        font.setPointSize(24)
        self.title.setFont(font)
        layout.addWidget(self.title)

        # Draw Button
        self.button_draw = QtWidgets.QPushButton('Draw')
        layout.addWidget(self.button_draw)

        # LineEdit
        self.lineEdit = QtWidgets.QLineEdit()
        layout.addWidget(self.lineEdit)

        # Draw Panel
        self.view = QtWidgets.QLabel()
        self.view.setAlignment(QtCore.Qt.AlignCenter)
        self.view.setAutoFillBackground(True)
        self.view.setFrameShape(QtWidgets.QFrame.Box)
        self.view.setLineWidth(2)
        self.view.setFixedSize(self.w, self.h)
        layout.addWidget(self.view)

        # Pixmap
        self.image = QtGui.QImage(
            self.w, self.h , 
            QtGui.QImage.Format_RGB888
        )
        self.image.fill(self.BG_COLOR)
        # self.pixmap = QtGui.QPixmap(self.w, self.h)
        # self.pixmap.fill(QtGui.QColor('Blue'))
        # self.view.setPixmap(self.pixmap)
        #--------------------------------------#
        # StatusBar
        #--------------------------------------#
        self.status_bar = self.statusBar()

        self.button_draw.pressed.connect(self.draw)

        # Update Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(200)

    def draw(self):
        start = time.time()
        print('Draw Start')

        w = self.w
        h = self.h

        image = self.image
        image.fill(self.BG_COLOR)

        for y in range(self.h):
            for x in range(self.w):
                r, g, b = self.get_pixel_color(x, y)
                color = QtGui.QColor(r, g, b)
                image.setPixelColor(x, y , color)
                QtWidgets.QApplication.processEvents()
                # self.update()

        print('Draw Finished.')
        elapsed = time.time() - start

        m, s = divmod(elapsed, 60)
        result = f'Draw time = {int(m)}:{s:.3f}'
        self.lineEdit.setText(result)

    def get_pixel_color(self, x, y):
        return self.uv(x, y)

    def uv(self, x, y):
        r = int(min(x+0.5/self.w, 255))
        g = int(min(y+0.5/self.h, 255))
        b = 0

        return r, g, b
                
    def paintEvent(self, event: QtGui.QPaintEvent):
        self.view.setPixmap(QtGui.QPixmap(self.image))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MyWindow()
    view.show()
    sys.exit(app.exec())