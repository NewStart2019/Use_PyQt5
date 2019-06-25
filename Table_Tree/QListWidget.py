#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QWidgets

class ListWidget(QWidgets.QListWidget):
    def clicked(self, index: QtCore.QModelIndex):
        QWidgets.QMessageBox.information(self,"ListWidget","你选择了："+index.text())

def Widgetd():
    listWidget =ListWidget()
    listWidget.resize(300,120)
    listWidget.addItem("item 1")
    listWidget.addItem("item 2")
    listWidget.addItem("item 3")
    listWidget.addItem("item 4")
    listWidget.setWindowTitle("QListWidget 例子")
    listWidget.itemClicked.connect(listWidget.clicked)
    return listWidget


if __name__ == '__main__':
    app = QWidgets.QApplication(sys.argv)
    listWidget=Widgetd()
    listWidget.show()
    sys.exit(app.exec())