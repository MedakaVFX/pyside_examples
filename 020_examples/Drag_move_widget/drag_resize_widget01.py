import sys
import enum
from PySide6 import QtCore, QtGui, QtWidgets

#===============================================================#
# Reference from :
# https://dungeonneko.hatenablog.com/entry/2017/06/19/180744
# Python 3.7.9 & PySide 2
#===============================================================#

class Item(QtWidgets.QLabel):
    Manipilate = enum.Enum(
        'Manipilate',
        'none move resize_l resize_r resize_t resize_b resize_lt resize_rt resize_lb resize_rb'
    )
    
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet('background-color: white; border: 1px solid black; padding: 4px;')
        self.resize(128, 64)
        self._mani = Item.Manipilate.none
        self._offset = QtCore.QPoint(0, 0)
        self._rect = self.rect()
        self.setMouseTracking(True)

        self.show()

    def mousePressEvent(self, event):
        pos = event.pos()
        if self._mani == Item.Manipilate.none:
            self._mani = self.get_manipulation(pos)
        self._offset = event.pos()
        self._rect = self.geometry()

    def mouseReleaseEvent(self, event):
        self._mani = Item.Manipilate.none

    def mouseMoveEvent(self, event):
        pos = event.pos()
        if self._mani == Item.Manipilate.none:
            self.setCursor({
                Item.Manipilate.none: QtCore.Qt.ArrowCursor,
                Item.Manipilate.move: QtCore.Qt.ArrowCursor,
                Item.Manipilate.resize_l: QtCore.Qt.SizeHorCursor,
                Item.Manipilate.resize_r: QtCore.Qt.SizeHorCursor,
                Item.Manipilate.resize_t: QtCore.Qt.SizeVerCursor,
                Item.Manipilate.resize_b: QtCore.Qt.SizeVerCursor,
                Item.Manipilate.resize_lt: QtCore.Qt.SizeFDiagCursor,
                Item.Manipilate.resize_rt: QtCore.Qt.SizeBDiagCursor,
                Item.Manipilate.resize_lb: QtCore.Qt.SizeBDiagCursor,
                Item.Manipilate.resize_rb: QtCore.Qt.SizeFDiagCursor,
            }[self.get_manipulation(pos)])
        elif self._mani == Item.Manipilate.move:
            self.move(self.mapToParent(pos - self._offset))
        elif self._mani == Item.Manipilate.resize_l:
            sub = pos - self._offset
            self.setGeometry(self._rect.x() + sub.x(), self._rect.y(), self._rect.width() - sub.x(), self._rect.height())
            self._rect = self.geometry()
        elif self._mani == Item.Manipilate.resize_r:
            sub = pos - self._offset
            self.setGeometry(self._rect.x(), self._rect.y(), self._rect.width() + sub.x(), self._rect.height())
        elif self._mani == Item.Manipilate.resize_t:
            sub = pos - self._offset
            self.setGeometry(self._rect.x(), self._rect.y() + sub.y(), self._rect.width(), self._rect.height()-sub.y())
            self._rect = self.geometry()
        elif self._mani == Item.Manipilate.resize_b:
            sub = pos - self._offset
            self.setGeometry(self._rect.x(), self._rect.y(), self._rect.width(), self._rect.height()+sub.y())
        elif self._mani == Item.Manipilate.resize_lt:
            sub = pos - self._offset
            self.setGeometry(self._rect.x() + sub.x(), self._rect.y()+ sub.y(), self._rect.width() - sub.x(), self._rect.height()-sub.y())
            self._rect = self.geometry()
        elif self._mani == Item.Manipilate.resize_rt:
            sub = pos - self._offset
            self.setGeometry(self._rect.x(), self._rect.y() + sub.y(), self._rect.width() + sub.x(), self._rect.height()-sub.y())
            #self._rect = self.geometry()
        elif self._mani == Item.Manipilate.resize_lb:
            sub = pos - self._offset
            self.setGeometry(self._rect.x() + sub.x(), self._rect.y(), self._rect.width() - sub.x(), self._rect.height()+sub.y())
            #self._rect = self.geometry()
        elif self._mani == Item.Manipilate.resize_rb:
            sub = pos - self._offset
            self.setGeometry(self._rect.x(), self._rect.y(), self._rect.width() + sub.x(), self._rect.height()+sub.y())
            #self._rect = self.geometry()
        
        self.update()

    def get_manipulation(self, pos):
        if pos.x() < 8 and pos.y() <8:
            return Item.Manipilate.resize_lt
        if pos.x() > (self.width() - 8) and pos.y() <8:
            return Item.Manipilate.resize_rt
        if pos.x() < 8 and pos.y() > (self.height() - 8) :
            return Item.Manipilate.resize_lb
        if pos.x() > (self.width() - 8) and pos.y() > (self.height() - 8):
            return Item.Manipilate.resize_rb
        if pos.x() < 8:
            return Item.Manipilate.resize_l
        if pos.x() > (self.width() - 8):
            return Item.Manipilate.resize_r
        if pos.y() < 8:
            return Item.Manipilate.resize_t
        if pos.y() > (self.height() - 8):
            return Item.Manipilate.resize_b
        else:
            return Item.Manipilate.move

class View(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._num = 0

        self.resize(640, 480)
        self.setWindowTitle('Resize and Move Item')
        
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenu)

    def contextMenu(self, point):
        menu = QtWidgets.QMenu(self)

        action = QtGui.QAction('Add', self)
        action.triggered.connect(self.add_item)
        menu.addAction(action)

        action = QtGui.QAction('Show', self)
        action.triggered.connect(self.info)
        menu.addAction(action)
        
        menu.exec_(self.mapToGlobal(point))

    def add_item(self):
        self._num+=1
        item = Item(f'item{self._num}', self)
        p1 = self.pos()
        p2 = QtGui.QCursor.pos()
        item.move(p2.x()-p1.x(), p2.y()-p1.y())

    def info(self):
        children = [ child for child in self.children() if child.__class__.__name__ == 'Item' ]
        print(children)

        for child in children:
            name = child.text()
            pos = child.pos()

            print(f'{name} pos:{pos.x()} {pos.y()}')
            print(child.geometry())
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = View()
    widget.show()
    app.exec()