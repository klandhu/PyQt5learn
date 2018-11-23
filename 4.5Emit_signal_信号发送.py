#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we show how to
emit a custom signal.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QMainWindow,QApplication

class Communicate(QObject):
#Communicate类创建了一个pyqtSignal()属性的信号。
    closeApp = pyqtSignal()


class Example(QMainWindow):
    # 我们创建了一个叫closeApp的信号，这个信号会在鼠标按下的时候触发，事件与QMainWindow绑定。
    #
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # closeApp信号QMainWindow的close()方法绑定。
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        # 点击窗口的时候，发送closeApp信号，程序终止。
        self.c.closeApp.emit()

if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
