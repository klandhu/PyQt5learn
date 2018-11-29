#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a QSlider widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
from PyQt5.QtWidgets import (QWidget,QSlider,
                             QLabel,QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #设置这是一个水平的滑块
        sld = QSlider(Qt.Horizontal,self)

        # setFocusPolicy是QWidget的方法，继承过来的
        # Qt.NoFocus默认的完全不接受焦点，TabFocus，ClickFocus，StrongFocus
        # 如果小部件处理键盘事件，则必须为其启用键盘焦点。
        # 这通常是通过小部件的构造函数完成的。
        # 例如，QLineEdit构造函数调用setFocusPolicy(QT：StrongFocus)。
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30,40,100,30)

        # 信号改为整数值连接槽changeValue
        # 滑块发信号并传值给槽
        sld.valueChanged[int].connect(self.changeValue)

        # QPixmap类用于绘图设备的图像显示，它可以作为一个QPainterDevice对象，
        # 也可以加载到一个控件中，通常是标签或者按钮，用于在标签或按钮上显示图像
        # QPixmap可以读取的图像文件类型有BMP，GIF，JPG等
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.jpg').scaled(30,30)) # QPixmap('mute.jpg')是一个对象，传递给setPixmap用
        self.label.setGeometry(160,40,30,30)

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self,value):
        # 将滑块的传参给changValue方法
        # 将滑块的整数值，也就是滑块的像素大小分成三部分
        if value == 0:
            self.label.setPixmap(QPixmap('mute.jpg').scaled(30,30)) # 图片缩放
        elif value >0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value > 30  and value <80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    '''
    小节：
        1、pixmap像素映射，用来给标签等窗体加上图片的类
        2、使用时依据具体路径生成对象
        3、标签窗体的setPixmap接受一个pix（尺寸设置好的）对象
        4、滑块依据自身长度发送信号并传递整数值，连接槽处理函数
        5、sld.setFocusPolicy(Qt.NoFocus)继承自QWid的方法设置键盘焦点方法
    '''