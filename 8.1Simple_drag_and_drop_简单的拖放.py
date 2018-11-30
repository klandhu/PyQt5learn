#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This is a simple drag and
drop example.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
拖拽

在GUI里，拖放是指用户点击一个虚拟的对象，拖动，然后放置到另外一个对象上面的动作。
一般情况下，需要调用很多动作和方法，创建很多变量。

拖放能让用户很直观的操作很复杂的逻辑。

一般情况下，我们可以拖放两种东西：数据和图形界面。
把一个图像从一个应用拖放到另外一个应用上的实质是操作二进制数据。
把一个表格从Firefox上拖放到另外一个位置 的实质是操作一个图形组。

简单的拖放
本例使用了QLineEdit和QPushButton。把一个文本从编辑框里拖到按钮上，更新按钮上的标签（文字）。
"""
from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit,QApplication)
import sys

class Button(QPushButton):
# 为了完成预定目标，我们要重构一些方法。首先用QPushButton上构造一个按钮实例。
    def __init__(self,title,parent):
        super().__init__(title,parent)

        # 激活组件的拖拽事件。
        self.setAcceptDrops(True)
        # 此属性保有是否接受拖放事件，来自于QWidget窗口的属性
        # 将此属性设置为true向系统宣布此小部件可能能够接受DROP事件
        # 默认情况下，此属性为false

    def dragEnterEvent(self, e):
        #同样是QWiaget的公共function，当拖动的动作开始并进入窗体时事件会被调用，并且事件传给参数
        # 首先，我们重构了dragEnterEvent()方法。设定好接受拖拽的数据类型（plain text）。
        if e.mimeData().hasFormat('text/plain'):
            #概念MIME：多用途互联网邮件扩展类型，是设定某种扩展名的文件用一种应用程序来打开的方式类型，当该扩展名文件被访问的时候，
            # 浏览器会自动使用指定应用程序来打开。多用于指定一些客户端自定义的文件名，
            # 以及一些媒体文件打开方式。MIME规定了用于表示各种各样的数据类型的符号化方法
            # MIME意为多功能Internet邮件扩展，它设计的最初目的是为了在发送电子邮件时附加多媒体数据，
            # 让邮件客户程序能根据其类型进行处理。然而当它被HTTP协议支持之后，它的意义就更为显著了。
            # 它使得HTTP传输的不仅是普通的文本，而变得丰富多彩。
            # 每个MIME类型由两部分组成，前面是数据的大类别，例如声音audio、图象image等，后面定义具体的种类。
            e.accept() # 设置事件对象的接受标志，等效于调用setAccepted(True)。
        else:
            e.ignore() # 不想要事件，就像个开关一样，针对想要的事件放行，不想要的事件丢弃
        print(e.mimeData().text())# 拖拽实现了传递文本内容
    # def dropEvent(self, e):
    #     # 然后重构dropEvent()方法，更改按钮接受鼠标的释放事件的默认行为。
    #     self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #QLineEdit默认支持拖拽操作，所以我们只要调用setDragEnabled()方法使用就行了。
        edit = QLineEdit('',self)
        edit.setDragEnabled(True)
        edit.move(30,65)

        # 继承自QPushbutton的新类
        button = Button('Button',self)
        button.move(190, 65)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Simple drag an drop')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

'''
常见的MIME类型(通用型)：
超文本标记语言文本 .html text/html
xml文档 .xml text/xml
XHTML文档 .xhtml application/xhtml+xml
######普通文本 .txt text/plain
RTF文本 .rtf application/rtf
PDF文档 .pdf application/pdf
Microsoft Word文件 .word application/msword
PNG图像 .png image/png
GIF图形 .gif image/gif
JPEG图形 .jpeg,.jpg image/jpeg
au声音文件 .au audio/basic
MIDI音乐文件 mid,.midi audio/midi,audio/x-midi
RealAudio音乐文件 .ra, .ram audio/x-pn-realaudio
MPEG文件 .mpg,.mpeg video/mpeg
AVI文件 .avi video/x-msvideo
GZIP文件 .gz application/x-gzip
TAR文件 .tar application/x-tar
任意的二进制数据 application/octet-stream
'''