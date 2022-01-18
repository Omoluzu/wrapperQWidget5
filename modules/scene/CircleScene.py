from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsEllipseItem
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPixmap

from . import ElementScene

__version__ = "0.0.1"


class CircleScene(ElementScene, QGraphicsEllipseItem):
    diameter: int = 80

    def draw(self):
        """ Отрисовка элемнета """
        self.setRect(QRectF(
            -self.radius,
            -self.radius,
            self.diameter,
            self.diameter
        ))

    @property
    def start_point_x(self):
        return self.point[0] + (self.diameter * self.bias[0])

    @property
    def start_point_y(self):
        return self.point[0] + (self.diameter * self.bias[0])

    @property
    def radius(self):
        return self.diameter / 2

    def set_image(self, path, bias=(0, 0)):
        _pixmap = QGraphicsPixmapItem(QPixmap(path))
        self.scene.addItem(_pixmap)
        _pixmap.setPos(
            -self.radius,
            -self.radius
        )
