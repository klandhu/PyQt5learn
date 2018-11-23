#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we select a color value
from the QColorDialog and change the background
color of a QFrame widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import (QWidget,QPushButton,QFrame,
                             QColorDialog,QApplication)
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
# 例子里有一个按钮和一个QFrame，默认的背景颜色为黑色，我们可以使用QColorDialog改变背景颜色
    def initUI(self):
        # 初始化QtGui.QFrame的背景颜色。PyQt5.QtGui object
        col = QColor(255,255,255)# PyQt5.QtGUi.Qcolor对象（颜色已定）
        print(col)
        btn = QPushButton('Dialog',self)
        btn.move(20,20)
        # btn点击后产生事件connect槽showDialog
        btn.clicked.connect(self.showDialog)
        # 绑定一个框架属性fram,
        self.frm = QFrame(self)
        # 框架样式的固定格式背景颜色类似于HTML样式
        self.frm.setStyleSheet("QWidget { background-color:%s}"
                               % col.name())#col.name表示的是PyQt5.QtGUi.Qcolor对象的颜色6位十六进制表示#ffffff
        self.frm.setGeometry(130,22,100,100)
        
        self.setGeometry(300,300,250,180)
        self.setWindowTitle('Color dialog')
        self.show()
        

    def showDialog(self):
        # 将col重新指向颜色对话框并获取选定的颜色对象
        col = QColorDialog.getColor() # 返回一个PyQt5.QtGUi.Qcolor对象（颜色已定）
        print(col)
        print(col.isValid())
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color:%s}"
                                   % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())