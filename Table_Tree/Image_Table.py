#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Table(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("显示图片大小的图片")
        self.resize(1000, 900)
        conLayout = QHBoxLayout()

        table = QTableWidget(5,3)
        table.setHorizontalHeaderLabels(["图片1","图片2","图片3"])
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setIconSize(QSize(300,200))

        for i in range(3):
            table.setColumnWidth(i,300)
        for i in range(5):
            table.setRowHeight(i,200)

        for k in range(15):
            i = k/3
            j = k%3
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled)# 用户点击时，图片被选中
            icon = QIcon(r'./images/bao%d.png' % k)
            item.setIcon(icon)

            print('e/icon/%d.png i= %d j= %d' % (k,i,j))
            table.setItem(i,j,item)
        conLayout.addWidget(table)
        self.setLayout(conLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Table()
    win.show()
    sys.exit(app.exec())