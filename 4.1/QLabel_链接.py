#!/usr/bin/env python
# _*_ coding:utf-8 _*_


'''
    【简介】
	PyQT5中Qlabel例子

'''

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtGui import QPixmap,QPalette
from PyQt5.QtCore import Qt
import sys

class WindowDemo(QWidget):

    def __init__(self):
        super().__init__()

        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)

        #1初始化标签控件
        label1.setText('这是一个文本标签。')
        label1.setAutoFillBackground(True)
        palette = QPalette() #调色板
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片')
        label3.setPixmap(QPixmap('python.jpg'))

        label4.setText("<a href='https://github.com/cxinping/PyQt5'>槐荫访问新平的小屋</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('<b style="color:red">这是一个超链接标签</b>')

        #2、在窗口中添加控件
        vbox= QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        #3、允许label1控件访问超链接
        label1.setOpenExternalLinks(True)
        #打开允许访问超链接，默认是不允许的，需要使用setOpenExternalLinks(True)允许访问浏览器访问超链接
        label4.setOpenExternalLinks(False) # 设置为False设置为不允许访问浏览器，响应自己的事件
        #点击文本绑定曹事件
        label4.linkActivated.connect(self.link_clicked)

        #划过文本绑定事件
        label2.linkHovered.connect(self.link_hoverd)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel例子")


    def link_clicked(self):
        print("当鼠标点击label-4标签时，触发事件")

    def link_hoverd(self):
        print("当用鼠标滑过label-2标签时，触发事件")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowDemo()
    window.show()
    sys.exit(app.exec())