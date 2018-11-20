#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a checkable menu.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import QApplication,QAction,QMainWindow

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
#本例创建了一个行为菜单。这个行为／动作能切换状态栏显示或者隐藏
    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')


        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')
        # 用checkable选项创建一个能选中的菜单。#异常退出QAction参数查没有checkable
        viewStatAct = QAction('View statusbar',self,checkable=True)
        # 使用checkable选项，我们创建了一个可选择菜单。
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(600,150,600,450)
        self.setWindowTitle('Check Menu')
        self.show()
    # 依赖于行为选中的状态，我们设置状态栏是否显示
    def toggleMenu(self):

         if state:
             self.statusBar.show()
         else:
             self.statusBar.hide()

if __name__ == '__main__':
    app =QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())