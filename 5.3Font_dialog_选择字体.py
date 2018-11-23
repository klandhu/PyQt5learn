#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we select a font name
and change the font of a label.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget,QVBoxLayout,QPushButton,
                             QSizePolicy,QLabel,QFontDialog,QApplication)
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        btn = QPushButton('Dialog',self)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        btn.move(20,20)
        btn.clicked.connect(self.showDialog)
        # btn.click.connect(self.showDialog())
        # AttributeError: 'builtin_function_or_method' object has no attribute 'connect'
        vbox.addWidget(btn)

        # lbl必须绑定，因为要在其他函数里调用
        self.lbl = QLabel('knowledge only matters',self)
        self.lbl.move(130,20)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300,300,250,180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        # PyQt5.QtGui.QFont object
        font,ok = QFontDialog.getFont()
        print(font)
        if ok:
            self.lbl.setFont(font)# 设置标签的字体

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

