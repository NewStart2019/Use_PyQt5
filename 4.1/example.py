#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
#Qt5中窗口的控件基本都在PyQt5.QWidgets模块中

app = QApplication(sys.argv)  #每一pyqt5都需要一个QApplication对象，包含在QTWidgets魔怀忠
window = QWidget() #创建所有空间的父类，如果控件不指定一个父类的控件，他会被当成窗口处理
window.resize(300,200)
window.move(250,150)
window.setWindowTitle('hello pyqt5')
window.setWindowIcon(QIcon('zqh.jpg'))#为窗口添加图标
window.show()
sys.exit(app.exec())#确保程序完整的约束  pyqt4版本时候为了避免发生冲突，所以用了app。exec_()