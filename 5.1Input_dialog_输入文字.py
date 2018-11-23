#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we receive data from
a QInputDialog dialog.

Aauthor: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import (QWidget,QPushButton,QLineEdit,
                             QInputDialog,QApplication)
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 这个示例有一个按钮和一个输入框，点击按钮显示对话框，输入的文本会显示在输入框里。
        self.btn = QPushButton('Dialog',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        # 这是显示一个输入框的代码。第一个参数是输入框的标题，第二个参数是输入框的占位符。
        # 对话框返回输入内容和一个布尔值，如果点击的是OK按钮，布尔值就返回True。
        # ok 只是点击ok按钮的返回的布尔值，判断执行下列调用文本的动作
        text, ok =  QInputDialog.getText(self,'Input Dialog',
                                         'Enter your name:')

        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())