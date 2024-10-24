"""Custom QListWidget Example

ファイルをドラッグ＆ドロップして表示

Info:
    * Updated: 2022/09/05
    * Created: 2022/08/29
    * Coding: Python 3.7.9 & PySide6(Qt5)
    * Coding by: Tatsuya YAMAGISHI
"""

import os
import re
import sys

from PySide6 import QtCore, QtGui, QtWidgets

class FileListWidgetItem(QtWidgets.QListWidgetItem):
    def __init__(self, file, parent=None) -> None:
        super().__init__(parent)   

        self.file = file

        self.setText(os.path.basename(file))

    def get(self):
        return self.file
    
    def test(self):
        parent = self.parent()
        print(parent)


class FileListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        
        self.setAcceptDrops(True)
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(
                QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)

        self.init_context_menu()


    def init_context_menu(self):
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.set_context_menu)


    def set_context_menu(self, point):
        menu = QtWidgets.QMenu(self)

        action = QtGui.QAction('Activate', self)
        action.triggered.connect(self.activate_items)
        menu.addAction(action)

        action = QtGui.QAction('Deleate All', self)
        action.triggered.connect(self.clear)
        menu.addAction(action)

        action = QtGui.QAction('Delete Selection', self)
        action.triggered.connect(self.delete_items)
        menu.addAction(action)

        menu.exec_(self.mapToGlobal(point))
    
    #================================================#
    # Drag & Drop
    #================================================#
    def dragEnterEvent(self, event):
        mimedata = event.mimeData()

        if mimedata.hasUrls() == True:
            event.accept()
        else:
            event.ignore()


    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()


    def dropEvent( self, event ):
        mimedata = event.mimeData()
 
        if mimedata.hasUrls():
            urllist = mimedata.urls()
            files = [ re.sub('^/', '', url.path()) for url in urllist ]
       
            self.set_items(files)
    
   
    #================================================#
    # Set / Get
    #================================================#
    def get_current_files(self):
        return [item.get() for item in self.selectedItems()]

    def set_items(self, files: list):
        items = [FileListWidgetItem(file, self) for file in files]


    #================================================#
    # Event
    #================================================#
    def delete_items(self):
        items = self.selectedItems()

        for item in items:
            row = self.row(item)
            self.takeItem(row)


    def activate_items(self):
        cur_files = self.get_current_files()

        print(cur_files)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = FileListWidget()
    view.show()
    app.exec()