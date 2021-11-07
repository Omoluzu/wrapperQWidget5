#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Обетка для QWidget, для построения элементов layout
"""

import sys
from pathlib import Path

from functools import wraps
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton


__version__ = "0.1.4"
__all__ = ['wrapper_widget', 'config_widget']


file = Path(__file__).resolve()
sys.path.append(str(file.parents[1]))


def wrapper_widget(foo):

    @wraps(foo)
    def wrapper(self, *args, **kwargs):
        foo(self, *args, **kwargs)

        if hasattr(self, 'config'):
            config_widget(self, self.config)

        if hasattr(self, 'layouts'):
            format_layout(self, self.layouts)

    return wrapper


def format_layout(self, parameters, parent=None):
    """ """

    if isinstance(parameters, dict):
        for key, value in parameters.items():
            if key == "config":
                config_widget(self=parent, config=value, parent=self)
            else:
                if key == "vbox":
                    layout = QVBoxLayout()
                elif key == "hbox":
                    layout = QHBoxLayout()

                for param in value:
                    format_layout(self=self, parameters=param, parent=layout)

                if isinstance(parent, QVBoxLayout) or isinstance(parent, QHBoxLayout):
                    parent.addLayout(layout)
                else:
                    self.setLayout(layout)

    else:
        if isinstance(parameters, QGridLayout):
            parent.addLayout(parameters)
        else:
            parent.addWidget(parameters)


class Config:

    @staticmethod
    def flat(self, value):
        if issubclass(self.__class__.__bases__[0], QPushButton):
            self.setFlat(value)


def config_widget(self, config, parent=None):
    """ Установка параметров для виджета и Layout"""

    if alignment := config.get('alignment'):
        from modules.config import set_alignment
        set_alignment(self, alignment, parent)

    if flat := config.get('flat'):
        Config.flat(self, flat)

    if icon := config.get('icon'):
        from modules.config.Icon import set_icon
        set_icon(self, icon, parent, resource=config.get('resource', False))

    if margin := config.get('margin'):
        if len(margin) == 1:
            self.setContentsMargins(margin[0], margin[0], margin[0], margin[0])
        elif len(margin) == 4:
            self.setContentsMargins(margin[0], margin[1], margin[2], margin[3])
        else:
            print("Переданно нестандартное кол-во параметров ")

    if size := config.get('size'):
        from modules.config.Size import set_size
        set_size(self, size, parent)

    if title := config.get('title'):
        self.setWindowTitle(title)
