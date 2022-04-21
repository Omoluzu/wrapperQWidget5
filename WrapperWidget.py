#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Обетка для QWidget, для построения элементов layout
"""

import warnings

from functools import wraps
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QWidget, QGroupBox

try:
    from modules.config import *
except ModuleNotFoundError:
    from .modules.config import *


__version__ = "0.2.4"
__all__ = ['wrapper_widget', 'config_widget']


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
                layout = None
                if key == "vbox":
                    layout = QVBoxLayout()
                elif key == "hbox":
                    layout = QHBoxLayout()
                elif key == "group":
                    layout = QGroupBox()

                if isinstance(value, list):
                    for param in value:
                        format_layout(self=self, parameters=param, parent=layout)
                else:
                    if isinstance(layout, (QHBoxLayout, QVBoxLayout)):
                        warnings.warn(f"{layout}: неправильный тип данных: {type(value)}, != list")

                if isinstance(layout, QGroupBox):
                    format_layout(self=layout, parameters=parameters['group'], parent=self)
                    parent.addWidget(layout)
                elif isinstance(parent, (QHBoxLayout, QVBoxLayout)):
                    parent.addLayout(layout)
                elif isinstance(parent, QGroupBox):
                    format_layout(self=self, parameters=parameters, parent=layout)
                elif issubclass(self.__class__.__bases__[0], QWidget):
                    self.setLayout(layout)
                else:
                    warnings.warn(f"{self.__class__.__bases__[0]}, {parent}: то с чем я еще не работаю")

    else:
        if isinstance(parameters, (QGridLayout, QHBoxLayout, QVBoxLayout)):
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
        # from modules.config import set_alignment
        set_alignment(self, alignment, parent)

    if flat := config.get('flat'):
        Config.flat(self, flat)

    if icon := config.get('icon'):
        # from modules.config.Icon import set_icon
        set_icon(self, icon, parent, resource=config.get('resource', False))

    if margin := config.get('margin'):
        if len(margin) == 1:
            self.setContentsMargins(margin[0], margin[0], margin[0], margin[0])
        elif len(margin) == 4:
            self.setContentsMargins(margin[0], margin[1], margin[2], margin[3])
        else:
            print("Переданно нестандартное кол-во параметров ")

    if size := config.get('size'):
        # from modules.config.Size import set_size
        set_size(self, size, parent)

    if title := config.get('title'):
        # from modules.config.Title import set_title
        set_title(self, title, parent)
