import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QBrush, QPainter
from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QMainWindow, QStyle, QStyleOptionGraphicsItem

class GanttChart(QGraphicsView):
    def __init__(self, parent=None):
        super(GanttChart, self).__init__(parent)

        # シーンを作成する
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # ガントチャートの幅と高さを設定する
        self.width = 800
        self.height = 600
        self.setFixedSize(self.width, self.height)

        # ガントチャートに表示するデータを設定する
        self.data = [
            {'name': 'Task 1', 'start': 0, 'end': 2},
            {'name': 'Task 2', 'start': 2, 'end': 4},
            {'name': 'Task 3', 'start': 4, 'end': 6},
            {'name': 'Task 4', 'start': 6, 'end': 8},
        ]

        # ガントチャートを描画する
        self.drawGanttChart()

    def drawGanttChart(self):
        # ガントチャートの各要素を描画する
        for i, task in enumerate(self.data):
            # タスクの長さを計算する
            length = task['end'] - task['start']

            # タスクの色を設定する
            color = QColor.fromHsl((i * 40) % 256, 255, 150)

            # タスクを描画する
            rect = self.scene.addRect(task['start'] * 100, 50 + i * 100, length * 100, 50)
            rect.setBrush(QBrush(color))
            rect.setPen(Qt.NoPen)

            # タスクの名前を描画する
            text = self.scene.addText(task['name'])
            text.setPos(task['start'] * 100 + 5, 60 + i * 100)


    def drawBackground(self, painter, rect):
        option = QStyleOptionGraphicsItem()
        option.rect = rect
        painter.setBrush(Qt.white)
        painter.drawRect(rect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chart = GanttChart()
    chart.show()
    app.exec()