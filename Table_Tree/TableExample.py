#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
from PyQt5.QtWidgets import QWidget,QTableWidget, QHBoxLayout, QApplication,\
    QTableWidgetItem,QHeaderView,QAbstractItemView,QComboBox, QPushButton
from PyQt5 import QtCore
from PyQt5 import QtGui

class Table(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(400,300)

        conLayout = QHBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        # 等价于 tableWidget= QTableWidget(4,3)
        conLayout.addWidget(tableWidget)

        # 设置表格头
        tableWidget.setHorizontalHeaderLabels(["姓名","性别","体重(kg)"])

        # 生成QTableWidgetItem对象，然后添加
        newItem = QTableWidgetItem("张三")
        tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem("男")
        tableWidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem("120")
        tableWidget.setItem(0,2,newItem)

        # 设置表格头为伸缩模式
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 将表格设置为禁止编辑
        # tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 设置表格整行选中
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 将行和列的宽度、高度设置为所显示的内容的宽度和高度
        QTableWidget.resizeColumnsToContents(tableWidget)
        QTableWidget.resizeRowsToContents(tableWidget)

        # 表格头的显示与隐藏
        # tableWidget.verticalHeader().setVisible(False)
        # tableWidget.horizontalHeader().setVisible(False)

        # 在单元格中放置控件
        comBox = QComboBox()
        comBox.addItem("男")
        comBox.addItem("女")
        comBox.setStyleSheet("QComBox{margin:3px};")
        tableWidget.setCellWidget(0,1,comBox)

        # searchBtn = QPushButton("修改")
        # searchBtn.setDown(True)
        # searchBtn.setStyleSheet("QPushButton{margin:3px};")
        # tableWidget.setCellWidget(0,2,searchBtn)
        newItem = QTableWidgetItem("170")
        newItem.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        tableWidget.setItem(0,2,newItem)

        # 在表格中快速定位到指定行
         # 遍历查找表格对应的单元格
        text="张三"  # 代表需要找到的文本，可能有多个
        item = tableWidget.findItems(text,QtCore.Qt.MatchExactly)
         # 获取其行号
        print(item)
        row = item[0].row()
         # 模拟鼠标快速滚动到指定的位置
        tableWidget.verticalScrollBar().setSliderPosition(row)

        newItem = QTableWidgetItem("李四")
        newItem.setBackground(QtGui.QBrush(QtGui.QColor(255,0,0))) # 设置背景颜色
        newItem.setForeground(QtGui.QBrush(QtGui.QColor(255,255,255))) #设置前景颜色
        tableWidget.setItem(1,0,newItem)

        # 字体加粗
        newItem = QTableWidgetItem("男")
        newItem.setFont(QtGui.QFont("Times",12, QtGui.QFont.Black))
        tableWidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem("160")
        # 设置单元格的对齐方式
        newItem.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        tableWidget.setItem(1, 2, newItem)

        # 按照升序排序
        tableWidget.sortItems(2,QtCore.Qt.AscendingOrder)

        # 合并单元格
        newItem = QTableWidgetItem("符合")
        tableWidget.setItem(2,0,newItem)
        tableWidget.setSpan(2,0,1,3)

        # 设置单元格大小
        tableWidget.setColumnWidth(2,50)
        tableWidget.setRowHeight(2,100)

        # 在表格中不现实分割线
        # tableWidget.setShowGrid(False)

        # 为单元格添加图片
        newItem = QTableWidgetItem(QtGui.QIcon("./images/bao1.png"), "背包")
        tableWidget.setItem(3,0,newItem)

        tableWidget.itemClicked.connect(self.getItem)

        self.setLayout(conLayout)

    def getItem(self,item):
        print("你选择的 =》"+ item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Table()
    win.show()
    sys.exit(app.exec())

