#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create three toggle buttons.
They will control the background color of a
QFrame.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget,QPushButton,
                             QFrame,QApplication)
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):
    # 我们创建了一个切换按钮和一个QWidget，并把QWidget的背景设置为黑色。
    # 点击不同的切换按钮，背景色会在红、绿、蓝之间切换（而且能看到颜色合成的效果，
    # 而不是单纯的颜色覆盖）。
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 初始化颜色为黑色
        self.col = QColor(0,0,0)

        # 设置红，绿，蓝三色按钮
        redb = QPushButton('Red',self)
        # 设置按钮为可选状态，即按下和未按下两种状态，
        # 创建一个QPushButton，然后调用它的setCheckable()的方法就把这个按钮编程了切换按钮。
        redb.setCheckable(True)
        redb.move(10,10)
        # 只有两种状态
        # 把点击信号和我们定义好的函数关联起来，这里是把点击事件转换成布尔值。
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green',self)
        greenb.setCheckable(True)
        greenb.move(10,60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue',self)
        blueb.setCheckable(True)
        blueb.move(10,110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget { background-color: %s}" % self.col.name())

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self,press):
        # 获取被点击的按钮。将获取的对象赋值给source
        source = self.sender()
        print(source)
        print(state)
        # source 和press
        if press:
            val = 255
        else:val= 0
    # 6.1勾选框只一个，无需分辨是哪一个发送的事件，而本例中颜色的三个按钮需要甄别，一一对应各自的选项
        if source.text() == 'Red':# 被点击按钮的文本是RED，条件甄选一
            self.col.setRed(val)# 设置颜色的RGB值中RED为255
        elif source.text() == 'Green':# 被点击按钮的文本是GREEN，条件甄选二
            self.col.setGreen(val)
        elif source.text() == 'Blue':
            self.col.setBlue(val)

        self.square.setStyleSheet("QWidget { background-color:%s}" % self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())