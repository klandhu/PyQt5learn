#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program shows a confirmation
message box when we click on the close
button of the application window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import (QApplication, QToolTip,QPushButton,QWidget,QMessageBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>Qwidget</b> widget')


        qbtn = QPushButton('quit',self)
        qbtn.setToolTip('This is a <b>QPushButton</b> widget')

        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(600,150,600,450)
        self.setWindowTitle('Messages box')
        self.setWindowIcon(QIcon('klandhu.jpg'))
        self.show()
    # 如果关闭Qwidget，就会产生一个QcloseEvent。
    def closeEvent(self, event):

        # 创建了一个消息框对象，上面有两个按钮：Yes和No.第一个字符串显示在消息框的标题栏，
        # 第二个字符串显示在对话框，第三个参数是消息框的两个按钮，最后一个参数是默认按钮，
        # 这个按钮是默认选中的。返回值在变量。
        reply = QMessageBox.question(self,'Message',
                "Are you sure to quit?",QMessageBox.Yes |
                QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())