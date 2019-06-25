#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class MainWidget(QWidget):

    def __init__(self,parent=None):
        super(MainWidget,self).__init__(parent)
        self.setWindowTitle("QThread 例子")
        self.thread = Worker()
        self.thread.sinOut.connect(self.slotAdd)

        self.listfile = QListWidget()

        self.btnStart= QPushButton("开始")
        self.btnStart.clicked.connect(self.slotStart)

        layout = QGridLayout(self)
        layout.addWidget(self.listfile,0,0,1,2)
        layout.addWidget(self.btnStart,1,1)

    def slotAdd(self,file_inf):
        self.listfile.addItem(file_inf)

    def slotStart(self):
        self.btnStart.setEnabled(False)
        self.thread.start()

class Worker(QThread):
    sinOut = pyqtSignal(str)
    def __init__(self,parent=None):
        super(Worker,self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while self.working == True:
            file_str = "File index {0}".format(self.num)
            self.num += 1
            #发射信号
            self.sinOut.emit(file_str)
            #线程休眠两秒
            self.sleep(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWidget()
    demo.show()
    sys.exit(app.exec())