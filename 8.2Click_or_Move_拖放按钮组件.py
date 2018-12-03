#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this program, we can press on a button with a left mouse
click or drag and drop the button with  the right mouse click.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
from PyQt5.QtWidgets import QPushButton,QWidget,QApplication
from PyQt5.QtCore import Qt,QMimeData
from PyQt5.QtGui import QDrag
import sys

class Button(QPushButton):
# 这个例子展示怎么拖放一个button组件。
    def __init__(self,title,parent):
        super().__init__(title,parent)

# 上面的例子中，窗口上有一个QPushButton组件。左键点击按钮，控制台就会输出press。
# 右键可以点击然后拖动按钮。
    def mouseMoveEvent(self, e):
# 从QPushButton继承一个Button类，然后重构QPushButton的两个方法:
# mouseMoveEvent()和mousePressEvent().mouseMoveEvent()是拖拽开始的事件。
        if e.buttons() != Qt.RightButton:
            return
# 创建一个QDrag对象，用来传输MIME-based数据。
        mimeData = QMimeData()

        drag = QDrag(self)

        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):

        super().mousePressEvent(e)
# 我们只劫持按钮的右键事件，左键的操作还是默认行为。
        if e.button() ==Qt.LeftButton:
            print('press')

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setAcceptDrops(True)

        self.button = Button('Button',self)
        self.button.move(100,65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300,300,280,150)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self,e):

        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
