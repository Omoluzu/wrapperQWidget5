import warnings


def set_action(self, value, parent=None):
    """
    Description;
        Реализация активация элементов

    init version 0.2.6
    """

    match self.__class__.__bases__[0].__name__:
        case 'QPushButton':
            self.clicked.connect(value)
        case _:
            warnings.warn(f"Параметр \"action\" указан для незарезервированного класса {self.__class__.__bases__[0]}")