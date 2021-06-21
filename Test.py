# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Test.ui'
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-10, 40, 1920, 1080))
        self.widget.setObjectName("widget")
        self.excelButton = QtWidgets.QPushButton(self.centralwidget)
        self.excelButton.setGeometry(QtCore.QRect(265, 13, 75, 23))
        self.excelButton.setObjectName("excelButton")
        self.OutButton = QtWidgets.QPushButton(self.centralwidget)
        self.OutButton.setGeometry(QtCore.QRect(346, 13, 75, 23))
        self.OutButton.setObjectName("OutButton")
        self.GoButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.GoButton_2.setGeometry(QtCore.QRect(103, 13, 75, 23))
        self.GoButton_2.setObjectName("GoButton_2")
        self.GoButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoButton.setGeometry(QtCore.QRect(22, 13, 75, 23))
        self.GoButton.setObjectName("GoButton")
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutButton.setGeometry(QtCore.QRect(427, 13, 75, 23))
        self.aboutButton.setObjectName("aboutButton")
        self.PayButton = QtWidgets.QPushButton(self.centralwidget)
        self.PayButton.setGeometry(QtCore.QRect(184, 13, 75, 23))
        self.PayButton.setObjectName("PayButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.GoButton, self.GoButton_2)
        MainWindow.setTabOrder(self.GoButton_2, self.excelButton)
        MainWindow.setTabOrder(self.excelButton, self.aboutButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "操作界面"))
        self.excelButton.setText(_translate("MainWindow", "导出excel"))
        self.OutButton.setText(_translate("MainWindow", "登出"))
        self.GoButton_2.setText(_translate("MainWindow", "工资"))
        self.GoButton.setText(_translate("MainWindow", "员工"))
        self.aboutButton.setText(_translate("MainWindow", "关于"))
        self.PayButton.setText(_translate("MainWindow", "付款信息"))


