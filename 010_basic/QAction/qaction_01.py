""" カスタムQActionサンプル

* フォルダ構造でメニューを作成
* メニュー内のテキストファイルを表示

Info:
    Coding: Python 3.12.4 & PySide6
    Created : 2025-02-03 Tatsuya Yamagishi
    Updated : 2025-02-03 Tatsuya Yamagishi
"""
import os
import pathlib
import sys

from PySide6 import QtCore, QtGui, QtWidgets

try:
    from PySide6.QtGui import QAction
except:
    from PySide2.QtWidgets import QAction


CUR_DIR = os.path.dirname(os.path.abspath(__file__))+'/qaction_01'



class CustomAction(QAction):
    clicked = QtCore.Signal()

    def __init__(self, name: str, filepath: str, parent=None):
        super().__init__(name, parent)

        self.filepath: str = filepath
        self.triggered.connect(self.execute)


    def get_filepath(self) -> str:
        return self.filepath


    def execute(self):
        filepath = self.get_filepath()
        text = pathlib.Path(filepath).read_text()

        print(text)




class CustomListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)


    def on_context_menu(self, pos):
        menu = QtWidgets.QMenu()

        action = QAction('Action 1', self)
        action.triggered.connect(self.action1)
        menu.addAction(action)

        action = QAction('Action 2', self)
        action.triggered.connect(self.action2)
        menu.addAction(action)

        sub_menu = QtWidgets.QMenu('Menu from Directory', self)
        self.on_menu_from_directory(sub_menu)
        menu.addAction(sub_menu.menuAction())

        menu.exec(self.mapToGlobal(pos))


    def action1(self):
        print('Action 1')

    def action2(self):
        print('Action 2')


    def on_menu_from_directory(self, menu: QtWidgets.QMenu):
        preset_path = CUR_DIR
        self.create_menu(self, menu, preset_path)


    def create_menu(self, view: QtWidgets.QWidget, menu: QtWidgets.QMenu, filepath: str):
        """ フォルダ構造でメニューを作成(再起処理) """
        filepath = pathlib.Path(filepath)

        if filepath.exists():
            filelist = [_filepath for _filepath in filepath.iterdir() 
                            if not _filepath.name.startswith('.')]
        
            for _filepath in filelist:
                if _filepath.is_dir():
                    _new_menu = QtWidgets.QMenu(_filepath.stem, self)
                    _new_menu.setObjectName(_filepath.stem)
                    menu.addAction(_new_menu.menuAction())

                    self.create_menu(view, _new_menu, _filepath)
                
                else:
                    action = CustomAction(
                                    _filepath.name,
                                    _filepath.as_posix(),
                                    parent=self)
                    
                    menu.addAction(action)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = CustomListWidget()
    view.show()
    app.exec()