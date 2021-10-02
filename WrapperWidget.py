#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Обетка для QWidget, для построения элементов layout
"""

from functools import wraps
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import QRect

version = "0.1.2"


__all__ = ['wrapper_widget']


def wrapper_widget(foo):

    @wraps(foo)
    def wrapper(self, *args, **kwargs):
        foo(self, *args, **kwargs)

        if hasattr(self, 'config'):
            config_widget(self, self.config)

        format_layout(self, self.layouts)

    return wrapper


def format_layout(self, parameters, parent=None):
    """ """

    if isinstance(parameters, dict):
        for key, value in parameters.items():
            if key == "config":
                # config_widget(parent if parent else self, value)
                config_widget(parent, value)
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


def config_widget(self, config):
    """ Установка параметров для виджета и Layout"""
    if title := config.get('title'):
        self.setWindowTitle(title)

    if margin := config.get('margin'):
        if len(margin) == 1:
            self.setContentsMargins(margin[0], margin[0], margin[0], margin[0])
        elif len(margin) == 4:
            print(margin)
            self.setContentsMargins(margin[0], margin[1], margin[2], margin[3])
        else:
            print("Переданно нестандартное кол-во параметров ")

    if size := config.get('size'):
        self.setGeometry(QRect(400, 400, size[0], size[1]))
