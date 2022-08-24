from .RectangleScene import RectangleScene

__version__ = "0.0.1"


class SquareScene(RectangleScene):
    size: int = 60  # Размер квадрата

    def __init__(self, *args, **kwarg):
        self.width = self.height = self.size
        super().__init__(*args, **kwarg)
