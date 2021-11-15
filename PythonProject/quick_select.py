# -*- coding: utf-8 -*-
"""
BEYZA SAYRACI
170403034
07.12.2020
rANDOMIZED SELECT
"""
import numpy as np
import random
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import qs
import ast
import insertion
from PyQt5.QtGui import QIcon
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from PyQt5.QtGui import QMovie

class QS(QMainWindow):
    def __init__(self):
        super().__init__() 
        
        loadUi("quick_select.ui", self)
        self.pushButton_array.clicked.connect(self.random_array) 
        self.pushButton_index.clicked.connect(self.ith_smallest)
        self.pushButton_array_2.clicked.connect(self.clear)
        self.pushButton_array_3.clicked.connect(self.create_array)
        self.pushButton_array_4.clicked.connect(self.sorted_array)
        self.pushButton_array_5.clicked.connect(self.close)
        self.pushButton_array_6.clicked.connect(self.default_array)
        self.graph.canvas.axes.xaxis.set_visible(False)
        self.graph.canvas.axes.yaxis.set_visible(False)
        self.pushButton_array_2.setIcon(QIcon("icons/img_185728.png"))
        self.pushButton_array_5.setIcon(QIcon("icons/25694 (1).png"))
        self.setWindowTitle("Randomized Select") #window title
        self.pushButton.setIcon(QIcon("icons/Excel-Icon.png"))
        self.pushButton.clicked.connect(self.excel)
        self.setFixedSize(1200, 865)
        self.gif = QMovie("icons/text (12).gif")
        self.label.setMovie(self.gif)
        self.gif.start()
       
        
    def autolabel(self,rects):
        for rect in self.rects:
            height = rect.get_height()
            self.graph.canvas.axes.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                    '%d' % int(height),
            ha='center', va='bottom',color='black', fontweight='bold')
   #%%%% random array #%%%%%%%%%%%%% 
    def random_array(self):
        self.label.setVisible(False)
        self.array_size = self.spinBox.value()
        self.upper_range = self.spinBox_2.value()
        self.lower_range = self.spinBox_4.value()
        if (self.lower_range == 0 and self.upper_range == 0) or self.array_size == 0 :
                QMessageBox.critical(self,"ERROR","Please check your array..")
        else:
            if self.lower_range > self.upper_range :
                QMessageBox.critical(self,"ERROR","Should be upper range greater than lower range...")
            else:
                if self.checkBox_2.isChecked():
                    if (abs(self.upper_range - self.lower_range)) < self.array_size:
                                      QMessageBox.critical(self,"ERROR","To obtain a unique array, the difference between the lower and upper bound must be greater than the length of the array...")
                    else:
                        self.random_arrays=[]
                        while len(self.random_arrays)<self.array_size:
                            x=random.randint(self.lower_range,self.upper_range)
                            if not np.isin(x,self.random_arrays):
                                self.random_arrays.append(x)
                else:
                    self.random_arrays=[]
                    while True:
                        self.random_arrays.append(random.randint(self.lower_range,self.upper_range))
                        if len(self.random_arrays)==self.array_size:
                            break
            self.textEdit.setText(str(self.random_arrays)) #printing text edite.
            self.x = [] #empty x list
            for i in range(len(self.random_arrays)): 
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.random_arrays, color="black", edgecolor="black")
            self.autolabel(self.rects)
            self.graph.canvas.draw()
   #%%% ith smallest #%%%%%% 
    def ith_smallest(self): 
       
        try:
            self.index = self.spinBox_3.value()
            self.smallest_element = qs.SelectAlgorithm().randomized_select(self.random_arrays, 0, len(self.random_arrays)-1, self.index)
            self.textEdit_2.setText(str(self.smallest_element))
            self.x = []
            for i in range(len(self.sorted_arrays)): 
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.graph.canvas.axes.bar(self.x, self.sorted_arrays, color="black", edgecolor="black")
            self.graph.canvas.axes.bar(self.x[self.index-1], self.sorted_arrays[self.index-1], color="blue", edgecolor="black")
            for k, v in enumerate(self.sorted_arrays): 
                      self.graph.canvas.axes.text(k + 1.4, v + 0.55, " " + str(v), color='b', va='center', ha='right',
                                                             fontweight='bold', fontsize=12)
            self.graph.canvas.draw()
        except :
            QMessageBox.critical(self, "Message", "Please enter valid index.")
            self.x = []
            for i in range(len(self.sorted_arrays)): 
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.sorted_arrays, color="black", edgecolor="black")
            self.autolabel(self.rects)
            self.graph.canvas.draw()
     #%%clear button        
    def clear(self):
        self.label.setVisible(True)
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.spinBox.setValue(1)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.graph.canvas.axes.clear()
        self.graph.canvas.axes.patch.set_alpha(0)
        self.graph.canvas.draw()
        self.lineEdit.clear()
        self.random_arrays = []
        self.sorted_arrays = []
    
    #%%%% create array #%%%%%%%%%
    def create_array(self):
        try:
            self.label.setVisible(False)
            lists =  self.lineEdit.text()
            self.random_arrays = ast.literal_eval(lists)
            self.x = [] #empty x list
            for i in range(len(self.random_arrays)):
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.random_arrays, color="black", edgecolor="black")
            self.autolabel(self.rects)
            self.textEdit.setText(str(self.random_arrays))
            # self.sorted_arrays = insertion.insertion_sort(self.random_arrays) #random array to sorted array.
            # self.textEdit_3.setText(str(self.sorted_arrays)) #printing text edite.
            self.graph.canvas.draw()
        except:
          QMessageBox.critical(self,"ERROR","Please your only enter number.")
          self.graph.canvas.axes.clear()
          self.graph.canvas.axes.patch.set_alpha(0)
          self.graph.canvas.draw()
    
    #%%%% sorted array #%%%%%%%%%
    def sorted_array(self):
        try:

            self.sorted_arrays = insertion.insertion_sort(self.random_arrays) #random array to sorted array.
            self.textEdit_3.setText(str(self.sorted_arrays)) #printing text edite.
            self.x = [] #empty x list
            for i in range(len(self.sorted_arrays)): 
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.sorted_arrays, color="black", edgecolor="black")
            self.autolabel(self.rects)
            self.graph.canvas.draw()
        except AttributeError:
            QMessageBox.critical(self,"ERROR","Please select array...")

        except:
                QMessageBox.critical(self,"Error","Please select array...")
           
  
    #%%%%default array #%%%% 
    def default_array(self):
        self.label.setVisible(False)
        self.lower_range = random.randint(0,25)
        self.upper_range = random.randint(70,150)
        self.array_size = random.randint(1,45)
        self.spinBox_4.setValue(int(self.lower_range))
        self.spinBox.setValue(int(self.array_size))
        self.spinBox_2.setValue(int(self.upper_range))
        if self.checkBox_2.isChecked():
            if (abs(self.upper_range - self.lower_range)) < self.array_size:
                        QMessageBox.critical(self,"ERROR","To obtain a unique array, the difference between the lower and upper bound must be greater than the length of the array...")
            else:
                self.random_arrays=[]
                while len(self.random_arrays)<self.array_size:
                    x=random.randint(self.lower_range,self.upper_range)
                    if not np.isin(x,self.random_arrays):
                        self.random_arrays.append(x)
                self.textEdit.setText(str(self.random_arrays)) #printing text edite.
                self.x = [] #empty x list
                for i in range(len(self.random_arrays)): 
                    self.x.append(i+1)
                self.graph.canvas.axes.clear()
                self.graph.canvas.axes.patch.set_alpha(0)
                self.rects = self.graph.canvas.axes.bar(self.x, self.random_arrays, color="black", edgecolor="black")
                self.autolabel(self.rects)
                self.graph.canvas.draw()
        else:
            self.random_arrays=[]
            while True:
                self.random_arrays.append(random.randint(self.lower_range,self.upper_range))
                if len(self.random_arrays)==self.array_size:
                    break
            self.textEdit.setText(str(self.random_arrays)) #printing text edite.
            self.x = [] #empty x list
            for i in range(len(self.random_arrays)): 
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.random_arrays, color="black", edgecolor="black")
            self.autolabel(self.rects)
            self.graph.canvas.draw()
        #%%%%% excel #%%%%
    def excel(self):
        try:
            self.label.setVisible(False)
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
            self.textEdit.setText(str(self.random_arrays)) #printing text edite.
            self.x = [] #empty x list
            for i in range(len(self.random_arrays)): 
                self.x.append(i+1)
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.patch.set_alpha(0)
            self.rects = self.graph.canvas.axes.bar(self.x, self.random_arrays, color="black", edgecolor="black")
            self.autolabel(self.rects)
            self.graph.canvas.draw()
        except ValueError:
                 QMessageBox.critical(self,"Error","Please check your file...")
        except FileNotFoundError:
                 QMessageBox.critical(self,"Error","Please select a file...")
         
    
        
              

