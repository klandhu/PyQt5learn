#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In the example, we draw randomly 1000 red points
on the window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
我们在窗口里随机的画出了1000个点。
"""

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys, random

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,190)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        # 可以在子类中重新实现此事件处理程序，以接收在事件中传递的绘制事件。
        # 窗口改变都会产这个这个事件，
        qp = QPainter()# 生成一个画笔对象

        qp.begin(self)# 画笔开始，相当于画笔落在纸上，
        self.drawPoints(qp)# 将画笔即将完成的动作封装成一个函数，这个函数就像一个万花筒
        qp.end() #画笔结束，画笔离开纸上

    def drawPoints(self,qp):
        # 该自定义函数实现设置画笔属性如颜色
        # 设置笔的颜色为红色，使用的是预定义好的颜色。
        qp.setPen(Qt.red)
        # 每次更改窗口大小，都会产生绘画事件，从size()方法里获得当前窗口的大小，
        # 然后把产生的点随机的分配到窗口的所有位置上。
        size = self.size() # 画笔大小

        for i in range(1000):
            x = random.randint(1,size.width()-1) # 随机点的范围
            y = random.randint(1,size.height()-1)# 随机
            # drawPoint()方法绘图。
            qp.drawPoint(x,y)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())