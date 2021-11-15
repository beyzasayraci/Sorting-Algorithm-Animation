# -*- coding: utf-8 -*-
"""
#Beyza Sayraci
#170403034
#Matrix mult.
#29.10.20
"""


from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
import numpy as np
from PyQt5.uic import loadUi
from tkinter import filedialog
import xlsxwriter
from PyQt5.QtGui import QIcon
import ast
from sort import AlignDelegate
import tkinter as tk
from tkinter import filedialog
from PyQt5.QtGui import QMovie
#%% connect button, window tittle and line edit information
class win(QMainWindow):
    def __init__(self):
        super().__init__() 
        
        loadUi("matrix.ui", self)        
        self.pushButton_clear.clicked.connect(self.clear) #clear connect button 
        self.row_A.setValidator(QIntValidator(1,10,self)) #only integer
        self.col_B.setValidator(QIntValidator(1,10,self)) #only integer 
        self.col_A.setValidator(QIntValidator(1,10,self)) #only integer 
        self.pushButton_create.clicked.connect(self.matrixCreate) #create connect button
        self.pushButton_multmat.clicked.connect(self.matrixmult) #multiply connect button
        self.pushButton_multmat_2.clicked.connect(self.generate_matrix)
        self.pushButton_clear_2.clicked.connect(self.close)
        self.pushButton_multmat_3.clicked.connect(self.minus)
        self.pushButton_multmat_4.clicked.connect(self.add)
        self.pushButton_clear.setIcon(QIcon("icons/img_185728.png"))
        self.pushButton_clear_2.setIcon(QIcon("icons/25694 (1).png"))
        self.pushButton_clear_3.setIcon(QIcon("icons/Excel-Icon.png"))
        self.pushButton_multmat_4.setIcon(QIcon("icons/artı.png"))
        self.pushButton_multmat_3.setIcon(QIcon("icons/eksi.png"))
        self.pushButton_clear_3.clicked.connect(self.savefile)
        self.pushButton_multmat.setIcon(QIcon("icons/çarp.png"))
        self.setWindowTitle("Matrix Operation") #window title
        self.setFixedSize(1214, 866)
        self.gif = QMovie("icons/text (11).gif")
        self.label_8.setMovie(self.gif)
        self.gif.start()
        

     #%% create celar button for all.
    def clear(self): #celar button
        self.row_A.setText("0")
        self.col_A.setText("0")
        self.col_B.setText("0")
        self.row_B.setText("0")
        self.tableWidget_mat1.clear()
        self.tableWidget_mat2.clear()
        self.tableWidget__mat3.clear()
        self.tableWidget_mat1.setRowCount(0) #matrix1 size determination
        self.tableWidget_mat1.setColumnCount(0) #matrix1 size determination
        self.tableWidget_mat2.setRowCount(0) #matrix2 size determination
        self.tableWidget_mat2.setColumnCount(0) #matrix2 size determination
        self.tableWidget__mat3.setRowCount(0)
        self.tableWidget__mat3.setColumnCount(0)
  
    
      #%%Create Random Matrix for matrix1 and matrix2  
    def matrixCreate(self):
        self.rowA = int(self.row_A.text()) #get input row1
        self.colA = int(self.col_A.text()) #get input col1 #get input row2
        self.colB = int(self.col_B.text())  #get input col2
        self.rowB = int(self.row_B.text())
        if self.rowA==0 or self.colA ==0 or self.colB==0 or self.rowB==0:
              QMessageBox.critical(self,"Error","Enter correct values for matrix operations...")
        else:
                self.tableWidget_mat1.setRowCount(self.rowA) #matrix1 size determination
                self.tableWidget_mat1.setColumnCount(self.colA) #matrix1 size determination
                self.tableWidget_mat2.setRowCount(self.rowB) #matrix2 size determination
                self.tableWidget_mat2.setColumnCount(self.colB) #matrix2 size determination
                
                for i in range(self.colA):
                    self.tableWidget_mat1.setColumnWidth(i,391/self.colA)
                for i in range(self.rowA):
                    self.tableWidget_mat1.setRowHeight(i,371/self.rowA)
                for i in range(self.colB):
                    self.tableWidget_mat2.setColumnWidth(i,391/self.colB)
                for i in range(self.rowB):
                    self.tableWidget_mat2.setRowHeight(i,371/self.rowB)

                self.matrix1 = np.random.randint(-100,100, size=(self.rowA,self.colA)) # create random matrix
                self.matrix2 = np.random.randint(-100,100, size=(self.rowB,self.colB)) # create random matrix
            
                #%% print the resulting matrix on the table widget.
                for i, rowA in enumerate(self.matrix1): #for matrix1
                    for j, value in enumerate(rowA): 
                        self.tableWidget_mat1.setItem(i,j,QtWidgets.QTableWidgetItem(str(value)))
                
                for i in range(self.colA):
                    delegate =AlignDelegate(self.tableWidget_mat1)
                    self.tableWidget_mat1.setItemDelegateForColumn(i, delegate)
                
                for i in range(self.rowA):
                    delegate =AlignDelegate(self.tableWidget_mat1)
                    self.tableWidget_mat1.setItemDelegateForRow(i, delegate)
                  
                for k, rowB in enumerate(self.matrix2): #for matrix2
                    for l, value in enumerate(rowB):
                        self.tableWidget_mat2.setItem(k, l, QtWidgets.QTableWidgetItem(str(value)))
                
                for i in range(self.rowB):
                    delegate =AlignDelegate(self.tableWidget_mat2)
                    self.tableWidget_mat2.setItemDelegateForRow(i, delegate)
        
                for i in range(self.colB):
                    delegate =AlignDelegate(self.tableWidget_mat2)
                    self.tableWidget_mat2.setItemDelegateForColumn(i, delegate)
                
      
       
      #%% function to do matrix multiplication. 
    def matrixmult(self): 
       
        try:
            self.tableWidget__mat3.setRowCount(self.rowA)
            self.tableWidget__mat3.setColumnCount(self.colB)
            if self.rowA==0 or self.colB==0 :
              QMessageBox.critical(self,"Error","Enter correct values for matrix multiplication...")
            else:
                if self.colA != self.rowB : 
                    QMessageBox.critical(self,"ERROR","For matrix multiplication, the row of matrix one must be equal to the column of the matrix two...")
                    self.tableWidget__mat3.setRowCount(0)
                    self.tableWidget__mat3.setColumnCount(0)
                
                else:
                    self.result = [[0 for i in range(self.colB)] for j in range(self.rowA)] #new matrix and matrix multiplication.
        
                    for i in range(self.rowA):
                        for j in range(self.colB):
                            for k in range(self.colA):
                                self.result[i][j] += int(self.tableWidget_mat1.item(i,k).text()) * int(self.tableWidget_mat2.item(k,j).text()) #matrix mult.
        
                
                    for i in range(self.rowA):
                        for j in range(self.colB):
                            number=self.result[i][j]
                            self.tableWidget__mat3.setItem(i, j, QtWidgets.QTableWidgetItem(str(number)))
                    
                    for i in range(self.rowA):
                        delegate =AlignDelegate(self.tableWidget__mat3)
                        self.tableWidget__mat3.setItemDelegateForRow(i, delegate)
                    
                    for i in range(self.colB):
                        delegate =AlignDelegate(self.tableWidget__mat3)
                        self.tableWidget__mat3.setItemDelegateForColumn(i, delegate)
                     
                    for i in range(self.colB):
                        self.tableWidget__mat3.setColumnWidth(i,391/self.colB)
                    
                    for i in range(self.rowA):
                        self.tableWidget__mat3.setRowHeight(i,371/self.rowA)
        except AttributeError :
            QMessageBox.critical(self, "Message", "Enter correct values for matrix multiplication...")
            self.tableWidget__mat3.setRowCount(0)
            self.tableWidget__mat3.setColumnCount(0)
            self.tableWidget__mat3.clear()
        except ValueError : 
            QMessageBox.critical(self, "Message", "Please enter numbers only.")
            self.tableWidget__mat3.setRowCount(0)
            self.tableWidget__mat3.setColumnCount(0)
            self.tableWidget__mat3.clear()
                
