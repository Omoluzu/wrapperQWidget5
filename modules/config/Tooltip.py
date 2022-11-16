import warnings


def set_tooltip(self, value, parent=None):
    """
    Description;
        Высплывающая подсказка

    new version 0.2.9  # Fixme
    """
    match self.__class__.__bases__[0].__name__:
        case 'QPushButton':
            self.setToolTip(value)
        case _:
            warnings.warn(f"Параметр header указан для незарезервированного класса {self.__class__.__bases__[0]}")