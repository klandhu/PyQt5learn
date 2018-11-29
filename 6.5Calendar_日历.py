#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a QCalendarWidget widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
from PyQt5.QtWidgets import (QWidget,QCalendarWidget,QLabel,QApplication,QVBoxLayout)
from PyQt5.QtCore import QDate
import sys

class Example(QWidget):
# 这个例子有日期组件和标签组件组成，标签显示被选中的日期。
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)# 创建一个QCalendarWidget。
        cal.setGridVisible(True)# 设置日历的栅栏可见
        cal.clicked[QDate].connect(self.showDate)# 日历点击发送日期数据

        vbox.addWidget(cal) # 将日历添加进垂直布局

        self.lbl = QLabel(self) #设置标签
        date = cal.selectedDate() # 日历获取日期
        self.lbl.setText(date.toString()) # 标签独的文本设置位字符串格式的日期

        vbox.addWidget(self.lbl) #将标签添加进垂直布局控件

        self.setLayout(vbox) # 设置布局
        # 例行窗体参数设置
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self,date):#接受鼠标点击发来的日期参数，并实现标签的文本替换位字符串格式的日期
        self.lbl.setText(date.toString())

if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
