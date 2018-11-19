#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a tooltip on
a window and a button.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import ( QWidget, QApplication, QToolTip, QPushButton,)
from PyQt5.QtGui import QFont, QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建了一个提示框，设置了提示框的字体，我们使用了10px的SanSerif字体
        QToolTip.setFont(QFont('SansSerif',10))

        # 创建提示框可以使用富文本格式的内容
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建了一个按钮，并且为按钮添加了一个提示框
        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # 调整按钮的大小，并让按钮在屏幕上显示出来， sizeHint()方法提供了默认的按钮大小
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        # 对主窗口设置
        self.setGeometry(600,150, 600, 450)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QIcon('klandhu.jpg'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())