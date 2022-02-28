
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QDesktopWidget
from PyQt5.QtCore import QRect

__version__ = "0.0.1"


class Scene(QGraphicsScene):
    draw_sketch = False

    def __init__(self, widget, size=(0, 0)):
        super().__init__(widget)
        self.active = None

        self.board = QGraphicsView(widget)
        if size == (0, 0):
            self.board.setGeometry(QDesktopWidget().screenGeometry())
        else:
            self.board.setGeometry(QRect(0, 0, *size))

        self.board.setScene(self)

        if self.draw_sketch:
            self.sketch()
        self.draw()

    def draw(self):
        pass

    def sketch(self):
        pass
