
import warnings

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

ALIGNMENT_VBOX = {
    "top": Qt.AlignTop,
    "bottom": Qt.AlignBottom,
    "center": Qt.AlignVCenter,
    "base_line": Qt.AlignBaseline
}


def set_alignment(self, value, parent):

    if isinstance(self, QVBoxLayout):
        if value in ALIGNMENT_VBOX.keys():
            self.setAlignment(ALIGNMENT_VBOX.get(value))
        else:
            warnings.warn(f"{parent.__class__.__name__}.vbox.alignment: Такого параметра не существует")

    elif isinstance(self, QHBoxLayout):
        warnings.warn(f"{parent.__class__.__name__}.hbox.alignment: Данный функционал еще не разработан")

    else:
        warnings.warn(f"{parent.__class__.__name__}: Вы ввели что то странное")
