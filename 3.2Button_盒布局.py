#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we position two push
buttons in the bottom-right corner
of the window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout,QVBoxLayout,QApplication)

class Example(QWidget):
#完成了在应用的右下角放了两个按钮的需求。当改变窗口大小的时候，它们能依然保持在相对的位置。
# 我们同时使用了QHBoxLayout和QVBoxLayout。
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        # 创建一个水平布局，增加两个按钮和弹性空间。stretch函数在两个按钮前面增加了一些弹性空间。
        # 下一步我们把这些元素放在应用的右下角。
        hbox = QHBoxLayout()
        hbox.addStretch(0)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(0)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(600,150,600,450)
        self.setWindowTitle('Button')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())