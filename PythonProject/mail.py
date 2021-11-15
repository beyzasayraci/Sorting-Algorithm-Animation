# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 23:59:08 2020

@author: pc
"""
import smtplib
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
class mail(QWidget):
    stop_array = "global"
    def __init__(self):
        super().__init__() 
        
        loadUi("mail.ui", self)
        
        
        self.pushButton_send.clicked.connect(self.send)
        self.pushButton_13.clicked.connect(self.close)
        self.pushButton_13.setIcon(QIcon("icons/25694 (1).png"))
        self.setFixedSize(496, 522)
        
    def send(self):
       
            self.name = self.textEdit_name.toPlainText()
            self.mail = self.textEdit_mail.toPlainText()
            self.message = self.textEdit_message.toPlainText()
       
            if len(self.message) == 0:
                QMessageBox.critical(self,"Error","Message field cannot be blank...")
            else:
                self.mes = self.name + self.mail + self.message
                mail = smtplib.SMTP("smtp.gmail.com",587)
                mail.ehlo()
                mail.starttls()
                mail.login("beyzasayraci@gmail.com","939802nbs")
                mail.sendmail("beyzasayraci@gmail.com","beyzasayraci@gmail.com",self.mes)
                QMessageBox.information(self,"Information","Your e-mail has been sent successfully....")
          
                
        

# app = QApplication([])
# window= mail()
# window.show()
# app.exec_()         