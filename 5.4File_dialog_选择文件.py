#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
from PyQt5.QtWidgets import (QMainWindow,QTextEdit,
                             QAction,QFileDialog,QApplication)
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):
    # 本例中有一个菜单栏，一个置中的文本编辑框，一个状态栏。
    # 点击菜单栏选项会弹出一个QtGui.QFileDialog对话框，在这个对话框里，你能选择文件，
    # 然后文件的内容就会显示在文本编辑框里。

    def __init__(self):
        super().__init__()

        self.initUI()
# 这里设置了一个文本编辑框，文本编辑框是基于QMainWindow组件的。
    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openfile = QAction(QIcon('klandhu.jpg'),'Open',self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('Open new file')
        openfile.triggered.connect(self.showDialog)

        pasttext = QAction(QIcon('klandhu.jpg'),'Past',self)
        pasttext.setShortcut('Ctrl+V')
        pasttext.setStatusTip('past text')

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(openfile)
        editmenu = menubar.addMenu('&Edit')

        editmenu.addAction(pasttext)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Open diaolog')
        self.show()

    def showDialog(self):
        # 弹出QFileDialog窗口。getOpenFileName()方法的第一个参数是说明文字，
        # 第二个参数是默认打开的文件夹路径。默认情况下显示所有类型的文件。
        # 返回的是一个元组(路径和所有文件（没有指定类型））
        #
        fname = QFileDialog.getOpenFileName(self,'open file','/home')
        if  fname[0]:
            f  = open(fname[0],'r')

            with f:# 不是所有文件读取后都可以填充到text中的
                data = f.read()# 当文件不可读，会报错

                self.textEdit.setText(data)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex  = Example()
    sys.exit(app.exec_())