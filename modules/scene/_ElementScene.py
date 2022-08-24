import os
import warnings

from abc import abstractmethod

__version__ = "0.0.2"


class ElementScene:
    type: str = 'ElementScene'
    scene: 'QGraphicsScene'  # Основная сцена
    image: str = None  # Путь до изображения. Если он есть то оно будет отрисованно
    _pixmap: 'QGraphicsPixmapItem' = None  # ...

    def __init__(self, scene=None, bias=(0, 0), point=(0, 0), *args, **kwargs):
        super().__init__()
        self.scene = scene
        self.point = point
        self.bias = bias

        self.draw()

        if self.image:
            if not os.path.exists(self.image):
                warnings.warn(f"Не найденн файл с изображением {self.image}")

            self.set_image(path=self.image)

    @abstractmethod
    def draw(self):
        """ Отрисовка элемнета """
        pass

    def set_image(self, path, bias=(0, 0)):
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

    def move_item(self, new_point, deactivated=True):
        self.remove_item()

        self.point = (
            new_point.start_point_x,
            new_point.start_point_y
        )
        self.bias = (0, 0)

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
