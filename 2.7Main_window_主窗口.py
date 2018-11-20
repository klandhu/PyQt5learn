#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar, and a central widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,qApp,QMenu,QAction,QTextEdit
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建了一个很经典的菜单框架，有右键菜单，工具栏和状态栏。

        # 这里创建了一个文本编辑区域，并把它放在QMainWindow的中间区域。
        # 这个组件或占满所有剩余的区域。

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('klandhu.jpg'),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(600,150,600,450)
        self.setWindowTitle('Main window')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