#%%%%%%%%%%% generate matrix #%%%%%%%%%%%%%%%%%%
    def generate_matrix(self): 
        try:
            self.rowA = int(self.row_A.text()) #get input row1
            self.colA = int(self.col_A.text()) #get input col1 #get input row2
            self.colB = int(self.col_B.text())
            self.rowB = int(self.row_B.text())
            if self.rowA==0 and self.colA ==0 and self.colB==0 and self.rowB==0:
              QMessageBox.critical(self,"Error","Enter correct values for matrix operations...")
              self.tableWidget__mat3.setRowCount(0)
              self.tableWidget__mat3.setColumnCount(0)
            else:
                        self.tableWidget_mat1.setRowCount(self.rowA) #matrix1 size determination
                        self.tableWidget_mat1.setColumnCount(self.colA) #matrix1 size determination
                        self.tableWidget_mat2.setRowCount(self.rowB) #matrix2 size determination
                        self.tableWidget_mat2.setColumnCount(self.colB) #matrix2 size determination
                     
                        
                        for i in range(self.colA):
                            self.tableWidget_mat1.setColumnWidth(i,391/self.colA)
                        for i in range(self.rowA):
                            self.tableWidget_mat1.setRowHeight(i,371/self.rowA)
                        for i in range(self.colB):
                            self.tableWidget_mat2.setColumnWidth(i,391/self.colB)
                        for i in range(self.rowB):
                            self.tableWidget_mat2.setRowHeight(i,371/self.rowB)
                        
                        for i in range(self.rowA):
                            delegate =AlignDelegate(self.tableWidget_mat1)
                            self.tableWidget_mat1.setItemDelegateForRow(i, delegate)
                
                        for i in range(self.colA):
                            delegate =AlignDelegate(self.tableWidget_mat1)
                            self.tableWidget_mat1.setItemDelegateForColumn(i, delegate)
                            
                        for i in range(self.rowB):
                            delegate =AlignDelegate(self.tableWidget_mat2)
                            self.tableWidget_mat2.setItemDelegateForRow(i, delegate)
        
                        for i in range(self.colB):
                            delegate =AlignDelegate(self.tableWidget_mat2)
                            self.tableWidget_mat2.setItemDelegateForColumn(i, delegate)
                          
                        self.matrix1 = np.zeros(self.rowA,self.colA)
                        self.matrix2 = np.zeros(self.rowB,self.colB)
        
                        for i, rowA in enumerate(self.matrix1): #for matrix1
                             for j, value in enumerate(rowA): 
                                 self.tableWidget_mat1.setItem(i,j,QtWidgets.QTableWidgetItem(str(value)))
                        
                       
                        for k, rowB in enumerate(self.matrix2): #for matrix2
                             for l, value in enumerate(rowB):
                                 self.tableWidget_mat2.setItem(k, l, QtWidgets.QTableWidgetItem(str(value)))

        except ValueError : 
            QMessageBox.critical(self, "Message", "Please enter numbers only.")
        except AttributeError :
            QMessageBox.critical(self, "Message", "Enter correct values for matrix operations...")
                
     #%%%%%%%%% save file #%%%%%%%%%%%%%%%%       
    def savefile(self):
        
        if len(self.result) == 0:
             QMessageBox.critical(self, "Message", "Please, make a matrix multiplication...")
             
        else:
            save_file = QFileDialog.getSaveFileName(self,"Select the file to save","","*.xlsx")
            self.excel_file = xlsxwriter.Workbook(save_file[0])
            self.save = self.excel_file.add_worksheet()
            row =0
            for i in range(len(self.result)):
                column = 0
                for j in range(len(self.result)):
                    self.save.write(row,column,self.result[i][j])
                    column += 1
                row +=1
            self.excel_file.close()
        
    #%%%%%%%%%%%%% add matrix #%%%%%%%%%%%%%%%%%%%%
    def add(self):
        
        # self.rowA = int(self.row_A.text()) #get input row1
        # self.colA = int(self.col_A.text()) #get input col1 #get input row2
        # self.colB = int(self.col_B.text())
        # self.rowB = int(self.row_B.text())
        try:
            self.tableWidget__mat3.setRowCount(self.rowA)
            self.tableWidget__mat3.setColumnCount(self.colB)
            if self.rowA==0 or self.colA ==0 or self.colB==0 or self.rowB==0:
              QMessageBox.critical(self,"Error","Enter correct values for matrix sum...")
              self.tableWidget__mat3.setRowCount(0)
              self.tableWidget__mat3.setColumnCount(0)
            else:
                if (self.rowA != self.rowB) or (self.colA != self.colB):
                     QMessageBox.critical(self,"Error","Enter correct values for matrix sum...")
                     self.tableWidget__mat3.setRowCount(0)
                     self.tableWidget__mat3.setColumnCount(0)
                else:
                    self.result = [[0 for i in range(self.colB)] for j in range(self.rowA)] 
                    
                    for i in range(len(self.matrix1)):
                        for j in range(len(self.matrix1[0])):
                            self.result[i][j] = int(self.tableWidget_mat1.item(i,j).text()) + int(self.tableWidget_mat2.item(i,j).text()) #matrix mult.
                    
                    for i in range(self.rowA):
                            for j in range(self.colB):
                                number=self.result[i][j]
                                self.tableWidget__mat3.setItem(i, j, QtWidgets.QTableWidgetItem(str(number)))
                    for i in range(self.colB):
                            delegate =AlignDelegate(self.tableWidget__mat3)
                            self.tableWidget__mat3.setItemDelegateForRow(i, delegate)
                        
                    for i in range(self.rowA):
                            delegate =AlignDelegate(self.tableWidget__mat3)
                            self.tableWidget__mat3.setItemDelegateForRow(i, delegate)
                         
                    for i in range(self.colA):
                            self.tableWidget__mat3.setColumnWidth(i,391/self.colA)
                            
                         
                    for i in range(self.colB):
                            self.tableWidget__mat3.setColumnWidth(i,391/self.colB)
                        
                    for i in range(self.rowB):
                            self.tableWidget__mat3.setRowHeight(i,371/self.rowB)
                    for i in range(self.rowA):
                            self.tableWidget__mat3.setRowHeight(i,371/self.rowA)
        except AttributeError :
            QMessageBox.critical(self, "Message", "Enter correct values for matrix sum...")
            self.tableWidget__mat3.setRowCount(0)
            self.tableWidget__mat3.setColumnCount(0)
          
        except ValueError : 
            QMessageBox.critical(self, "Message", "Please enter numbers only.")
            self.tableWidget__mat3.setRowCount(0)
            self.tableWidget__mat3.setColumnCount(0)
            
    #B%%%%% subtract #%%%%%%%%%%%
    def minus(self):
        try:
            self.tableWidget__mat3.setRowCount(self.rowA)
            self.tableWidget__mat3.setColumnCount(self.colB)
            self.rowA = int(self.row_A.text()) #get input row1
            self.colA = int(self.col_A.text()) #get input col1 #get input row2
            self.colB = int(self.col_B.text())
            self.rowB = int(self.row_B.text())
            if (self.rowA != self.rowB) or (self.colA != self.colB):
                 QMessageBox.critical(self,"Error","Enter correct values for matrix subtraction...")
                 self.tableWidget__mat3.setRowCount(0)
                 self.tableWidget__mat3.setColumnCount(0)
            else:
                self.result = [[0 for i in range(self.colB)] for j in range(self.rowA)] 
                for i in range(len(self.matrix1)):
                    for j in range(len(self.matrix1[0])):
                        self.result[i][j] =int(self.tableWidget_mat1.item(i,j).text()) - int(self.tableWidget_mat2.item(i,j).text())
                for i in range(self.rowA):
                        for j in range(self.colB):
                            number=self.result[i][j]
                            self.tableWidget__mat3.setItem(i, j, QtWidgets.QTableWidgetItem(str(number)))
                for i in range(self.colB):
                        delegate =AlignDelegate(self.tableWidget__mat3)
                        self.tableWidget__mat3.setItemDelegateForRow(i, delegate)
                    
                for i in range(self.rowA):
                        delegate =AlignDelegate(self.tableWidget__mat3)
                        self.tableWidget__mat3.setItemDelegateForRow(i, delegate)
                     
                for i in range(self.colA):
                        self.tableWidget__mat3.setColumnWidth(i,391/self.colA)
                        
                     
                for i in range(self.colB):
                        self.tableWidget__mat3.setColumnWidth(i,391/self.colB)
                    
                for i in range(self.rowB):
                        self.tableWidget__mat3.setRowHeight(i,371/self.rowB)
                for i in range(self.rowA):
                        self.tableWidget__mat3.setRowHeight(i,371/self.rowA)
        except AttributeError :
            QMessageBox.critical(self, "Message", "Enter correct values for matrix subtraction...")
            self.tableWidget__mat3.setRowCount(0)
            self.tableWidget__mat3.setColumnCount(0)
          
        except ValueError : 
            QMessageBox.critical(self, "Message", "Please enter numbers only.")
            self.tableWidget__mat3.setRowCount(0)
            self.tableWidget__mat3.setColumnCount(0)
            

     

    
