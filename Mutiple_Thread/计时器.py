#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

sec = 0
min = 59
hour= 0
class WorkThread(QThread):

    trigger = pyqtSignal()
    def __init__(self):
        super(WorkThread,self).__init__()

    def run(self):
        # 耗时操作
        for i in range(2000000000):
            pass

        #循环完毕后发射信号
        self.trigger.emit()

def countTime():
    global sec,min,hour
    sec += 1
    if sec == 60:
        sec=0
        min += 1
    if min== 60:
        min = 0
        hour += 1
    if hour == 60:
        hour=0
    # LED 显示数字
    if sec<10:
        str1="0"+str(str(sec))
    else:
        str1=str(sec)
    if min<10:
        str2="0"+str(str(min))
    else:
        str2=str(min)
    if hour<10:
        str3="0"+str(str(hour))
    else:
        str3=str(hour)
    print(str3+':'+str2+':'+str1)
    LCDNUmber.display(str3+':'+str2+':'+str1)

def work():
    # 计时器每秒技术
    timer.start(1000)
    # 计数开始
    workThread.start()
    # 当获得循环完毕的信号时，停止计时
    workThread.trigger.connect(timeStop)

def timeStop():
    timer.stop()
    print("运行结束用时:",LCDNUmber.value())
    global sec
    sec = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    top =QWidget()
    top.resize(300,200)

    # 垂直布局类
    layout = QVBoxLayout(top)
    #添加一个显示板
    LCDNUmber = QLCDNumber()
    layout.addWidget(LCDNUmber)
    button= QPushButton("测试")
    layout.addWidget(button)

    timer = QTimer()
    workThread = WorkThread()

    button.clicked.connect(work)
    # 每次及时结束，触发countTime
    timer.timeout.connect(countTime)

    top.show()
    sys.exit(app.exec())