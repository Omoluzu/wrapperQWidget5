from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsPolygonItem
from PyQt5.QtCore import QPointF, QSize
from PyQt5.QtGui import QPolygonF, QPixmap

from . import ElementScene

__version__ = "0.0.4"


class RectangleScene(ElementScene, QGraphicsPolygonItem):
    """
    Прямоугольник элемента сцены
    """
    height: int = 60  # высота прямоугольника
    width: int = 120  # Ширина прямоугольника

    def draw(self):
        indent_x = self.width / 2
        indent_y = self.height / 2

        self.setPolygon(
            QPolygonF(
                [
                    QPointF(self.start_point_x - indent_x, self.start_point_y + indent_y),
                    QPointF(self.start_point_x + indent_x, self.start_point_y + indent_y),
                    QPointF(self.start_point_x + indent_x, self.start_point_y - indent_y),
                    QPointF(self.start_point_x - indent_x, self.start_point_y - indent_y),
                ]
            )
        )

        self.scene.addItem(self)

    @property
    def start_point_x(self):
        return self.point[0] + (self.width * self.bias[0])

    @property
    def start_point_y(self):
        return self.point[1] + (self.height * self.bias[1])

    def set_image(self, path, bias=(0, 0), scaled=True, scaled_size=None):
        """

        update version 0.0.3:
            - Добавлен необязательный атрибут scaled.
        update version 0.0.4:
            - Добавлен необязательный атрибут scaled_size для указания новых размеров изображения.
        """
        pixmap = QPixmap(path)
        if scaled:
            if not scaled_size:
                pixmap = pixmap.scaled(QSize(int(self.width), int(self.height)))
            else:
                pixmap = pixmap.scaled(QSize(int(scaled_size[0]), int(scaled_size[1])))

        self._pixmap = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self._pixmap)
        self._pixmap.setPos(
            self.start_point_x - self.width / 2 + bias[0],
            self.start_point_y - self.height / 2 + bias[1]
        )
