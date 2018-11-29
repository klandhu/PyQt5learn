#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we dispay an image
on the window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
from PyQt5.QtWidgets import (QWidget,QHBoxLayout,
                             QLabel,QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap= QPixmap('house.jpg') # 创建一个QPixmap对象，接收一个文件作为参数

        self.lbl = QLabel()
        self.lbl.setPixmap(pixmap)# 把QPixmap实例放到QLabel组件里。

        hbox.addWidget(self.lbl)
        self.setLayout(hbox)

        self.setGeometry(600,150,600,450)
        self.setWindowTitle('House')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex  = Example()
    sys.exit(app.exec_())