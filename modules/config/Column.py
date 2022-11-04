import warnings

from PyQt5.QtWidgets import QTreeWidget


def set_column(self, value, parent=None):
    """
    Description;
        Реализация табличные элементов

    init version 0.2.6
    """

    if self.__class__.__bases__[0] == QTreeWidget:
        for key, param in value.items():
            match key:
                case 'count':  # Количество колонок
                    set_column_count(self, param)
                case 'width':  # Размер колонок
                    set_column_width(self, param)
                case _:
                    warnings.warn(f'set_column. \"{key}\" Данный параметр еще не реализован')
    else:
        warnings.warn(f"Параметр column указан для незарезервированного класса {self.__class__.__bases__[0]}")


def set_column_count(self, value):
    """
    Кол-во колонок

    init version 0.2.6
    """
    self.setColumnCount(value)


def set_column_width(self, value):
    """
    Размер колонок

    init version 0.2.6
    """
    for key, param in value.items():
        self.setColumnWidth(key, param)

