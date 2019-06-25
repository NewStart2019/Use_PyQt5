#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from PyQt5.QtWidgets import QWidget,QFormLayout,QLineEdit,QApplication
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class LoginMainFrame(QWidget):

    def __init__(self):
        super(LoginMainFrame,self).__init__()
        self.setWindowTitle('登录界面')

        account  = QLineEdit()
        password = QLineEdit()
        password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        password.setToolTip('<b style="color:red;">密码</b>')

        layout = QFormLayout()
        layout.addRow('账户:',account)
        layout.addRow('密码:',password)

        account.setPlaceholderText('邮箱/手机号码')

        reg1 = QRegExp("[0-9A-Za-z]+@[0-9A-Za-z]{3,}.com$")
        reg2 = QRegExp("[0-9A-Za-z#@]+$")

        accountValidator   = QRegExpValidator(self)
        passwordValidator  = QRegExpValidator(self)
        accountValidator.setRegExp(reg1)
        passwordValidator.setRegExp(reg2)

        account.setValidator(accountValidator)
        password.setValidator(passwordValidator)

        self.setLayout(layout)
        self.setFixedWidth(400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = LoginMainFrame()
    loginWindow.show()
    sys.exit(app.exec())