#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows how to use
a QComboBox widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
QComboBox组件能让用户在多个选择项中选择一个。
"""
from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication)
import sys


class Example(QWidget):
# 本例包含了一个QComboBox和一个QLabel。
# 下拉选择框有五个选项，都是Linux的发行版名称，标签内容为选定的发行版名称。
    def __init__(self):
         super().__init__()

         self.initUI()

    def  initUI(self):

         self.lbl = QLabel("Ubuntu",self)

        # 创建一个QComboBox组件和五个选项。
         combo = QComboBox(self)
         combo.addItem("Ubuntu")
         combo.addItem("Mandriva")
         combo.addItem("Fedora")
         combo.addItem("Arch")
         combo.addItem("Gentoo")

         combo.move(50,50)
         self.lbl.move(50,150)

        # 在选中的条目上调用onActivated()方法。
         combo.activated[str].connect(self.onActived)

         self.setGeometry(300,300,300,200)
         self.setWindowTitle("QComboBox")
         self.show()

    def onActived(self,text):

        # 在方法内部，设置标签内容为选定的字符串，然后设置自适应文本大小。
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())