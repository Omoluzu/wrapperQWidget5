import warnings

from PyQt5.QtWidgets import QTreeWidget


def set_column(self, value, parent=None):

    if self.__class__.__bases__[0] == QTreeWidget:
        for key, param in value.items():
            match key:
                case 'count':
                    set_column_count(self, param)
                case 'width':
                    ...
                case _:
                    ...
    else:
        warnings.warn(f"Параетр column указан для незарезервированного класса {self.__class__.__bases__[0]}")


def set_column_count(self, value):
    self.setColumnCount(value)

