
from PyQt5 import QtCore, QtGui, QtWidgets
 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(434, 329)
        self.infoBtn = QtWidgets.QPushButton(Dialog)
        self.infoBtn.setGeometry(QtCore.QRect(40, 40, 101, 23))
        self.infoBtn.setObjectName("infoBtn")
        self.questionBtn = QtWidgets.QPushButton(Dialog)
        self.questionBtn.setGeometry(QtCore.QRect(40, 80, 101, 23))
        self.questionBtn.setObjectName("questionBtn")
        self.warningBtn = QtWidgets.QPushButton(Dialog)
        self.warningBtn.setGeometry(QtCore.QRect(40, 120, 101, 23))
        self.warningBtn.setObjectName("warningBtn")
        self.criticalBtn = QtWidgets.QPushButton(Dialog)
        self.criticalBtn.setGeometry(QtCore.QRect(40, 160, 101, 23))
        self.criticalBtn.setObjectName("criticalBtn")
        self.aboutBtn = QtWidgets.QPushButton(Dialog)
        self.aboutBtn.setGeometry(QtCore.QRect(40, 200, 101, 23))
        self.aboutBtn.setObjectName("aboutBtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 10, 221, 16))
        self.label.setObjectName("label")
        self.aboutQtBtn = QtWidgets.QPushButton(Dialog)
        self.aboutQtBtn.setGeometry(QtCore.QRect(40, 240, 101, 23))
        self.aboutQtBtn.setObjectName("aboutQtBtn")

        self.retranslateUi(Dialog)
        self.infoBtn.clicked.connect(Dialog.infoBtn_clicked)
        self.questionBtn.clicked.connect(Dialog.questionBtn_clicked)
        self.warningBtn.clicked.connect(Dialog.warningBtn_clicked)
        self.criticalBtn.clicked.connect(Dialog.criticalBtn_clicked)
        self.aboutBtn.clicked.connect(Dialog.aboutBtn_clicked)
        self.aboutQtBtn.clicked.connect(Dialog.aboutQtBtn_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.infoBtn.setText(_translate("Dialog", "通知对话框"))
        self.questionBtn.setText(_translate("Dialog", "询问对话框"))
        self.warningBtn.setText(_translate("Dialog", "警告对话框"))
        self.criticalBtn.setText(_translate("Dialog", "严重警告对话框"))
        self.aboutBtn.setText(_translate("Dialog", "关于对话框"))
        self.label.setText(_translate("Dialog", "我是一个lable"))
        self.aboutQtBtn.setText(_translate("Dialog", "关于Qt对话框"))

