#!/usr/bin/env python
# _*_ coding:utf-8 _*_   #避免中文乱码

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QToolTip
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText('button')
#以 QWidget 左上角(0,0)点
btn.move(20,20)

QToolTip.setFont(QFont('黑体',20))
btn.setToolTip('<b style="color:cyan">这是一个按钮的气泡提示！</b>')


#不同的操作系统可能对窗口的最小宽度有规定
widget.resize(300,200)
#屏幕左上角为(0,0)
widget.move(250,200)

widget.setWindowTitle('PyQt坐标系统例子')
widget.show()
print('QWidget:')
print('w.x()=%d' % widget.x())
print("w.y()= %d" % widget.y())
print("w.width()= %d" % widget.width())
print("w.height()= %d" % widget.height())

print('QWidget.geometry()')
print("QWidget.geometry().x()= %d" % widget.geometry().x())
print("QWidget.geometry().y()= %d" % widget.geometry().y())
print("QWidget.geometry().width()= %d" % widget.geometry().width())
print("QWidget.geometry().height()= %d" % widget.geometry().height())

sys.exit(app.exec())