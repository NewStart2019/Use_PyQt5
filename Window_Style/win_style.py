#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.resize(400,200)
        self.setWindowTitle("设置窗口样式例子")
        # 设置无窗口边框样式
        self.setWindowFlags(Qt.FramelessWindowHint)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())