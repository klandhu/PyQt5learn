#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows
how to use QSplitter widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
QSplitter组件能让用户通过拖拽分割线的方式改变子窗口大小的组件。
本例中我们展示用两个分割线隔开的三个QFrame组件。
"""

from PyQt5.QtWidgets import (QWidget,QHBoxLayout,QFrame,
                             QSplitter,QStyleFactory,QApplication)
from PyQt5.QtCore import Qt
import sys
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

         hbox = QHBoxLayout(self)

        # 为了更清楚的看到分割线，我们使用了设置好的子窗口样式。
         topleft = QFrame(self)
         topleft.setFrameShape(QFrame.StyledPanel)

         topright = QFrame(self)
         topright.setFrameShape(QFrame.StyledPanel)

         bottom = QFrame(self)
         bottom.setFrameShape(QFrame.StyledPanel)

        # 创建一个QSplitter组件，并在里面添加了两个框架。
         splitter1 = QSplitter(Qt.Horizontal) # 分割水平框架
         splitter1.addWidget(topleft)
         splitter1.addWidget(topright)

         # 也可以在分割线里面再进行分割。
         splitter2 =QSplitter(Qt.Vertical) # 分割垂直框架
         splitter2.addWidget(splitter1) # 将水平分割提潜入垂直框架，
         splitter2.addWidget(bottom)# 将底部框架加入垂直框架

         hbox.addWidget(splitter2)
         self.setLayout(hbox)

         self.setGeometry(300,300,300,200)
         self.setWindowTitle('QSplitter')
         self.show()

    def  onChanged(self,text):

        self.lbl.setTex(text)
        self.lbl.adjustSize() # 实现自动设置尺寸
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())