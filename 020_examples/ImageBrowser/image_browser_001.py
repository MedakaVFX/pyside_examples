"""Custom Image Label
Custom Image Label

Reference From :
Reincarnation+#Tech CustomLayoutを作ろう
https://fereria.github.io/reincarnation_tech/11_PySide/02_Tips/11_custom_layout/

Info:
    script_updated = 'JUN 15 2022'
    script_version = 'v2.0.0'
    script_name = 'TyIconWidet'
    script_coding = 'Tatsuya YAMAGISHI'
    script_tool_version = 'Python 3.7.9'
    script_created = 'JUN 15 2022'
    script_auther = '@2022 Tatsuya Yamagishi'
"""

import os
import sys

from PySide6 import QtCore, QtGui, QtWidgets

class TyImageLabel(QtWidgets.QWidget):


    def __init__(self, parent=None):
        super().__init__(parent)

        self._layout = QtWidgets.QVBoxLayout(self)

        # ImageLabel
        self._image_label = QtWidgets.QLabel(self)
        self._image_label.setText('Thumb')
        self._image_label.setAlignment(QtCore.Qt.AlignCenter)
        self._image_label.setAutoFillBackground(False)
        self._image_label.setFrameShape(QtWidgets.QFrame.Box)
        self._image_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self._image_label.setLineWidth(1)

        self._layout.addWidget(self._image_label)

        # Label
        self._label = QtWidgets.QLabel(self)
        self._label.setAlignment(QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._label)

        # Frame

        # ContextMenu
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenu)

        self.setLayout(self._layout)
    
    #-------------------------------------#
    # ContexMenu
    #-------------------------------------#
    def contextMenu(self, point):
        menu = QtWidgets.QMenu(self)
 
        action = QtWidgets.QAction('Menu1', self)
        action.triggered.connect(self.menu1)
        menu.addAction(action)

        menu.exec_(self.mapToGlobal(point))

    def menu1(self):
        print('Selected')

    #-------------------------------------#
    # カーソルイベント
    #-------------------------------------#
    def enterEvent(self, event):
        self._image_label.setLineWidth(3)

    def leaveEvent(self, event):
        self._image_label.setLineWidth(1)
    #-------------------------------------#
    # Set
    #-------------------------------------#
    def setName(self, name):
        self._label.setText(name)

    def setSize(self, w, h):
        size = QtCore.QSize(w, h)
        self._image_label.setMinimumSize(size)
        self._image_label.setMaximumSize(size)

    def setImage(self, path):
        if os.path.exists(path):
            name = os.path.basename(path)
            self.setName(name)
            image = QtGui.QImage(path)
            size = self._image_label.size()
            pixmap = QtGui.QPixmap(image.scaledToWidth(size.width(), mode=QtCore.Qt.SmoothTransformation))
            self._image_label.setPixmap(pixmap)


class TyFlowScrollWidegt(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TyFlowScrollWidegt, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.scroll = QtWidgets.QScrollArea(self)
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scroll.setWidget(self.scrollAreaWidgetContents)

        self.layout.addWidget(self.scroll)

        self.setLayout(self.layout)


class TyFlowLayout(QtWidgets.QLayout):
    def __init__(self, margin: int, hSpacing: int, vSpacing: int, parent=None):
        super(TyFlowLayout, self).__init__(parent=parent)
        self.setContentsMargins(margin, margin, margin, margin)
 
        self.itemList = []
        self.hSpacing = hSpacing
        self.vSpacing = vSpacing
 
    def addItem(self, item: QtWidgets.QLayoutItem):
 
        self.itemList.append(item)
 
    def count(self):
 
        return len(self.itemList)
 
    def itemAt(self, index: int):
 
        if self.count() > 0 and index < self.count():
            return self.itemList[index - 1]
        return None
 
    def takeAt(self, index):
 
        if index >= 0 and index < self.count():
            return self.itemList.pop(index - 1)
        return None
 
    # def expandingDirections(self):
    #     return Qt.Orientation.Vertical
 
    def hasHeightForWidth(self):
        return True
 
    def heightForWidth(self, width: int):
        height = self.doLayout(QtCore.QRect(0, 0, width, 0))
        return height
 
    def sizeHint(self):
        return self.minimumSize()
 
    def minimumSize(self):
 
        size = QtCore.QSize()
        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())
 
        margins = self.contentsMargins()
        size += QtCore.QSize(margins.left() + margins.right(), margins.top() + margins.bottom())
 
    def setGeomertry(self, rect):
        # 配置されるWidgetのジオメトリを計算するときに呼び出される
        super().setGeometry(rect)
        self.doLayout(rect)
 
    def doLayout(self, rect):
 
        # rect は、現在のLayoutの矩形
        x = rect.x()
        y = rect.y()
        lineHeight = 0
 
        for item in self.itemList:
            wid = item.widget()
            # 次のWidgetの配置場所
            nextX = x + item.sizeHint().width() + self.hSpacing
            if nextX - self.hSpacing > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + self.vSpacing
                nextX = x + item.sizeHint().width() + self.hSpacing
                lineHeight = 0
 
            item.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))
            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())
 
        return y + lineHeight - rect.y()

class SampleUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SampleUI, self).__init__(parent)
 
        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.widget = TyFlowScrollWidegt(self)
        self.layout.addWidget(self.widget)
 
        self.flowlayout = TyFlowLayout(3, 5, 5)
        widget = self.widget.scroll.widget()
        widget.setLayout(self.flowlayout)
 
        for i in range(20):
            btn = TyImageLabel(self)
            btn.setName(f"Version {i}")
            btn.setSize(100, 50)
            self.flowlayout.addWidget(btn)

        self.setLayout(self.layout)
        self.resize(400, 200)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # QtWidgets.QApplication.setFallbackSessionManagementEnabled(True)
    a = SampleUI()
    a.show()
    sys.exit(app.exec())