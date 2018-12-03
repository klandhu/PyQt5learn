
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program draws a Bézier curve with
QPainterPath.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
噩梦可以使用PyQt5的QPainterPath创建贝塞尔曲线。绘画路径是由许多构建图形的对象，
具体表现就是一些线的形状，比如矩形，椭圆，线和曲线。+


"""
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,380,250)
        self.setWindowTitle('Bezier curve')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self,qp):

        path = QPainterPath()
        path.moveTo(30,30)
        path.cubicTo(30,30,200,350,350,30)

        qp.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex  = Example()
    sys.exit(app.exec_())