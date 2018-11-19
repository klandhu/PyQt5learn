#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a menubar. The
menubar has one menu with an exit action.

Author: Jan Bodnar
Website: zetcode.com
Last edited: January 2017
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp,QApplication
from PyQt5.QtGui import QIcon
import sys
# from PyQt5.QtWidgets import (QWidget,QApplication,QDesktopWidget,QPushButton,QToolTip,QMessageBox,QMainWindow)
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('klandhu.jpg'),'&Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        self.statusBar().showMessage('Ready')

        self.setGeometry(600,150,600,450)
        self.setWindowTitle('statusBar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())