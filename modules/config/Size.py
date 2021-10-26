import warnings

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtGui import QIcon


def set_size(self, value, parent=None):
    if issubclass(self.__class__.__bases__[0], QPushButton):
        if isinstance(value, int):
            self.setFixedSize(QSize(value, value))
        else:
            if len(value) == 2:
                self.setFixedSize(QSize(value[0], value[1]))
            elif len(value) == 1:
                self.setFixedSize(QSize(value[0], value[0]))

    elif issubclass(self, QIcon):

        if issubclass(parent.__class__.__bases__[0], QPushButton):
            if isinstance(value, int):
                parent.setIconSize(QSize(value, value))
            else:
                warnings.warn(f"set_size. Данный параметр еще не реализован")
        else:
            warnings.warn(f"set_size. Данный параметр еще не реализован")

    else:
        warnings.warn(f"set_size. Тот параметр который ты ищешь он где то здесь.")
        self.setGeometry(QRect(400, 400, value[0], value[1]))
