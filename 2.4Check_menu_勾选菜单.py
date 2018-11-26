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
from PyQt5.QtWidgets import  QMainWindow, QAction, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar =self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar',self,checkable=True)
        viewStatAct.setStatusTip('View statubar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu) #区分下triggered和troggle，troggled
        viewMenu.addAction(viewStatAct)
        # 在Qt中，checkable按纽或是图标的槽函数应该用toggled()事件来激活，也是这个道理
        #  trigger更有触发的意思。这个单词还有另一个意思就是板机，枪械上用来发射子弹的那种。
        # 我们很容易想到板机是没有开/关两种状态的，不能说让它一直关上，一直发射子弹，
        # 至少在造词时并没有想到激光武器一说，我想如果针对激光武器，
        # 那么要fire的时候应该就不是扣trigger了，而是按toggle。在Qt中，
        # 一般的按纽（uncheckable）的激活方式即是triggered()。

        self.setGeometry(600,150,600,450)
        self.setWindowTitle('Check Menu')
        self.show()

    def toggleMenu(self,state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex =  Example()
    sys.exit(app.exec_())
