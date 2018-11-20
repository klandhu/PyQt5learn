#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a context menu.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,qApp,QMenu

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(600,150,600,450)
        self.setStatusTip('Content Menu')
        self.show()
    #还是使用contextMenuEvent()方法实现这个菜单。
    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction('New')
        opnAct = cmenu.addAction('Open')
        quitAct = cmenu.addAction('Quit')

        #使用exec_()方法显示菜单。从鼠标右键事件对象中获得当前坐标。
        # mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        # 如果右键菜单里触发了事件，也就触发了推出事件，我们就关闭菜单。
        if action == quitAct:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
