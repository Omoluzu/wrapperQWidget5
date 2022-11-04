#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Обетка для QWidget, для построения элементов layout
"""

import warnings

from functools import wraps
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QWidget, QGroupBox, QButtonGroup, \
    QSpacerItem

try:
    from modules.config import *
except ModuleNotFoundError:
    from .modules.config import *
except ImportError:
    from .modules.config import *


__version__ = "0.2.9"
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
    # print(f"{self=}", f"{parameters=}", f"{parent=}")

    if isinstance(parameters, dict):
        for key, value in parameters.items():
            match key:
                case "config":
                    config_widget(self=parent, config=value, parent=self)
                case "menu":
                    menu_bar(self, parameters)
                case _:
                    layout = None
                    match key:
                        case "vbox":
                            layout = QVBoxLayout()
                        case "hbox":
                            layout = QHBoxLayout()
                        case "group":
                            layout = QGroupBox()
                        # case "group_button":
                        #     group_button(key=key, value=value, self=self, parent=parent)
                        case _:
                            warnings.warn(f"Пришел незнакомый ключ {key}")
                            continue

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
                    elif issubclass(self.__class__.__bases__[0], QWidget) and layout:
                        self.setLayout(layout)
                    else:
                        warnings.warn(f"{self.__class__.__bases__[0]}, {parent=}: то с чем я еще не работаю")

    else:
        if isinstance(parameters, (QGridLayout, QHBoxLayout, QVBoxLayout)):
            parent.addLayout(parameters)
        elif isinstance(parameters, QSpacerItem):
            parent.addItem(parameters)
        else:
            parent.addWidget(parameters)


class Config:

    @staticmethod
    def flat(self, value):
        if issubclass(self.__class__.__bases__[0], QPushButton):
            self.setFlat(value)


def menu_bar(self: 'QMainWindow', parameters: dict):
    """
    Установка меню через WrapperWidget

    self = QMainWindow
    parameters = {'menu': <class '__main__.WrapperMenu'>}
    """
    self.menu = parameters['menu']()
    self.setMenuBar(self.menu)


# def group_button(key, value, self, parent):
#     print(f"{key=}")
#     print(f"{value=}")
#     print(f"{self=}")
#     print(f"{parent=}")
#
#     button_group = QButtonGroup()
#     button_group.buttonClicked[int].connect(value['action'])
#     for i, name_button in enumerate(value['items']):
#         button = QPushButton(name_button)
#         button_group.addButton(button, i)
#         parent.addWidget(button)


def config_widget(self, config, parent=None):
    """ Установка параметров для виджета и Layout"""

    if action := config.get('action'):
        set_action(self, action, parent)

    if alignment := config.get('alignment'):
        set_alignment(self, alignment, parent)

    if column := config.get('column'):
        set_column(self, column, parent)

    if header := config.get('header'):
        set_header(self, header, parent)

    if flat := config.get('flat'):
        Config.flat(self, flat)

    if icon := config.get('icon'):
        set_icon(self, icon, parent, resource=config.get('resource', False))

    if margin := config.get('margin'):
        if len(margin) == 1:
            self.setContentsMargins(margin[0], margin[0], margin[0], margin[0])
        elif len(margin) == 4:
            self.setContentsMargins(margin[0], margin[1], margin[2], margin[3])
        else:
            print("Переданно нестандартное кол-во параметров ")

    if size := config.get('size'):
        set_size(self, size, parent)

    if title := config.get('title'):
        set_title(self, title, parent)

