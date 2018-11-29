#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a QProgressBar widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
'''
进度条是用来展示任务进度的（我也不想这样说话）。它的滚动能让用户了解到任务的进度。
QProgressBar组件提供了水平和垂直两种进度条，进度条可以设置最大值和最小值，
默认情况是0~99。
'''

from PyQt5.QtWidgets import (QWidget,QProgressBar,
                             QPushButton,QApplication)
from PyQt5.QtCore import QBasicTimer
import sys
# 我们创建了一个水平的进度条和一个按钮，这个按钮控制进度条的开始和停止。
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #进度条首先将self作为参数传递进去，否则在窗体上显示不出来（QPushbutton，QProgressBar）
        # 新建一个QProgressBar构造器。
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        self.btn = QPushButton('Start',self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.docAction)
        # The QBasicTimer class provides timer events for objects 计时器事件
        # 功能单一，需要一个截止时间和
        self.timer =QBasicTimer()
        self.step = 0

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('OProgressBar')
        self.show()

    def timerEvent(self,e):
# 每个QObject和又它继承而来的对象都有一个timerEvent()事件处理函数。为了触发事件，我们重载了这个方法。
        if self.step >= 100:

            self.timer.stop() #计时器停止
            self.btn.setText('Finished')
            return
        # 改写时间事件循环，并将时间和step联系在一起

        self.step = self.step + 1
        self.pbar.setValue(self.step) # 进度条的槽，传进去一个整数值

    def docAction(self):

        if self.timer.isActive():
            # 如果时间对象是激活状态，则时间停止，并将按钮文字改为开始
            self.timer.stop()
            self.btn.setText('Start')
        else: # 如果时间对象的状态不是激活，则将时间开启
            # 时间对象，开始和停止，自身是在计算的
            # 调用start()方法加载一个时间事件。这个方法有两个参数：过期时间和事件接收者。
            self.timer.start(100,self)#100毫秒超时启动或重启一个计时器，绑定对象将获得一个计时器事件
            self.btn.setText('Stop')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())