# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:06:20 2021

@author: Administrator
"""
import sys
from login import Ui_MainWindow as A_Ui # a界面的库
from Test import Ui_MainWindow as B_Ui # b界面的库
from Input import Ui_MainWindow as C_Ui
from insertemp import Ui_MainWindow as E_Ui
from insertsal import Ui_MainWindow as F_Ui
from message import message
from OpOracle import OpOracle
from PyQt5 import QtCore, QtWidgets
from functools import partial
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextBrowser, QWidget, QFrame



class HelloWindow(QtWidgets.QMainWindow, A_Ui):
    
    switch_window1 = QtCore.pyqtSignal()
    def __init__(self):
        super(HelloWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gooperate)
    def gooperate(self):
        self.switch_window1.emit()

class OperateWindow(QtWidgets.QMainWindow, B_Ui):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    def __init__(self):
        super(OperateWindow, self).__init__()
        self.setupUi(self)
        self.GoButton.clicked.connect(self.insertemp)
        self.GoButton_2.clicked.connect(self.insertsal)
        self.OutButton.clicked.connect(self.out)
        self.excelButton.clicked.connect(self.Input)
        self.aboutButton.clicked.connect(self.about)
    def insertemp(self):
        self.switch_window1.emit()
    def insertsal(self):
        self.switch_window2.emit()
    def out(self):
        self.switch_window3.emit()
    def Input(self):
        self.switch_window4.emit()
    def about(self):
        self.switch_window5.emit()

class InputWindow(QtWidgets.QMainWindow, C_Ui):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    def __init__(self):
        super(InputWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.excel)
        self.pushButton_2.clicked.connect(self.EXIT)
    def excel(self):
        self.switch_window1.emit()
    def EXIT(self):
        self.switch_window2.emit()
        
class insertempWindow(QtWidgets.QMainWindow, E_Ui):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    def __init__(self):
        super(insertempWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_4.clicked.connect(self.update)
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.EXIT)
        self.pushButton_5.clicked.connect(self.check)
    def insert(self):
        self.switch_window1.emit()
    def update(self):
        self.switch_window4.emit()
    def delete(self):
        self.switch_window3.emit()
    def EXIT(self):
        self.switch_window2.emit() 
    def check(self):
        self.switch_window5.emit() 
        
class insertsalWindow(QtWidgets.QMainWindow, F_Ui):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    def __init__(self):
        super(insertsalWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_3.clicked.connect(self.update)
        self.pushButton_4.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.EXIT)
        self.pushButton_5.clicked.connect(self.check)
    def insert(self):
        self.switch_window1.emit()
    def update(self):
        self.switch_window3.emit()
    def delete(self):
        self.switch_window4.emit()
    def EXIT(self):
        self.switch_window2.emit()    
    def check(self):
        self.switch_window5.emit() 
        
class Controller:
    def __init__(self):
        self.mess = message()
    def show_hello(self):
        self.hello = HelloWindow()
        self.hello.switch_window1.connect(partial(self.show_operate,self.hello)) 
        self.hello.setStyleSheet('#widget{border:3px  groove}'
                                 '#label_3{font-family:华文行楷 }'
                                 '#label_3{font: bold 24px }'
                                 '#widget{border-color: rgba(225, 255, 255, 150)}'
                                 '#label{background-color: rgba(255, 255, 255, 100)}'
                                 '#label_2{background-color: rgba(255, 255, 255, 100)}'
                                 'QMainWindow{border-image:url(C:/Users/Administrator/Pictures/Camera Roll/3.jpg)}')

        self.hello.show()
    # 跳转到 operate 窗口, 注意关闭原页面
    def show_operate(self,ui):
        
        self.operate = OperateWindow()
        self.input1 = ui.lineEdit.text()
        self.input2 = ui.lineEdit_2.text()
        self.check_name()
    def about(self):
        self.mess.aboutBtn_clicked()
    def show_emp(self):
        self.insertemp = insertempWindow()
        self.insertemp.setStyleSheet('QMainWindow{background-color:}')
        self.insertemp.show()
        self.insertemp.switch_window1.connect(self.emp_insert) 
        self.insertemp.switch_window2.connect(self.insertemp.close)
        self.insertemp.switch_window3.connect(self.emp_delete)
        self.insertemp.switch_window4.connect(self.emp_update)
        self.insertemp.switch_window5.connect(self.emp_check)
    def show_sal(self):
        self.insertsal = insertsalWindow()
        self.insertsal.setStyleSheet('QMainWindow{background-color:}')
        self.insertsal.show()
        self.insertsal.switch_window1.connect(self.sal_insert) 
        self.insertsal.switch_window2.connect(self.insertsal.close)
        self.insertsal.switch_window3.connect(self.sal_update)
        self.insertsal.switch_window4.connect(self.sal_delete)
        self.insertsal.switch_window5.connect(self.sal_check)
    def emp_insert(self):
        input1 = self.insertemp.lineEdit.text()    
        input2 = self.insertemp.lineEdit_2.text()
        input3 = self.insertemp.lineEdit_3.text() 
        input4 = self.insertemp.lineEdit_4.text()    
        input5 = self.insertemp.lineEdit_5.text()
        input6 = self.insertemp.lineEdit_6.text()
        input7 = self.insertemp.lineEdit_7.text()    
        input8 = self.insertemp.lineEdit_8.text()
        input9 = self.insertemp.lineEdit_9.text() 
        try:
            cid = self.ora.Ora_select_out('select s.id from fdl_city l,fdl_city s where l.l_name=:l_name and s.l_name=:s_name and s.PARENT_ID=l.SERIAL_NO',{'l_name':input6,'s_name':input7})
            cnaps = self.ora.Ora_select_out('select CNAPS_CODE from bank where BRANCH=:BRANCH and BNAME=:BNAME' ,{'BRANCH':input5,'BNAME':input4})
            self.ora.Ora_IUD_Multi('insert into employees values (:eno,:eaccount,:ename,:cnaps_code,:id,:email,:phone)',[{'eno':input1,'eaccount':input2,'ename':input3,'cnaps_code':cnaps,'id':cid,'email':input8,'phone':input9}])
        except:
            self.mess.criticalBtn_clicked()
        else:
            self.mess.infoBtn_clicked()
    def sal_insert(self):
        input1 = self.insertsal.lineEdit.text()    
        input2 = self.insertsal.lineEdit_2.text()
        input3 = self.insertsal.lineEdit_3.text() 
        try:
           self.ora.Ora_IUD_Multi('insert into salary values (:eno,:YEAR_MONTH,:AMOUNT)',[{'eno':input1,'YEAR_MONTH':input2,'AMOUNT':input3}])
        except:
            self.mess.criticalBtn_clicked()
        else:
            self.mess.infoBtn_clicked()
    def sal_update(self):
        
        input1 = self.insertsal.lineEdit.text()    
        input2 = self.insertsal.lineEdit_2.text()
        input3 = self.insertsal.lineEdit_3.text() 
        try:
            self.ora.Ora_IUD_Multi('update salary set amount=:amount where eno=:eno and YEAR_MONTH=:YEAR_MONTH',[{'eno':input1,'YEAR_MONTH':input2,'amount':input3}])
        except:
            self.mess.criticalBtn_clicked()
        else:
            self.mess.infoBtn_clicked()
    def emp_update(self):
        
        input1 = self.insertemp.lineEdit.text()    
        input2 = self.insertemp.lineEdit_2.text()
        input3 = self.insertemp.lineEdit_3.text() 
        input4 = self.insertemp.lineEdit_4.text()    
        input5 = self.insertemp.lineEdit_5.text()
        input6 = self.insertemp.lineEdit_6.text()
        input7 = self.insertemp.lineEdit_7.text()    
        input8 = self.insertemp.lineEdit_8.text()
        input9 = self.insertemp.lineEdit_9.text() 
        try:
            cid = self.ora.Ora_select_out('select s.id from fdl_city l,fdl_city s where l.l_name=:l_name and s.l_name=:s_name and s.PARENT_ID=l.SERIAL_NO',{'l_name':input6,'s_name':input7})
            cnaps = self.ora.Ora_select_out('select CNAPS_CODE from bank where BRANCH=:BRANCH and BNAME=:BNAME' ,{'BRANCH':input5,'BNAME':input4})
            self.ora.Ora_IUD_Multi('update employees set eaccount=:eaccount,ename=:ename,cnaps_code=:cnaps_code,id=:id,email=:email,phone=:phone where eno=:eno',[{'eno':input1,'eaccount':input2,'ename':input3,'cnaps_code':cnaps,'id':cid,'email':input8,'phone':input9}])
        except:
            self.mess.criticalBtn_clicked()
        else:
            self.mess.infoBtn_clicked()
    def sal_delete(self):
        input1 = self.insertsal.lineEdit.text()    
        input2 = self.insertsal.lineEdit_2.text()
        try:
            self.ora.Ora_IUD_Multi('delete from salary  where eno=:eno and YEAR_MONTH=:YEAR_MONTH',[{'eno':input1,'YEAR_MONTH':input2}])
        except:
            self.mess.criticalBtn_clicked()
        else:
            self.mess.infoBtn_clicked()
    def emp_delete(self):
        input1 = self.insertemp.lineEdit.text()    
        try:
            self.ora.Ora_IUD_Multi('delete from salary where eno=:eno ',[{'eno':input1}])
            self.ora.Ora_IUD_Multi('delete from employees where eno=:eno',[{'eno':input1}])
        except:
            self.mess.criticalBtn_clicked()
        else:
            self.mess.infoBtn_clicked()
    def out(self):
        self.ora.Ora_Cur_Close()
        self.ora.Ora_db_Close() 
        self.operate.close()
        self.hello.show()

    def emp_check(self):
        try:
            input1 = self.insertemp.lineEdit.text()    
            EACCOUNT = self.ora.Ora_select_out('select EACCOUNT from employees where eno=:eno',{'eno':input1})
            self.insertemp.lineEdit_2.setText(EACCOUNT)
            ENAME = self.ora.Ora_select_out('select ENAME from employees where eno=:eno',{'eno':input1})
            self.insertemp.lineEdit_3.setText(ENAME)
            BNAME = self.ora.Ora_select_out('select BNAME from employees,bank where eno=:eno and employees.CNAPS_CODE=bank.CNAPS_CODE',{'eno':input1})
            self.insertemp.lineEdit_4.setText(BNAME)
            BRANCH = self.ora.Ora_select_out('select BRANCH from employees,bank where eno=:eno and employees.CNAPS_CODE=bank.CNAPS_CODE',{'eno':input1})
            self.insertemp.lineEdit_5.setText(BRANCH)   
            L_NAME_0 = self.ora.Ora_select_out('select l.L_NAME from employees,FDL_CITY l,FDL_CITY s where eno=:eno and employees.id=s.id and l.SERIAL_NO=s.PARENT_ID',{'eno':input1})
            self.insertemp.lineEdit_6.setText(L_NAME_0)
            L_NAME_1 = self.ora.Ora_select_out('select L_NAME from employees,FDL_CITY where eno=:eno and employees.id=FDL_CITY.id',{'eno':input1})
            self.insertemp.lineEdit_7.setText(L_NAME_1)
            EMAIL = self.ora.Ora_select_out('select EMAIL from employees where eno=:eno',{'eno':input1})
            self.insertemp.lineEdit_8.setText(EMAIL)
            PHONE = self.ora.Ora_select_out('select PHONE from employees where eno=:eno',{'eno':input1})
            self.insertemp.lineEdit_9.setText(PHONE)
        except:
            self.mess.criticalBtn_clicked()
        else:
            self.mess.infoBtn_clicked()
            self.Input.close()
    
    def sal_check(self):
        try:
            input1 = self.insertsal.lineEdit.text()  
            input2 = self.insertsal.lineEdit_2.text() 
            AMOUNT = self.ora.Ora_select_out('select AMOUNT from salary where eno=:eno and YEAR_MONTH=:YEAR_MONTH',{'eno':input1,'YEAR_MONTH':input2})
            self.insertsal.lineEdit_3.setText(AMOUNT)
        except:
            self.mess.criticalBtn_clicked()
        else:
            self.mess.infoBtn_clicked()
            self.Input.close()        
    def excel(self): 
        input1 = self.Input.dateEdit.text()
        input2 = self.Input.dateEdit_2.text() 
        self.year1='01'+'-'+input1[5:6]+'月 '+'-'+input1[2:4]
        self.year2='01'+'-'+input2[5:6]+'月 '+'-'+input2[2:4]
        try:
            self.ora.Ora_Select_List("""select e.eno"收款人编号",e.eaccount"收款人账号",e.ename"收款人名称",b.branch"收方开户支行",c.l_name"收款人所在省",l.l_name"收款人所在市",e.email"收方邮件地址",e.phone"收方移动电话",p.Currency"币种",p.branch"付款分行",p.settlement_method"结算方式",p.business_types"业务种类",p.account"付方账号",to_char(sysdate,'yyyymmdd')"期望日",to_char(sysdate,'hh24miss')"期望时间",p.purposes"用途",sum(s.amount)"金额",b.cnaps_code"收方联行号",b.bname"收方开户银行" 
                                     from employees e,bank b,FDL_CITY c,FDL_CITY l,payment p,salary s 
                                     where b.CNAPS_CODE=e.CNAPS_CODE and l.ID=e.ID and s.eno=e.eno and c.SERIAL_NO=l.PARENT_ID and s.YEAR_MONTH between :month1 and :month2 
                                     group by e.eno,e.eaccount,e.ename,b.branch,c.l_name,l.l_name,e.email,e.phone,p.Currency,p.branch,p.settlement_method,p.business_types,p.account,to_char(sysdate,'yyyymmdd'),to_char(sysdate,'hh24miss'),p.purposes,b.cnaps_code,b.bname
                                     order by e.eno""",
                                     {'month1':self.year1,'month2':self.year2})
            self.ora.Ora_excel(self.Input.lineEdit.text())
        except:
            self.mess.criticalBtn_clicked()
        else:
            self.mess.infoBtn_clicked()
            self.Input.close()
    
    def Input_name(self):
        self.Input = InputWindow()
        self.Input.show()
        self.Input.switch_window1.connect(self.excel)
        self.Input.switch_window2.connect(self.Input.close)
    def check_name(self):
        try:
            self.ora=OpOracle(self.input1,self.input2,'localhost','1521','orcl')
        except:
            print('登录名/登录密码错误,请重新输入')
            self.mess.criticalBtn_clicked()
        else:
            print('登录成功')
            self.hello.close()
            self.operate.setStyleSheet('#widget{background-color: white }'
                                       'QMainWindow{border-image:url(C:/Users/Administrator/Pictures/Camera Roll/3.jpg)}')
            self.operate.show()
            self.operate.switch_window1.connect(self.show_emp)  
            self.operate.switch_window2.connect(self.show_sal)  
            self.operate.switch_window3.connect(self.out)
            self.operate.switch_window4.connect(self.Input_name)
            self.operate.switch_window5.connect(self.about)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller() # 控制器实例
    controller.show_hello() # 默认展示的是 hello 页面
    sys.exit(app.exec_())


        


