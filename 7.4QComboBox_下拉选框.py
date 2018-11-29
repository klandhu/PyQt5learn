#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows how to use
a QComboBox widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
QComboBox组件能让用户在多个选择项中选择一个。
"""
from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
         super().__init__()

         self.initUI()

    def  initUI(self):

         b 