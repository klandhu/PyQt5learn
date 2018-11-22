#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we display the x and y
coordinates of a mouse pointer in a label widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个网格布局对象
        grid = QGridLayout()
        # 网格间距10px
        grid.setSpacing(1)

        x = 0
        y = 0

        # X Y坐标显示在QLabel组件里(初始状态)
        # 格式化绑定text
        self.text = "x:{0}, y:{1}".format(x,y)
        #
        self.label = QLabel(self.text)
        self.labe2 = QLabel(self.text,self)
        grid.addWidget(self.label,0,0,Qt.AlignBottom)
        grid.addWidget(self.labe2,0,0,Qt.AlignLeft)

        # 鼠标追踪默认没有开启，当有鼠标点击事件发生后才会开启
        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(300,300,350,200)
        self.setWindowTitle('Event Object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x:{0},y:{1}".format(x,y)
        self.label.setText(text)
        self.labe2.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
