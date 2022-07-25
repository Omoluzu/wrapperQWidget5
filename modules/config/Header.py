import warnings


def set_header(self, value, parent=None):
    """
    Description;
        Реализация Элемента Headers

    init version 0.2.6
    """
    match self.__class__.__bases__[0].__name__:
        case 'QTreeWidget':
            set_header_q_tree_widget(self, value)
        case _:
            warnings.warn(f"Параметр header указан для незарезервированного класса {self.__class__.__bases__[0]}")


def set_header_q_tree_widget(self, value):
    """
    Description;
        Реализация Элемента Headers для QTreeWidget

    init version 0.2.6
    """
    for key, param in value.items():
        match key:
            case 'hidden':  # Сокрытие элемента.
                self.setHeaderHidden(param)
            case _:
                warnings.warn(f'set_header. \"{key}\" Данный параметр для \"QTreeWidget\" еще не реализован')


