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
    # QMainWindow提供了主窗口的功能，使用它能创建一些简单的状态栏、工具栏和菜单栏
    def __init__(self):
        super().__init__()#  super()构造器方法返回父级的对象即QMainWindow类的对象

        self.initUI()

    def initUI(self):
        # 调用QtGui.QMainWindow类的statusBar()方法，创建状态栏。第一次调用创建一个状态栏，
        # 返回一个状态栏对象。showMessage()方法在状态栏上显示一条信息
        self.statusBar().showMessage('Ready')# 状态栏是由QMainWindow创建的所以要绑定self

        #例行设置窗体参数
        self.setGeometry(600,150,600,450)
        self.setWindowTitle('statusBar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())