# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\input.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(196, 158, 72, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(274, 158, 133, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(226, 130, 88, 20))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(332, 130, 88, 20))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(196, 130, 24, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 130, 16, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(196, 186, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(277, 186, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionasf = QtWidgets.QAction(MainWindow)
        self.actionasf.setObjectName("actionasf")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dateEdit, self.dateEdit_2)
        MainWindow.setTabOrder(self.dateEdit_2, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "导出excel"))
        self.label.setText(_translate("MainWindow", "请输入文件名"))
        self.label_2.setText(_translate("MainWindow", "日期"))
        self.label_3.setText(_translate("MainWindow", "-"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.actionasf.setText(_translate("MainWindow", "asf  "))


