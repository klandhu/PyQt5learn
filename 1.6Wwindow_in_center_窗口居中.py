#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program centers a window
on the screen.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import (QApplication,QPushButton,QToolTip,QMessageBox,QWidget,QDesktopWidget)
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif'))
        self.setToolTip('This is a <b>QWidget</b> widget')

        bptn = QPushButton('quit',self)
        bptn.setToolTip('This is a <b>QPushbutton</b> widget')
        bptn.clicked.connect(QCoreApplication.instance().quit)
        bptn.resize(bptn.sizeHint())
        bptn.move(250,400)
        self.resize(600,450)
        self.move(50,50)
        self.center() # 调用窗体居中的函数

        #self.setGeometry(600, 150, 600, 450) #因为要居中，设置窗体大小位置的这个方法没有必要了
        self.setWindowTitle('center')
        self.setWindowIcon(QIcon('klandhu.jpg'))
        self.show()

    # QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小
    def center(self):
        qr = self.frameGeometry() # 得到主窗口的大小,qr是一个矩形和窗体一样的大小，但是不是窗体，窗体的移动坐标以左上角的位置定位的
        cp = QDesktopWidget().availableGeometry().center() # 获取显示器的分辨率，然后得到中间点的位置
        qr.moveCenter(cp) # 把自己窗口的中心点放置到qr的中心点
        self.move(qr.topLeft()) #把窗口左上角的坐标设置为qr的矩形左上角坐标，这样就把窗口居中了



    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self,'message','Are you sure to quit?',
                                     QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:# reply == QtGui.QMessageBox.Yes
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())