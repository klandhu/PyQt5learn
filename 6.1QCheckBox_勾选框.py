#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, a QCheckBox widget
is used to toggle the title of a window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        cb = QCheckBox('show Title',self)
        cb.move(20,20)
        # cb.setChecked(True)#切换成set这个也能达成效果 这个是初始化操作chceked为默认已勾选，
        # checkable 为是否勾选
        cb.toggle() # 切换，开关。开启切换信号也就是状态改变的事件这是一个slot，由界面点击触发，返回值None
        # 在Qt中，checkable按纽或是图标的槽函数应该用toggled()事件来激活，也是这个道理
        #  trigger更有触发的意思。这个单词还有另一个意思就是板机，枪械上用来发射子弹的那种。
        # 我们很容易想到板机是没有开/关两种状态的，不能说让它一直关上，一直发射子弹，
        # 至少在造词时并没有想到激光武器一说，我想如果针对激光武器，
        # 那么要fire的时候应该就不是扣trigger了，而是按toggle。在Qt中，
        # 一般的按纽（uncheckable）的激活方式即是triggered()。

        # stateChanged这个信号无返回值，但是传递给slot一个值state
        cb.stateChanged.connect(self.changeTitle)



        self.setGeometry(300,300,250,250)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self,state):
        # print(state) Qt的checked值给QT非图形的属性值 2，文字描述意义，换成2也可以，但是没有可读性
        if state == Qt.Checked:
            self.setWindowTitle('1QCheckBox')
            
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

