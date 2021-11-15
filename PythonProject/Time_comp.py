# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:37:33 2020

@author: pc
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
import sys
from sort import times
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
class Time(QWidget):

    def __init__(self):
        super().__init__() 
        
        loadUi("time.ui", self)
        
        self.method_list=[False,False,False,False,False,False,False,False,False]

        self.checkBox_2.toggled.connect(self.onCheckBox_Toggled)
        self.checkBox.toggled.connect(self.onCheckBox_Toggled)
        self.checkBox_3.toggled.connect(self.onCheckBox_Toggled)
        self.checkBox_9.toggled.connect(self.onCheckBox_Toggled)
        self.checkBox_6.toggled.connect(self.onCheckBox_Toggled)
        self.checkBox_8.toggled.connect(self.onCheckBox_Toggled)
        self.checkBox_5.toggled.connect(self.onCheckBox_Toggled)
        self.checkBox_4.toggled.connect(self.onCheckBox_Toggled)
        self.checkBox_7.toggled.connect(self.onCheckBox_Toggled)
        self.pushButton_4.clicked.connect(self.close)
        self.graphs.canvas.axes.set_title('Time Comparison Graph')
        self.graphs.canvas.axes.set_xlabel('Number of elements in array')
        self.graphs.canvas.axes.set_ylabel('Time')
        self.setWindowTitle("Time Comparison")
        self.pushButton_2.clicked.connect(self.handle_CompareAll)
        self.pushButton_3.clicked.connect(self.clear)
        self.pushButton.clicked.connect(self.handle_CompareChosen)
        self.pushButton_3.setIcon(QIcon("icons/img_185728.png"))
        self.pushButton_4.setIcon(QIcon("icons/25694 (1).png"))
        self.setFixedSize(1200, 865)
        
    def handle_CompareAll(self):
        
            all_methods=times().comparison([True,True,True,True,True,True,True,True,True])
            row_headers=["Bubble","Insertion","Merge","Selection","Counting","Heap","Bucket","Radix","Quick"]
            methods_list=[]
            for i in row_headers:
                methods_list.append(all_methods[i])
           
            color_list=["#F9E16D","#e60000","#114477","#F1A1D8","#03F512","#BCF199","#03F5DF","#B303F5","#223300"]
            k=0
            self.graphs.canvas.axes.clear()
            for i in methods_list:
                
                self.graphs.canvas.axes.plot([100,300,500,2000],i, color=color_list[k],label=row_headers[k])
                self.graphs.canvas.axes.legend(row_headers,loc="upper left")
                self.graphs.canvas.draw()
                k+=1
                
    def handle_CompareChosen(self):
            if not(self.method_list[0] or self.method_list[1] or self.method_list[2] or self.method_list[3] or self.method_list[4] or self.method_list[5] or self.method_list[6] or self.method_list[7] or self.method_list[8]): 
                QMessageBox.critical(self,"ERROR","Please choose a methods.")
            else:
                 row_headers=[]
                 row_counter=0
                 if self.method_list[0]:
                     row_headers.append("Bubble")
                     row_counter+=1
                 if self.method_list[1]:
                     row_headers.append("Insertion")
                     row_counter+=1
                 if self.method_list[2]:
                     row_headers.append("Merge")
                     row_counter+=1
                 if self.method_list[3]:
                     row_headers.append("Selection")
                     row_counter+=1
                 if self.method_list[4]:
                     row_headers.append("Counting")
                     row_counter+=1
                 if self.method_list[5]:
                     row_headers.append("Heap")
                     row_counter+=1
                 if self.method_list[6]:
                     row_headers.append("Bucket")
                     row_counter+=1
                 if self.method_list[7]:
                     row_headers.append("Radix")
                     row_counter+=1
                 if self.method_list[8]:
                     row_headers.append("Quick")
                     row_counter+=1
                 chosen_methods=times().comparison(self.method_list)
                 methods_list=[]
                 for i in row_headers: 
                     methods_list.append(chosen_methods[i])
               
                 color_list=["#F9E16D","#e60000","#114477","#F1A1D8","#03F512","#BCF199","#03F5DF","#B303F5","#223300"]
                 k=0
                 self.graphs.canvas.axes.clear()
                 for i in methods_list: 
                     self.graphs.canvas.axes.plot([100,300,500,2000],i, color=color_list[k],label=row_headers[k])
                     self.graphs.canvas.axes.legend(row_headers,loc="upper left")
                     self.graphs.canvas.draw()
                     k+=1
                     
    def onCheckBox_Toggled(self):
        
        if self.checkBox_2.isChecked():
            self.method_list[0]=True
        else:
            self.method_list[0]=False
        if self.checkBox.isChecked():
            self.method_list[1]=True
        else:
            self.method_list[1]=False
        if self.checkBox_3.isChecked():
            self.method_list[2]=True
        else:
            self.method_list[2]=False
        if self.checkBox_9.isChecked():
            self.method_list[3]=True
        else:
            self.method_list[3]=False
        if self.checkBox_6.isChecked():
            self.method_list[4]=True
        else:
            self.method_list[4]=False
        if self.checkBox_8.isChecked():
            self.method_list[5]=True
        else:
            self.method_list[5]=False
        if self.checkBox_5.isChecked():
            self.method_list[6]=True
        else:
            self.method_list[6]=False
        if self.checkBox_4.isChecked():
            self.method_list[7]=True
        else:
            self.method_list[7]=False
        if self.checkBox_7.isChecked():
            self.method_list[8]=True
        else:
            self.method_list[8]=False
            
    def clear(self): 
        self.checkBox_2.setChecked(False)
        self.checkBox.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.graphs.canvas.axes.clear()
        self.graphs.canvas.draw()
        
        
       


