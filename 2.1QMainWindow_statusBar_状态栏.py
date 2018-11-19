#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a statusbar.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
'''
QT中QWidget、QDialog及QMainWindow的区别
1\QWidget类是所有用户界面对象的基类，QMainWindow和QDialog都是QWidget的子类。窗口部件是用户界面的一个基本单元
2\QMainWindow 类提供一个有菜单条、锚接窗口（例如工具条）和一个状态条的主应用程序窗口
3\QDialog类是对话框窗口的基类。对话框窗口是主要用于短期任务以及和用户进行简要通讯的顶级窗口
'''
import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QDesktopWidget,QPushButton,QToolTip,QMessageBox,QMainWindow)
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(600,150,600,450)
        self.setWindowTitle('statusBar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())