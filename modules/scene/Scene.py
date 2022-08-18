
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QDesktopWidget
from PyQt5.QtCore import QRect

__version__ = "0.0.2"


class Scene(QGraphicsScene):
    draw_sketch = False

    def __init__(self, app, size=(0, 0)):
        """

        init version 0.0.1
        update version 0.0.2
            - Входящий параметр сменен с widget на app
        """
        super().__init__(app.widget)

        self.app = app
        self.active = None
        self.board = QGraphicsView(app.widget)

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

