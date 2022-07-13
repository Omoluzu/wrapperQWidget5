import warnings
import os

from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtGui import QIcon


def set_icon(self, value, parent=None, resource=False):
    try:
        from WrapperWidget import config_widget
    except ModuleNotFoundError:
        from ...WrapperWidget import config_widget

    if isinstance(value, dict):
        config_widget(QIcon, value, parent=self if self else parent)

    elif parent:
        if not os.path.isfile(value) and not resource:
            warnings.warn(f"Не найдена иконка по указанному пути = {os.path.abspath(value)}")
        else:
            if issubclass(parent.__class__.__bases__[0], QPushButton):
                parent.setIcon(QIcon(f":/{value}" if resource else value))
            elif issubclass(parent.__class__.__bases__[0], QWidget):
                parent.setWindowIcon(QIcon(f":/{value}" if resource else value))
            else:
                warnings.warn(f"Указан параметр icon для непределенного параметра: {parent=}, {self=}, title={value}, {resource=}")
    else:
        warnings.warn(f"Указан параметр icon для непределенного параметра: {parent=}, {self=}, title={value}, {resource=}")
