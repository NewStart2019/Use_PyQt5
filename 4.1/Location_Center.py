#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
import PyQt5

class MainWidget(QMainWindow):

    def __init__(self,parent=None):
        super(MainWidget,self).__init__(parent)
        self.resize(400,200)
        self.status= self.statusBar() #获取状态栏对象
        self.status.showMessage('这是状态栏提示',5000)#5s是时间
        self.setWindowTitle('窗口中间显示，关闭主窗口')

        self.button1 = PyQt5.QtWidgets.QPushButton('关闭主窗口')
        self.button1.clicked.connect(self.onButtonClick)

        layout = PyQt5.QtWidgets.QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = PyQt5.QtWidgets.QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

        self.center()

    def center(self):
        screen = PyQt5.QtWidgets.QDesktopWidget().screenGeometry()#获取屏幕大小
        size = self.geometry()   #获取窗口大小
        self.move((screen.width()-size.width())//2,(screen.height()-size.height())//2)#设置窗口居中

    def onButtonClick(self):
        #sender 是发送信号的对象
        sender = self.sender()
        print(sender.text()+'被按下了！')
        qApp = PyQt5.QtWidgets.QApplication.instance()
        qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # path='cartoon1.ico'
    path='zqh.jpg'
    app.setWindowIcon(QIcon(path))
    form = MainWidget()
    form.show()
    sys.exit(app.exec_())

