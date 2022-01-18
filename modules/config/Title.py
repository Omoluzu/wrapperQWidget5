import warnings
from PyQt5.QtWidgets import QMainWindow, QGroupBox, QWidget


def set_title(self, value, parent):

    if issubclass(self.__class__.__bases__[0], QMainWindow):
        self.setWindowTitle(value)
    elif isinstance(parent, QGroupBox):
        parent.setTitle(value)
    elif issubclass(parent.__class__.__bases__[0], QWidget):
        parent.setWindowTitle(value)
    else:
        warnings.warn(f"Указан параметр title для непределенного параметра: parent={parent}, self={self}, title={value}")
