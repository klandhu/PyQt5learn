#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a quit
button. When we press the button,
the application terminates.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QToolTip)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
'''

class Example(QWidget):
    def __int__(self):
        super.__init__()

        self.initUI()

    

        self.initUI()

'''
class Example(QWidget):
    def __init__(self):
        # super()构造器方法返回父级的对象
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>Qwiddget</b> widget ')

        qbtn = QPushButton('Quit',self) # 这里的self是主窗口Qwiaget返回的对象

        # QCoreAppcation 包含了事件的主循环，它能添加和删除所有的事件，
        # instance()创建了一个它的实例。
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QPushbutton</b> widget')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(600,150,600,450)
        self.setWindowTitle('Quit button')
        self.setWindowIcon(QIcon('klandhu.jpg'))
        self.show()


if __name__== "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
