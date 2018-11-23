#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we determine the event sender
object.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication

class Example(QMainWindow):
    # 我们创建了一个叫closeApp的信号，这个信号会在鼠标按下的时候触发，事件与QMainWindow绑定。
    # 我们调用sender()方法判断发送信号的信号源是哪一个。
    # 然后在应用的状态栏上显示被按下的按钮的标签内容
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30,50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150,50)
        # 两个按钮都和同一个slot绑定，所谓句柄handle就是处理函数，生涩的词汇
        # 鼠标点击后，信号发送给句柄也就槽slot也就是改GUI程序绑定的方法buttonclicked
        # 处理
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Event sender')
        self.show()

    # 我们用调用sender()方法的方式决定了事件源。状态栏显示了被点击的按钮
    def buttonClicked(self):
        # 存在疑问，sender是绑定给initUI的怎么判断是那个按钮的，是全局的，还是因为btn1出发事件，
        # 导致sender也改变了
        # sender = self.sender()
        self.statusBar().showMessage(self.sender().text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
