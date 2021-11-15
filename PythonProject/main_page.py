# -*- coding: utf-8 -*-
"""
Beyza Sayraci
170403034
31.11.2020
"""
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from matrix import win
from fibonacci import fibonacci
from hmw3_binary import binaryy
from sortal import Sort
from inf import Information
from quick_select import QS
from Time_comp import Time
from PyQt5.QtGui import QIcon
import webbrowser
from mail import mail
#%%interface login screen
class MainPage(QWidget):
    def __init__(self):
        super().__init__() 
        
        loadUi("main.ui", self)
        #%%enable buttons
        self.pushButton.clicked.connect(self.open_second_page)
        self.pushButton_3.clicked.connect(self.open_third_page)
        self.pushButton_2.clicked.connect(self.open_fourth_page)
        self.pushButton_5.clicked.connect(self.open_sort_page)
        self.pushButton_4.clicked.connect(self.open_information_page)
        self.pushButton_7.clicked.connect(self.open_randomize_page)
        self.pushButton_6.clicked.connect(self.open_time_page)
        self.pushButton_9.clicked.connect(self.close)
        self.pushButton_11.clicked.connect(self.youtube)
        self.pushButton_8.setIcon(QIcon("icons/İzmir_Kâtip_Çelebi_Üniversitesi_logosu.png"))
        self.pushButton_8.clicked.connect(self.web)
        self.pushButton_10.clicked.connect(self.open_mail_page)
        self.pushButton_10.setIcon(QIcon("icons/indir.png"))
        self.pushButton_9.setIcon(QIcon("icons/images (3).png"))
        self.pushButton_4.setIcon(QIcon("icons/information-icon-png-8-png-image-information-icon-png-1200_630.png"))
        self.pushButton_11.setIcon(QIcon("icons/youtube.png"))
        self.setWindowTitle("Introduction the Algorithm ---Created by Beyza Sayraci")
        self.setFixedSize(1200, 865)
        self.randomize_page = QS()
        self.second_page = win()
        self.third_page = fibonacci()
        self.fourth_page = binaryy()
        self.sort_page = Sort()
        self.information_page = Information()
        self.time_page = Time()
        self.mail_page = mail()
        
    def open_second_page(self): #matrix mul fun.
        self.second_page.show() #show in window.
            
    def open_third_page(self): #fibonacci fun.
        self.third_page.show() #show in window.
        
    def open_fourth_page(self): #bianary fun.
        self.fourth_page.show() #show in window.
        
    def open_sort_page(self):
        self.sort_page.show()
        
    def open_information_page(self):
        self.information_page.show()
    
    def open_randomize_page(self):
        self.randomize_page.show()
        
    def open_time_page(self):
        self.time_page.show()
    
    def web(self):
        webbrowser.open('https://www.ikcu.edu.tr/%27')
    def youtube(self):
        webbrowser.open('https://www.youtube.com/channel/UCVx9odXaosySGaDtXX96QGA')
        
    def open_mail_page(self):
        self.mail_page.show()
        
        

