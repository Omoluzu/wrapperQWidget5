import os
import time
import warnings

from abc import abstractmethod
from PyQt5.QtGui import QPen, QColor

__version__ = "0.0.3"


class ElementScene:
    """

    update version 0.0.2:
        - Вывод информационного сообщения если не найдено изображение по укаанному в self.image пути
    """
    type: str = 'ElementScene'
    scene: 'QGraphicsScene'  # Основная сцена
    image: str = None  # Путь до изображения. Если он есть то оно будет отрисованно
    _pixmap: 'QGraphicsPolygonItem' = None

    def __init__(self, scene=None, bias=(0, 0), point=(0, 0), *args, **kwargs):
        super().__init__()
        self.scene = scene
        self.point = point
        self.bias = bias

        self.draw()

        if self.image:
            if not os.path.exists(self.image) and not self.image.startswith(":/"):
                warnings.warn(f"Не найден файл с изображением {self.image}")

            self.set_image(path=self.image)

    @abstractmethod
    def draw(self):
        """ Отрисовка элемнета """
        pass

    def set_image(self, path, bias=(0, 0), scaled=True):
        """ Установка изображения на Элемент """
        pass

    @property
    def start_point_x(self):
        """ Центральная точка по оси X """
        return self.point[0]

    @property
    def start_point_y(self):
        """ Центральная точка по оси Y """
        return self.point[1]

    def remove_item(self):
        """ Удаление текущего элемента """
        if self._pixmap:
            self.scene.removeItem(self._pixmap)

        self.scene.removeItem(self)

    def move_item(self, new_point=None, new_bias=None, deactivated=True):
        """

        update version:
            - параметр new_point стал опциональным
            - Добавлен параметр new_bias. Для указание позиции новой позиции.
        """
        self.remove_item()

        self.point = (0, 0)
        self.bias = (0, 0)

        if new_point:
            self.point = (
                new_point.start_point_x,
                new_point.start_point_y
            )
        if new_bias:
            self.bias = new_bias

        self.draw()
        if self.image:
            self.set_image(path=self.image)

        if deactivated:
            self.deactivated()

    def mousePressEvent(self, event):
        """ Отработка нажатия мыши на текущий элемент """
        if self.scene.active == self:
            self.deactivated()
        else:
            self.activated()

    def activated(self):
        pass

    def deactivated(self):
        pass

    def set_border(self, color: str = 'Black', border: int = 1) -> None:
        """
        Description:
            Установка цвета и размера границ элемента

        Parameters:
            ::color (str) - цвет границы. По умолчанию черный
            ::border (int) - размер границы. По умолчанию 1

        init version 0.0.3
        """
        self.setPen(QPen(QColor(color), border))
