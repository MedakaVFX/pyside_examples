"""
Info:
    * Coding : Python 3.7.9 & PySide6
    * Coding by : Tatsuya Yamagishi
    * Updated : 2023/02/27
    * Created : 2023/02/27

Reference From:
    * Getting a QTreeWidgetItem List again from QTreeWidget
        * https://stackoverflow.com/questions/9986231/getting-a-qtreewidgetitem-list-again-from-qtreewidget
"""
import sys

from PySide6 import QtCore, QtGui, QtWidgets

HEADERS = ('A', 'B', 'C')
HEADER_SIZES = (80, 80, 90)

items = [
    [True, False, True],
    [False, False, True],
    [True, True, False],
]


class MyTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setSortingEnabled(True)
        self.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.setAlternatingRowColors(True)
        self.setColumnCount(len(HEADERS))
        self.setHeaderLabels(HEADERS)
        self.setSelectionMode(self.ExtendedSelection)
        
        header = self.header()
        for i, value in enumerate(HEADER_SIZES):
            header.resizeSection(i, value)

        self.init_context_menu()

        self.refresh()

    def init_context_menu(self):
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.list_contex_menu)

    def list_contex_menu(self, point):
        menu = QtWidgets.QMenu(self)

        action = QtWidgets.QAction('Select A is True', self)
        action.triggered.connect(self.select_a_is_true)
        menu.addAction(action)

        menu.exec_(self.mapToGlobal(point))
    #--------------------------#
    # Get / Set
    #--------------------------#
    def get_subtree_nodes(self, tree_widget_item):
        """Returns all QTreeWidgetItems in the subtree rooted at the given node."""
        nodes = []
        nodes.append(tree_widget_item)
        for i in range(tree_widget_item.childCount()):
            nodes.extend(self.get_subtree_nodes(tree_widget_item.child(i)))
        return nodes


    def get_all_items(self):
        """Returns all QTreeWidgetItems in the given QTreeWidget."""
        all_items = []
        for i in range(self.topLevelItemCount()):
            top_item = self.topLevelItem(i)
            all_items.extend(self.get_subtree_nodes(top_item))
            
        return all_items
    
    # def get_all_items(self):
    #     """Returns all QTreeWidgetItems in the given QTreeWidget."""
    #     all_items = self.findItems(
    #         name, QtCore.Qt.MatchWrap |QtCore.Qt.MatchWildcard | QtCore.Qt.MatchRecursive,
    #     )
    #     return all_items
    
    #--------------------------#
    # Functions
    #--------------------------#
    
    def refresh(self):
        self.clear()

        for item in items:
            treewidget_item = QtWidgets.QTreeWidgetItem(self)
            treewidget_item.setText(0, str(item[0]))
            treewidget_item.setText(1, str(item[1]))
            treewidget_item.setText(2, str(item[2]))


    def select_a_is_true(self):
        all_items = self.get_all_items()
        print(all_items)

        for item in all_items:
            text = item.text(0)

            if text == 'True':
                item.setSelected(True)
            else:
                item.setSelected(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    view = MyTreeWidget()
    view.show()
    app.exec()