#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a submenu.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QMenu,qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        '''
        QAction和Qmenu区别，两者可以显示在同一下拉菜单中，
        但是前者为命令点击执行，后者子菜单拉出新的子列
        :return:
        '''
        exitAct = QAction(QIcon('klandhu.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar() #生成菜单栏按钮最高，下属事件和子菜单绑定对象
        fileMenu = menubar.addMenu('&File')# &是助记码。在在窗口获得焦点时，按下alt键，
        # 你会看到有的按钮或菜单某个字母下面出现一个下划线，这就是助记码。助记码方便你用键盘操作界面。
        fileMenu.addAction(exitAct)

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self) #性质为事件

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(600, 150, 600, 450)
        self.setWindowTitle('statusBar')
        self.show()
        #Qmenu,QAction生成对象，addmenu和addAction绑定父级对象

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())