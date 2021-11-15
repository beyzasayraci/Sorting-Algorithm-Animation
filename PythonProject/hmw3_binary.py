# -*- coding: utf-8 -*-
"""
Beyza Sayraci
170403034
29.11.2020
Binary Search Main
"""

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import numpy as np
import insertion, binary
from PyQt5.uic import loadUi
import ast
import random
from PyQt5.QtWidgets import*
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from PyQt5.QtGui import QMovie
class binaryy(QMainWindow):
    def __init__(self):
        super().__init__() 
        loadUi("binary.ui", self)
        
        #%%#connect button
        self.pushButton_random.clicked.connect(self.random_array) 
        self.pushButton_sorted.clicked.connect(self.sorted_array)
        self.pushButton_index.clicked.connect(self.index)
        self.pushButton.clicked.connect(self.clear)
        self.pushButton_random_2.clicked.connect(self.create_array)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_random_3.clicked.connect(self.default_array)
        self.pushButton_3.clicked.connect(self.excel)
        self.graph.canvas.axes.xaxis.set_visible(False)
        self.graph.canvas.axes.yaxis.set_visible(False)
        self.pushButton.setIcon(QIcon("icons/img_185728.png"))
        self.pushButton_2.setIcon(QIcon("icons/25694 (1).png"))
        self.pushButton_3.setIcon(QIcon("icons/images (1).png"))
        self.setWindowTitle("Binary Search")
        self.setFixedSize(1200, 865)
        self.gif = QMovie("icons/text (9).gif")
        self.label_4.setMovie(self.gif)
        self.gif.start()
   
    def autolabel(self,rects):
        for rect in self.rects:
            height = rect.get_height()
            self.graph.canvas.axes.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                    '%d' % int(height),
            ha='center', va='bottom',color='black', fontweight='bold')

       
        #%%random array
    def random_array(self):
        self.label_4.setVisible(False)
        self.array_size = self.spinBox.value()
        self.upper_range = self.spinBox_2.value()
        self.lower_range = self.spinBox_3.value()
        if (self.lower_range == 0 and self.upper_range == 0) or self.array_size == 0 :
                QMessageBox.critical(self,"ERROR","Please check your array..")
        else:
            if self.lower_range > self.upper_range :
                QMessageBox.critical(self,"ERROR","Should be upper range greater than lower range...")
            else:
                if (abs(self.upper_range - self.lower_range)) < self.array_size:
                                  QMessageBox.critical(self,"ERROR","To obtain a unique array, the difference between the lower and upper bound must be greater than the length of the array...")
                else:
                    self.random_arrays=[]
                    while len(self.random_arrays)<self.array_size:
                        x=random.randint(self.lower_range,self.upper_range)
                        if not np.isin(x,self.random_arrays):
                            self.random_arrays.append(x)

            self.textEdit_rondam.setText(str(self.random_arrays)) #printing text edite.
            self.x = [] #empty x list
            for i in range(len(self.random_arrays)): 
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.random_arrays, color="red", edgecolor="black")
            self.autolabel(self.rects)
            self.graph.canvas.draw()
        # except AttributeError:
        #     QMessageBox.critical(self,"ERROR","Please check your array")
        
    #%%sorted array
    def sorted_array(self):
       try:
            self.sorted_arrays = insertion.insertion_sort(self.random_arrays) #random array to sorted array.
            self.textEdit_sorted.setText(str(self.sorted_arrays)) #printing text edite.
            self.x = [] #empty x list
            for i in range(len(self.random_arrays)): 
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.random_arrays, color="red", edgecolor="black")
            self.autolabel(self.rects)
            self.graph.canvas.draw()
       except AttributeError:
            QMessageBox.critical(self,"ERROR","Please select array.")
        
    #%%index
    def index(self):
        try:
           self.arrays = self.spinBox_input_index.value()  #what number?
           self.x = []
           for i in range(len(self.sorted_arrays)):
               self.x.append(i+1)
           self.binaryS = binary.Binary_Search(self.sorted_arrays,0,len(self.sorted_arrays), self.arrays) #print binary search index
           self.textEdit_index.setText(str(self.binaryS)) #printing text edite.
           self.graph.canvas.axes.clear()
           self.graph.canvas.axes.patch.set_alpha(0)
           self.graph.canvas.axes.bar(self.x, self.sorted_arrays, color="red", edgecolor="black")
           self.rects = self.graph.canvas.axes.bar(self.x[self.binaryS], self.sorted_arrays[self.binaryS], color="blue", edgecolor="black")
           self.autolabel(self.rects)
           self.graph.canvas.draw()
        except:
            QMessageBox.critical(self,"ERROR","Please enter the correct number.")
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.sorted_arrays, color="red", edgecolor="black")
            self.autolabel(self.rects)
            self.graph.canvas.draw()
        
      
       #%%clearbutton
    def clear(self): 
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.spinBox_input_index.setValue(0)
        self.textEdit_index.clear()
        self.textEdit_rondam.clear()
        self.textEdit_sorted.clear()
        self.graph.canvas.axes.clear()
        self.graph.canvas.axes.patch.set_alpha(0)
        self.graph.canvas.draw()
        self.lineEdit.clear()
        self.random_arrays = []
        self.sorted_arrays = []
        self.label_4.setVisible(True)
        #%%create array
    def create_array(self):
        try:
            self.label_4.setVisible(False)
            lists =  self.lineEdit.text()
            self.random_arrays = ast.literal_eval(lists)
            self.x = [] #empty x list
            for i in range(len(self.random_arrays)):
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.random_arrays, color="red", edgecolor="black")
            self.autolabel(self.rects)
            self.textEdit_rondam.setText(str(self.random_arrays))
            self.graph.canvas.draw()
        except:
            QMessageBox.critical(self,"ERROR","Please your only enter number.")
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.graph.canvas.draw()
    
    #%% default array #%%%
    
    def default_array(self):
        self.label_4.setVisible(False)
        self.lower_range = random.randint(0,25)
        self.upper_range = random.randint(70,150)
        self.array_size = random.randint(1,45)
        self.spinBox_3.setValue(int(self.lower_range))
        self.spinBox.setValue(int(self.array_size))
        self.spinBox_2.setValue(int(self.upper_range))
        if (abs(self.upper_range - self.lower_range)) < self.array_size:
                    QMessageBox.critical(self,"ERROR","To obtain a unique array, the difference between the lower and upper bound must be greater than the length of the array...")
        else:
            self.random_arrays=[]
            while len(self.random_arrays)<self.array_size:
                x=random.randint(self.lower_range,self.upper_range)
                if not np.isin(x,self.random_arrays):
                    self.random_arrays.append(x)
  
        # self.random_arrays=[]
        # while True:
        #     self.random_arrays.append(random.randint(self.lower_range,self.upper_range))
        #     if len(self.random_arrays)==self.array_size:
        #         break
        self.textEdit_rondam.setText(str(self.random_arrays)) #printing text edite.
        self.x = [] #empty x list
        for i in range(len(self.random_arrays)): 
            self.x.append(i+1)
        self.graph.canvas.axes.clear()
        self.graph.canvas.axes.patch.set_alpha(0)
        self.rects = self.graph.canvas.axes.bar(self.x, self.random_arrays, color="red", edgecolor="black")
        self.autolabel(self.rects)
        self.graph.canvas.draw()
   
    #%%%%% excel #%%%%%%%%%%%%%
    def excel(self):
        try:
            self.label_4.setVisible(False)
            result = QMessageBox()
            result.setIcon(QMessageBox.Question)
            result.setText("Please select Xlxs File?")
            result.setStandardButtons(QMessageBox.Yes)
            button_txt = result.button(QMessageBox.Yes)
            button_txt.setText("Xlxs File")
            a = result.exec_()
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()
            df = pd.read_excel(file_path)
            self.random_arrays=df.columns
            self.random_arrays=list(self.random_arrays)
            print(self.random_arrays)
            for i in range(len(self.random_arrays)):
                   self.random_arrays[i]=int(self.random_arrays[i])
            self.textEdit_rondam.setText(str(self.random_arrays)) #printing text edite.
            self.x = [] #empty x list
            for i in range(len(self.random_arrays)): 
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.random_arrays, color="red", edgecolor="black")
            self.autolabel(self.rects)
            self.graph.canvas.draw()
        except ValueError:
                 QMessageBox.critical(self,"Error","Please check your file...")
        except FileNotFoundError:
                 QMessageBox.critical(self,"Error","Please select a file...")
         
                        
    
        
            
                 
