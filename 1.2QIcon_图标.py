#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows an icon
in the titlebar of the window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__() # super()构造器方法返回父级的对象

        self.initUI()


    def initUI(self):
        # 这三个方法都继承自QWidget类。

        # 把窗口放到屏幕上并且设置窗口大小。参数分别代表屏幕坐标的x、y和窗口大小的宽、高。
        # 也就是说这个方法是resize()和move()的合体。
        self.setGeometry(600, 150, 600, 450)

        # 窗口添加了一个标题
        self.setWindowTitle('Icon')

        # 添加了图标，先创建一个QIcon对象，然后接受一个路径作为参数显示图标
        self.setWindowIcon(QIcon('klandhu.jpg'))

        self.show()


if __name__ == '__main__':
    # 创建一个应用对象  sys.argv是一组命令行参数的列表
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())