#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from PyQt5.QtWidgets import QApplication,QWidget,QToolTip
from PyQt5.QtGui import QFont
import sys

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))    #设置去泡提示的字体和字号
        self.setToolTip('<b style="color:red">这是一个气泡提示</b>') #创建提示语句
        self.setWindowTitle('气泡提示的Demo')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())