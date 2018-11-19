#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__=="__main__":
    app = QApplication(sys.argv) # 创建一个应用对象 sys.argv是一组命令行参数的列表

    # QWigdget控件是一个用户界面的基本控件，它提供了基本的应用程序构造器。
    # 默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（windows）。
    w = QWidget()

    # resize()方法能改变控件的大小，这里的意思是窗口宽250px，高150px
    w.resize(600,450)

    # move()是修改控件位置的方法。它把控件的放置到屏幕坐标（300， 300）的位置
    # 注：屏幕坐标系的原点是屏幕的左上角。
    w.move(600,300)

    # 我们给这个窗口添加了一个标题，标题在标题栏展示（虽然这看起来是一句废话，
    # 但是后面还有各种栏，还是要注意下，多了就蒙了）。
    w.setWindowTitle('Simple')

    # show()能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
    w.show()

    # 最后，我们进入了应用的的主循环中，事件处理器这个开始工作。主循环从窗口上接收事件，
    # 并把事件传入到派发到应用控件里。当调用exit()方法或者直接销毁控件时，主循环就会结束。
    # sys.exit()方法能确保主循环安全退出。外部环境能通知主循环控件怎么结束
    # exec_()之所以有个下划线，是因为exec是一个python的关键字。
    sys.exit(app.exec_())
