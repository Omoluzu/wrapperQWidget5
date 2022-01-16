
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPolygonF, QPixmap

from . import ElementScene

import math


class HexagonScene(ElementScene):
    """
    Шестиугольный элемента сцены
    """
    type = 'HexagonScene'
    sides = 6  # Кол-во углов
    radius = 50  # Радиус внешнего круга

    def __init__(self, angle=0.0, radius=None, *args, **kwargs):
        """
        Initializes an hexagon of the given radius.
            parent - Родительский виджет
            bias - Смещение.
            point - Начальная точка позиционирования.
            angle - угол смещения вершин в радианах
        """
        self.angle = angle

        if radius:
            self.radius = radius

        super().__init__(*args, **kwargs)

    @property
    def start_point_x(self):
        """ Центральная точка по оси X """
        return self.point[0] + (self.radius * 2 * self.bias[0])

    @property
    def start_point_y(self):
        """ Центральная точка по оси Y """
        return self.point[1] + (self.radius * math.sin(self.angle + 2 * math.pi * 1 / self.sides) * 2 * self.bias[1]) * -1

    def draw(self):
        points = list()
        for s in range(self.sides):
            _angle = self.angle + 2 * math.pi * s / self.sides
            points.append(QPointF(
                self.start_point_x + self.radius * math.cos(_angle),
                self.start_point_y + self.radius * math.sin(_angle)
            ))

        self.setPolygon(QPolygonF(points))

    def set_image(self, path, bias=(0, 0)):
        """
        Установка изображения в нарисованный Шестиугольник

        :param path: - Путь до изображение
        :param bias: (x, y) - Смещение изображение относительно начальной точки
        :return:

        Начальная тоска текущего шестиугольника и начальная точка изображения отличаются координатами.
        """

        self.__pixmap = QGraphicsPixmapItem(QPixmap(path))
        self.scene.addItem(self.__pixmap)
        self.__pixmap.setPos(
            self.start_point_x - self.radius + bias[0],
            self.start_point_y - (self.radius * math.sin(self.angle + 2 * math.pi * 1 / self.sides)) + bias[1]
        )

