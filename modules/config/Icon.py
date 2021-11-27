import warnings

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon


def set_icon(self, value, parent=None, resource=False):
    from WrapperWidget import config_widget

    if isinstance(value, dict):
        config_widget(QIcon, value, parent=self)

    elif parent:
        if issubclass(parent.__class__.__bases__[0], QPushButton):
            if resource:
                parent.setIcon(QIcon(f":/{value}"))
            else:
                parent.setIcon(QIcon(value))
        else:
            warnings.warn(f"set_icon. Данный параметр еще не реализован")
    else:
        warnings.warn(f"set_icon. Данный параметр еще не реализован")
