from PyQt5.QtWidgets import QGraphicsPolygonItem, QGraphicsPixmapItem
from abc import abstractmethod

__version__ = "0.0.1"


class ElementScene(QGraphicsPolygonItem):
    type: str = 'ElementScene'
    scene: 'QGraphicsScene'  # Основная сцена
    image: str = None  # Путь до изображения. Если он есть то оно будет отрисованно
    _pixmap: QGraphicsPixmapItem = None  # ...

    def __init__(self, scene=None, bias=(0, 0), point=(0, 0)):
        super().__init__()
        self.scene = scene
        self.point = point
        self.bias = bias

        self.draw()

        if self.image:
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

    def mousePressEvent(self, event):
        """ Отработка нажатия мыши на текущий элемент """
        pass