#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.

Author: Jan Bodnar
Website: zetcode.com
Last edited: January 2017
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber,QSlider,
                             QVBoxLayout,QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld =QSlider(Qt.Horizontal,self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        #我们将滑块条的valueChanged信号和lcd数字显示的display槽连接在一起。

发送者是一个发送了信号的对象。接受者是一个接受了信号的对象。槽是对信号做出反应的方法
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(600,150,600,450)
        self.setWindowTitle('Signal and slot')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())