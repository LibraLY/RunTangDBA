# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:17:36 2021

@author: Administrator
"""

from PyQt5.QtWidgets import *
from messageBox import Ui_Dialog
import sys
 
class message(QDialog):
    def __init__(self):
        super(message,self).__init__()
        print("Dialog is called!")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
     
    #通知对话框槽函数
    def infoBtn_clicked(self):
        #显示的按钮分别是Ok、Close，默认按钮是Close。
        reply=QMessageBox.information(self,"通知","成功",QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.ui.label.setText('你选择了Ok！')
        else:
            self.ui.label.setText('你选择了Close！')
    #询问对话框槽函数
    def questionBtn_clicked(self):
        reply=QMessageBox.question(self,"询问","提醒用户是否进行某种操作",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.ui.label.setText('你选择了Yes！')
        elif reply == QMessageBox.No:
            self.ui.label.setText('你选择了No！')
        else:
            self.ui.label.setText('你选择了Cancel！')
    #警告对话框槽函数
    def warningBtn_clicked(self):
        QMessageBox.warning(self,'警告','程序运行时产生的异常，提示用户注意，非致命性错误，一般可以忽略', QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
    #严重警告对话框槽函数
    def criticalBtn_clicked(self):
        QMessageBox.critical(self,'严重警告','产生错误或者异常,请重新输入', QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore , QMessageBox.Retry)
    #关于对话框槽函数
    def aboutBtn_clicked(self):
        QMessageBox.about(self,"关于","润堂劳务公司财务系统\t \n \nCopyright © 2021-2021 Runtang.Co.Ltd . All rights reserved. \t")

    #关于Qt对话框槽函数
    def aboutQtBtn_clicked(self):
        QMessageBox.aboutQt(self,"关于Qt")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = message()
    #显示主界面
    main.show()
    sys.exit(app.exec_())
