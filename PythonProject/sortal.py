# -*- coding: utf-8 -*-
"""
Beyza Sayraci
09.11.20
170403034
Sort Algorithm
"""
import sys
import timeit
import numpy as np
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import time
import insertion
import random
from PyQt5 import QtCore
import create_array
import tkinter as tk
from tkinter import filedialog
import csv
import pandas as pd
import numpy as np
from PyQt5.QtGui import QIcon
import xlsxwriter
import ast
import matplotlib.pyplot as plt
import speech_recognition as sr
import pyaudio
import pyglet
from PyQt5.QtGui import QMovie

class Sort(QWidget):
    stop_array = "global"
    def __init__(self):
        super().__init__() 
        self.randomArray = []
        # self.music = music
        
        loadUi("sorting_algortihm.ui", self)
        self.gif = QMovie("icons/text (7).gif")
        self.label.setMovie(self.gif)
        self.gif.start()
        
        
        self.pushButton_4.clicked.connect(self.random_array)
        self.pushButton_2.clicked.connect(self.insertion_sort)
        self.pushButton_3.clicked.connect(self.merge_sort)
        self.pushButton_8.clicked.connect(self.quick_sort)
        self.pushButton.clicked.connect(self.bubble_sort)
        self.pushButton_7.clicked.connect(self.heap_sort)
        self.pushButton_9.clicked.connect(self.bucket_sort)
        self.pushButton_5.clicked.connect(self.counting_sort)
        self.pushButton_6.clicked.connect(self.radix_sort)
        self.pushButton_10.clicked.connect(self.selection_sort)
        self.pushButton_11.clicked.connect(self.shell_sort)
        self.pushButton_12.clicked.connect(self.default_array)
        self.pushButton_14.clicked.connect(self.stop)
        self.pushButton_15.clicked.connect(self.skip)
        self.pushButton_16.clicked.connect(self.contunie)
        self.pushButton_18.clicked.connect(self.get_excel)
        self.pushButton_19.clicked.connect(self.save_excel)
        self.pushButton_13.clicked.connect(self.close)
        self.pushButton_20.clicked.connect(self.cocktail_sort)
        self.pushButton_21.clicked.connect(self.comb_sort)
        self.pushButton_22.clicked.connect(self.clear)
        self.pushButton_23.clicked.connect(self.voice)
        self.pushButton_18.setIcon(QIcon("icons/images.png"))
        self.pushButton_19.setIcon(QIcon("icons/kdsfjklhfsdjk.png"))
        self.pushButton_14.setIcon(QIcon("icons/pause-circle-fill-play-tool-button-31939.png"))
        self.pushButton_15.setIcon(QIcon("icons/ic_skip_next_48px-512.png"))
        self.pushButton_16.setIcon(QIcon("icons/img_106831.png"))
        self.pushButton_13.setIcon(QIcon("icons/25694 (1).png"))
        self.pushButton_22.setIcon(QIcon("icons/img_185728.png"))
        self.pushButton_23.setIcon(QIcon("icons/microphone.png"))
        self.setWindowTitle("Sorting Algorithm")
        self.setFixedSize(1200, 865)
        self.widget1.canvas.axes.xaxis.set_visible(False)
        self.widget1.canvas.axes.yaxis.set_visible(False)
        self.pushButton_17.clicked.connect(self.create_array)
        #self.widget1.canvas.axes.set_frame_on(False)
        self.widget1.canvas.axes.set_facecolor('#d8bfd8')
        self.widget1.canvas.axes.get_facecolor()
        self.pushButton_14.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.verticalSlider.setNotchesVisible(True)
    
    def autolabel(self,rects):
        for rect in self.rects:
            height = rect.get_height()
            self.widget1.canvas.axes.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                    '%d' % int(height),
            ha='center', va='bottom',color='white', fontweight='bold')
    
    def clear(self):
        self.label.setVisible(True)
        self.randomArray = []
        self.textEdit.setText("Unsorted Array")
        self.textEdit_2.setText("Sorted Array")
        self.spinBox_range.setValue(0)
        self.spinBox_array_size_2.setValue(0)
        self.widget1.canvas.axes.clear()
        self.widget1.canvas.axes.patch.set_alpha(0)
        self.widget1.canvas.draw()
        self.label_6.setText("Speed")
        self.lineEdit_3.setText("")
        self.spinBox_range_2.setValue(0)
        self.lineEdit_5.clear()

    
    def create_array(self):
        try:
            self.label.setVisible(False)
            lists =  self.lineEdit_3.text()
            self.randomArray = ast.literal_eval(lists)
            self.x = [] #empty x list
            for i in range(len(self.randomArray)):
                self.x.append(i+1)
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.rects = self.widget1.canvas.axes.bar(self.x, self.randomArray, color="magenta",edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
        except:
                QMessageBox.critical(self,"Error","Please enter only numbers..")
                
    def voice(self):
        self.label.setVisible(False)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                # self.label.setText('You are start talking.')
                audio = r.listen(source)
                # self.label.setText('You are stop talking.')
                a = (r.recognize_google(audio))
                try:
                    a = int(a)
                    print(a)
                    self.randomArray.append(a)
                    self.lineEdit_5.setText(str(self.randomArray))    
                    print(self.randomArray)
            
                except ValueError:
                       QMessageBox.information(self,"Error","Please, try again...")
            except sr.UnknownValueError:
                QMessageBox.information(self,"ERROR","Please, repeat what you said...")
            except sr.RequestError as e:
                QMessageBox.information(self,"ERROR","Could not request results from Google Speech Recognition service; {0}".format(e))
            except sr.RequestError:
                QMessageBox.information(self,"ERROR","You have not Internet Connection...")
      
        self.x = [] #empty x list
        for i in range(len(self.randomArray)):
            self.x.append(i+1)
        self.widget1.canvas.axes.clear()
        self.widget1.canvas.axes.patch.set_alpha(0)
        self.rects = self.widget1.canvas.axes.bar(self.x, self.randomArray, color="magenta",edgecolor="white",linewidth=1)
        self.autolabel(self.rects)
        self.widget1.canvas.draw()
       
        
                        
                
    def contunie(self):
        global stop_array
        self.stop_array = int(0)
        self.plays.play()
    def stop(self):
        global stop_array
        self.stop_array = int(1)
        self.plays.pause()
    def skip(self):
        global stop_array
        global randomArray
        self.widget1.canvas.axes.clear()
        self.stop_array = int(2)
        if self.stop_array == 2:
            sorted_array = self.randomArray
            sorted_array.sort()
            t = np.arange(len(sorted_array))
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.rects = self.widget1.canvas.axes.bar(t, sorted_array, color="magenta" , edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.widget1.canvas.axes.set_title('Sorted Array Bar')
            self.widget1.canvas.draw()
            self.textEdit_2.setText(str(sorted_array))
        self.plays.pause()
     
  
    def butttons(self):
        global stop_array
        global randomArray
        while self.stop_array == 1: 
                        if self.stop_array == 0:
                               if self.stop_array == 2:
                                   self.widget1.canvas.axes.clear()
                                   self.widget1.canvas.axes.patch.set_alpha(0)
                                   break
                               break
                        time.sleep(1)
                        QtCore.QCoreApplication.processEvents()
                        if self.stop_array == 2:
                                   self.widget1.canvas.axes.clear()
                                   self.widget1.canvas.axes.patch.set_alpha(0)
                                   break
     
                        
    def get_excel(self):
        try:
            self.label.setVisible(False)
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Question)
            mb.setText("Please select File?")
            mb.setWindowTitle("Error")
            mb.setStandardButtons(QMessageBox.Yes | QMessageBox.Open | QMessageBox.Ok)
            button_xlsx = mb.button(QMessageBox.Yes)
            button_xlsx.setText("Xlsx File")
            button_txt = mb.button(QMessageBox.Open)
            button_txt.setText("Txt File")
            button_csv = mb.button(QMessageBox.Ok)
            button_csv.setText("Csv File")
            result = mb.exec_()
            if result == QMessageBox.Yes:
                root = tk.Tk()
                root.withdraw()
                file_path = filedialog.askopenfilename()
                df = pd.read_excel(file_path)
                self.randomArray=df.columns
                self.randomArray=list(self.randomArray)
                print(self.randomArray)
                for i in range(len(self.randomArray)):
                    self.randomArray[i]=int(self.randomArray[i])
                
          
            elif result == QMessageBox.Open: ##txt file
                root = tk.Tk()
                root.withdraw()
                file_path = filedialog.askopenfilename()
                text_file = open(file_path, "r")
                self.randomArray = text_file.read().split(',')
                for i in range(len(self.randomArray)):
                    self.randomArray[i]=int(self.randomArray[i])
                    
            else:
                root = tk.Tk()
                root.withdraw()
                file_path = filedialog.askopenfilename()
                with open(file_path) as f: 
                    okur = csv.reader(f)
                    for satır in okur:
                        self.randomArray=satır
                    for i in range(len(self.randomArray)):
                        self.randomArray[i]=int(self.randomArray[i])
               
            self.x = []       
            for i in range(len(self.randomArray)):
                self.x.append(i+1)
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.rects=self.widget1.canvas.axes.bar(self.x, self.randomArray, color="magenta",edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
            self.textEdit.setText(str(self.randomArray)) 
        except ValueError:
                 QMessageBox.critical(self,"Error","Please check your file...")
        except FileNotFoundError:
                 QMessageBox.critical(self,"Error","Please select a file...")
                 
    def save_excel(self):
        try:
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Question)
            mb.setText("Please select File?")
            mb.setWindowTitle("Error")
            mb.setStandardButtons(QMessageBox.Yes | QMessageBox.Open | QMessageBox.Ok)
            button_xlsx = mb.button(QMessageBox.Yes)
            button_xlsx.setText("Xlsx File")
            button_txt = mb.button(QMessageBox.Open)
            button_txt.setText("Txt File")
            button_csv = mb.button(QMessageBox.Ok)
            button_csv.setText("Csv File")
            result = mb.exec_()
            if len(self.randomArray) == 0:
                QMessageBox.critical(self,"Error","Please select array...")
            else:
                try:

                    if result == QMessageBox.Yes:
                        save_file = QFileDialog.getSaveFileName(self,"Select the file to save","","*.xlsx")
                        self.excel_file = xlsxwriter.Workbook(save_file[0])
                        self.save = self.excel_file.add_worksheet()
                        row = 0
                        column = 0
                        for i in range (len(self.randomArray)):
                            self.save.write(row,column,self.randomArray[i])
                            column += 1
                        self.excel_file.close()
                    
                    elif result == QMessageBox.Open:
                        root = tk.Tk()
                        root.withdraw()
                        file_path =filedialog.asksaveasfilename(defaultextension="txt",
                          filetypes=[("Text Files", ".txt"), ("All Files", ".*")],) 
                        if not file_path:
                          return
                        with open(file_path, "w") as output_file:
                          text = str(self.randomArray)
                          text=text.strip("[")
                          text=text.strip("]")
                          output_file.write(text)
                        
                    else:
                        root = tk.Tk()
                        root.withdraw()
                        file_path = filedialog.asksaveasfilename(
                          defaultextension="csv",
                          filetypes=[("csv file",".csv"), ("All Files", ".*")],)
                        if not file_path:
                            return
                        with open(file_path, "w") as output_file:
                          text = str(self.unsorted_array)
                          text=text.strip("[")
                          text=text.strip("]")
                          output_file.write(text)
                except FileNotFoundError:
                    QMessageBox.critical(self,"Error","Please enter name a file...")
                 
                   
        except ValueError:
                 QMessageBox.critical(self,"Error","Please check your file...")
       
                     
            
        
    def default_array(self):
        self.label.setVisible(False)
        self.range = random.randint(0,25)
        self.upper_range = random.randint(70,150)
        self.array_size = random.randint(1,45)
        self.spinBox_range.setValue(int(self.range))
        self.spinBox_array_size_2.setValue(int(self.array_size))
        self.spinBox_range_2.setValue(int(self.upper_range))
        if self.checkBox.isChecked():
            random.seed(0)
            random.sample
            if self.checkBox_2.isChecked():
                if (abs(self.upper_range - self.range)) < self.array_size:
                    QMessageBox.critical(self,"ERROR","To obtain a unique array, the difference between the lower and upper bound must be greater than the length of the array...")
                else:
                    self.randomArray=[]
                    while len(self.randomArray)<self.array_size:
                        x=random.randint(self.range,self.upper_range)
                        if not np.isin(x,self.randomArray):
                            self.randomArray.append(x)
            else:
                self.randomArray=[]
                while True:
                    self.randomArray.append(random.randint(self.range,self.upper_range))
                    if len(self.randomArray)==self.array_size:
                        break
        else:
            if self.checkBox_2.isChecked():
                if (abs(self.upper_range - self.range)) < self.array_size:
                    QMessageBox.critical(self,"ERROR","To obtain a unique array, the difference between the lower and upper bound must be greater than the length of the array...")
                              
                else:  
                    self.randomArray=[]
                    while len(self.randomArray)<self.array_size:
                        x=random.randint(self.range,self.upper_range)
                        if not np.isin(x,self.randomArray):
                            self.randomArray.append(x)
                                    
                self.randomArray=[]
                while len(self.randomArray)<self.array_size:
                    x=random.randint(self.range,self.upper_range)
                    if not np.isin(x,self.randomArray):
                        self.randomArray.append(x)
                                
            else:
                self.randomArray=[]
                while True:
                    self.randomArray.append(random.randint(self.range,self.upper_range))
                    if len(self.randomArray)==self.array_size:
                        break
            
      
            
            
        self.x = []
        for i in range(len(self.randomArray)):
            self.x.append(i+1)
        self.widget1.canvas.axes.clear()
        self.widget1.canvas.axes.patch.set_alpha(0)
        self.widget1.canvas.axes.patch.set_alpha(0)
        self.rects=self.widget1.canvas.axes.bar(self.x, self.randomArray, color="magenta", edgecolor="white",linewidth=1)
        self.autolabel(self.rects)
        self.widget1.canvas.draw()
        self.textEdit.setText(str(self.randomArray)) 
             
      
   
    def enable(self):
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        self.pushButton_17.setEnabled(True)
        self.pushButton_14.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_18.setEnabled(True)
        self.pushButton_19.setEnabled(True)
        self.pushButton_15.setEnabled(False)
        self.pushButton_13.setEnabled(True)
    def disable(self):
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_14.setEnabled(True)
        self.pushButton_16.setEnabled(True)
        self.pushButton_18.setEnabled(False)
        self.pushButton_19.setEnabled(False)
        self.pushButton_15.setEnabled(True)
        self.pushButton_13.setEnabled(False)
    
    def random_array(self):
        self.label.setVisible(False)
        self.randomArray = []
        try:
            self.array_range = int(self.spinBox_range.value())
            self.upper_range = int(self.spinBox_range_2.value())
            self.array_size = int(self.spinBox_array_size_2.value())

            if (self.array_range == 0 and self.upper_range == 0) or self.array_size == 0 :
                QMessageBox.critical(self,"ERROR","Please check your array..")
            else:
                if self.array_range > self.upper_range :
                    QMessageBox.critical(self,"ERROR","Should be upper range greater than lower range...")
                else:
                    
                    if self.checkBox.isChecked():
                        random.seed(0)
                        random.sample
                        if self.checkBox_2.isChecked():
                            if (abs(self.upper_range - self.array_range)) < self.array_size:
                                  QMessageBox.critical(self,"ERROR","To obtain a unique array, the difference between the lower and upper bound must be greater than the length of the array...")
                            else:
                                self.randomArray=[]
                                while len(self.randomArray)<self.array_size:
                                    x=random.randint(self.array_range,self.upper_range)
                                    if not np.isin(x,self.randomArray):
                                        self.randomArray.append(x)
                                
                     
                        else: 
                            self.randomArray=[]
                            while True:
                                self.randomArray.append(random.randint(self.array_range,self.upper_range))
                                if len(self.randomArray)==self.array_size:
                                    break
                            
                    else:
                        
                        if self.checkBox_2.isChecked():
                            if (abs(self.upper_range - self.array_range)) < self.array_size:
                                  QMessageBox.critical(self,"ERROR","To obtain a unique array, the difference between the lower and upper bound must be greater than the length of the array...")
                                  
                            else:  
                                self.randomArray=[]
                                while len(self.randomArray)<self.array_size:
                                    x=random.randint(self.array_range,self.upper_range)
                                    if not np.isin(x,self.randomArray):
                                        self.randomArray.append(x)
                                        
                            self.randomArray=[]
                            while len(self.randomArray)<self.array_size:
                                x=random.randint(self.array_range,self.upper_range)
                                if not np.isin(x,self.randomArray):
                                    self.randomArray.append(x)
                                    
                        else:
                            self.randomArray=[]
                            while True:
                                self.randomArray.append(random.randint(self.array_range,self.upper_range))
                                if len(self.randomArray)==self.array_size:
                                    break
                
            self.x = []
            for i in range(len(self.randomArray)):
                self.x.append(i+1)
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.rects = self.widget1.canvas.axes.bar(self.x, self.randomArray, color="magenta",edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
            self.textEdit.setText(str(self.randomArray))                
        except AttributeError:
            QMessageBox.critical(self,"ERROR","Please check your array")
       
        
   ###### insertion sort ###############     
    def insertion_sort(self):#insertion algorithm start 
         
         try:
            self.disable()
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.rects = self.widget1.canvas.axes.bar(self.x, self.randomArray, color='magenta', edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
            self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
            time.sleep(self.sort_speed)
            QApplication.processEvents()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
           
    
            for i in range(1,len(self.randomArray)):  #the first number is sorted.skip the first number.
             
               
                self.widget1.canvas.axes.clear()
                self.widget1.canvas.axes.patch.set_alpha(0)
                key = self.randomArray[i]  #set a key value.
                j = i  #run through the list of items. 
                self.widget1.canvas.axes.bar(self.x, self.randomArray, color='magenta')
                self.widget1.canvas.axes.bar(self.x[j], self.randomArray[j], color='black')
                self.widget1.canvas.axes.bar(self.x[j-1], self.randomArray[j-1], color='black')
                self.widget1.canvas.draw()
                self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                time.sleep(self.sort_speed)
                QApplication.processEvents()
              
                while j > 0 and self.randomArray[j-1] > key: #find the correct position.compare the smaller and greater of the numbers.Do this only if key is smaller than other values.
                     self.widget1.canvas.axes.clear()
                     self.widget1.canvas.axes.patch.set_alpha(0)
                     self.widget1.canvas.axes.bar(self.x, self.randomArray, color='magenta', edgecolor="white",linewidth=1)
                     self.widget1.canvas.axes.bar(self.x[j], self.randomArray[j], color='black')
                     self.widget1.canvas.axes.bar(self.x[j-1], self.randomArray[j-1], color='black')
                     self.widget1.canvas.draw()
                     self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                     time.sleep(self.sort_speed)
                     QApplication.processEvents()
                     self.randomArray[j] = self.randomArray[j-1] #shift the value one position to the left
                     self.randomArray[j-1] = key  #when finish shifting the number items, our key is sorted correctly.
                     j = j -1  #reposition from right to left.
                     
                     self.butttons()
                     self.widget1.canvas.axes.clear()
                     self.widget1.canvas.axes.patch.set_alpha(0)
                     self.widget1.canvas.axes.set_title("Insertion Sort Animation",loc='left')
                     self.rects = self.widget1.canvas.axes.bar(self.x, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                     self.autolabel(self.rects)
                     self.textEdit_2.setText(str(self.randomArray))
                     self.widget1.canvas.draw()
                     self.butttons()
                     self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                     time.sleep(self.sort_speed)
                     QApplication.processEvents()
                    
               
                
                self.randomArray[j] = key 
               
            
         except AttributeError:
             QMessageBox.critical(self,"ERROR","Please select your array:")
         self.enable()
         self.plays.pause()      
                
            
    
 

#################bubble sort##################
    def bubble_sort(self): #bubble sort algorithm start
        try:
            self.disable()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
           
            for i in range(len(self.randomArray)):  #look at each items in the series one by one and check up how sort  
                for j in range(len(self.randomArray)-1-i):
                    self.widget1.canvas.axes.clear()
                    self.widget1.canvas.axes.patch.set_alpha(0)
                    self.widget1.canvas.axes.bar(self.x, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                    self.widget1.canvas.axes.bar(self.x[j], self.randomArray[j], color='black')
                    self.widget1.canvas.axes.bar(self.x[j+1], self.randomArray[j+1], color='black')
                    self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                    time.sleep(self.sort_speed)
                    QApplication.processEvents()
                        
                    if  self.randomArray[j] >  self.randomArray[j+1]: #If the item is greater than its adjacent value, then swap 
                        self.butttons()
                        key = self.randomArray[j]
                        self.randomArray[j] = self.randomArray[j+1]
                        self.randomArray[j+1] = key
                    
                        self.widget1.canvas.axes.clear()
                        self.widget1.canvas.axes.patch.set_alpha(0)
                        self.widget1.canvas.axes.set_title("Bubble Sort Animation",loc='left')
                        self.widget1.canvas.axes.bar(self.x, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                        self.widget1.canvas.axes.bar(self.x[j], self.randomArray[j], color='black')
                        self.widget1.canvas.axes.bar(self.x[j+1], self.randomArray[j+1], color='black')
                        self.textEdit_2.setText(str(self.randomArray))
                        self.widget1.canvas.draw()
                        self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                        time.sleep(self.sort_speed)
                        QApplication.processEvents()
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.widget1.canvas.axes.set_title("Bubble Sort Animation",loc='left')
            self.rects = self.widget1.canvas.axes.bar(self.x, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.textEdit_2.setText(str(self.randomArray))
            self.widget1.canvas.draw()
            self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
            time.sleep(self.sort_speed)
            QApplication.processEvents()
        
        except AttributeError:
            QMessageBox.critical(self,"ERROR","Please select your array:")
        self.enable()
        self.plays.pause()
                
     ############ merge sort ################  
    def merge_sort(self):
         try:
            self.disable()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
            randomArray = self.randomArray
            self.mergeSort(randomArray, 0, len(self.randomArray)-1)
         except AttributeError:
            QMessageBox.critical(self,"ERROR","Please select your array:")
         self.enable()
         self.plays.pause()
            
        
    def mergeSort(self, randomArray,p,r):
            if p < r: 
                q = (p+(r-1))//2  #same as (p+r)//2, but avoids overflow for 
                self.mergeSort(randomArray, p, q) 
                self.mergeSort(randomArray, q+1, r) 
                self.merge(randomArray, p, q, r)  
            return randomArray
        
    def merge(self,randomArray,p,q,r):
       
            t = np.linspace(1, len(self.randomArray), len(self.randomArray))
            n1 = q - p +1                                                          #first subarray is arr[p..q]. 
            n2 = r - q                                 
            left_side = [0] * (n1+1)                                               #create arrays.
            right_side = [0] * (n2+1)
            for i in range(0 , n1):                                                #copy data to te arrays.
                left_side[i] = randomArray[p + i]
            for j in range(0 , n2):                                                #copy data to te arrays.
                right_side[j] = randomArray[q + 1 + j]
            left_side[n1]=(np.inf)
            right_side[n2]=(np.inf)
            i = 0                                                                  #first half of array.
            j = 0                                                                  #second half of array. 
        
                
            for k in range(p, r+1): 
                if left_side[i] <= right_side[j]:  
                    randomArray[k] = left_side[i] #copy the left out elements of left half.
                    i += 1
                    self.butttons()
                    self.widget1.canvas.axes.clear()
                    self.widget1.canvas.axes.patch.set_alpha(0)
                    self.widget1.canvas.axes.bar(t, randomArray, color='magenta',edgecolor="white",linewidth=1)
                    self.widget1.canvas.axes.bar(t[k], randomArray[k], color='black')
                    self.widget1.canvas.axes.bar(t[i-1], randomArray[i-1], color='black')
                    self.textEdit_2.setText(str(self.randomArray))
                    self.widget1.canvas.draw()
                    self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                    time.sleep(self.sort_speed)
                    QApplication.processEvents()
                         
                else:
                    randomArray[k] = right_side[j]  #copy the left out elements of right half. 
                    j += 1
                    self.widget1.canvas.axes.clear()
                    self.widget1.canvas.axes.patch.set_alpha(0)
                    self.widget1.canvas.axes.bar(t, randomArray, color='magenta',edgecolor="white",linewidth=1)
                    self.widget1.canvas.axes.bar(t[k], randomArray[k], color='black')
                    self.widget1.canvas.axes.bar(t[j-1], randomArray[j-1], color='black')
                    self.textEdit_2.setText(str(self.randomArray))
                    self.widget1.canvas.draw()
                    self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                    time.sleep(self.sort_speed)
                    QApplication.processEvents()
            
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.widget1.canvas.axes.set_title("Merge Sort Animation",loc='left')
            self.rects = self.widget1.canvas.axes.bar(t, randomArray, color='magenta',edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
      
                
        
   #%%Heap Sort Code############    
    def heap_sort(self):
        randomArray = self.randomArray
        self.heapSort(randomArray)
    
    def heapSort(self, randomArray):
        try:
            self.disable()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
           
            n = len(randomArray)
            for i in range(n//2 -1, -1,-1):
                self.heapify(randomArray,n, i)
                self.widget1.canvas.axes.clear()
                self.widget1.canvas.axes.patch.set_alpha(0)
                self.widget1.canvas.axes.bar(self.x, randomArray, color='magenta',edgecolor="white",linewidth=1)
                self.widget1.canvas.axes.bar(self.x[i], randomArray[i], color='black')
                self.widget1.canvas.draw()
                self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                time.sleep(self.sort_speed)
                QApplication.processEvents()
                
                
                
            for i in range(n-1, 0, -1):  
                randomArray[i], randomArray[0] = randomArray[0], randomArray[i]
                self.heapify(randomArray,i,0)
                self.widget1.canvas.axes.clear()
                self.widget1.canvas.axes.patch.set_alpha(0)
                self.widget1.canvas.axes.bar(self.x, randomArray, color='magenta',edgecolor="white",linewidth=1)
                self.widget1.canvas.axes.bar(self.x[i], randomArray[i], color='red')
                self.widget1.canvas.draw()
                self.textEdit_2.setText(str(self.randomArray))
                self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                time.sleep(self.sort_speed)
                QApplication.processEvents()
               
                
                
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.widget1.canvas.axes.set_title("Heap Sort Animation",loc='left')
            self.rects = self.widget1.canvas.axes.bar(self.x, randomArray, color='magenta',edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
            self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
            time.sleep(self.sort_speed)
            QApplication.processEvents()
        except AttributeError:
           QMessageBox.critical(self,"ERROR","Please select your array:")
        self.enable()
        self.plays.pause()
                
    
            
    def heapify (self, randomArray, n, i):
       largest = i
       l = 2*i+1
       r = 2*i+2
       
       if  l < n and randomArray[l] > randomArray[i]:
           largest = l
    
       if r < n and randomArray[r] > randomArray[largest]:
           largest = r
    
    
       if largest != i:
           randomArray[largest],randomArray[i] = randomArray[i],randomArray[largest]
           self.butttons()
           self.heapify(randomArray,n,largest)
           
  
     

    #%%Quick Sort Code
    def quick_sort(self):
        try:
            self.disable()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
            randomArray = self.randomArray
            self.quickSort(randomArray, 0 , len(self.randomArray)-1)
        except AttributeError:
          QMessageBox.critical(self,"ERROR","Please select your array:")
        self.enable()
        self.plays.pause()
                
    
    def quickSort(self, randomArray, low, high): 
        t = np.linspace(1, len(self.randomArray), len(self.randomArray))
        if low < high:
           q = self.partition(randomArray, low, high)
           self.quickSort(randomArray, low, q-1)
           self.quickSort(randomArray, q+1, high)
        self.widget1.canvas.axes.clear()
        self.widget1.canvas.axes.patch.set_alpha(0)
        self.widget1.canvas.axes.set_title("Quick Sort Animation",loc='left')
        self.rects = self.widget1.canvas.axes.bar(t, randomArray, color='magenta',edgecolor="white",linewidth=1)
        self.autolabel(self.rects)
        self.textEdit_2.setText(str(self.randomArray))
        self.widget1.canvas.draw()
        self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
        time.sleep(self.sort_speed)
        QApplication.processEvents()

           
         
    def partition(self, randomArray, low, high):
        t = np.linspace(1, len(self.randomArray), len(self.randomArray))
        x= randomArray[high]
        i = (low-1)
        for j in range(low,high): 
            if randomArray[j] < x:
               i = i+1
               self.butttons()
               self.widget1.canvas.axes.clear()
               self.widget1.canvas.axes.patch.set_alpha(0)
               self.widget1.canvas.axes.bar(t, randomArray, color='magenta',edgecolor="white",linewidth=1)
               self.widget1.canvas.axes.bar(t[j], randomArray[j], color='red')
               self.widget1.canvas.axes.bar(t[i], randomArray[i], color='blue')
               self.widget1.canvas.axes.bar(t[j+1], randomArray[j+1], color='black')
               self.widget1.canvas.draw()
               self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
               time.sleep(self.sort_speed)
               QApplication.processEvents()
               randomArray[j] , randomArray[i] = randomArray[i], randomArray[j] 
               #self.butttons()
              
                
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.widget1.canvas.axes.bar(t, randomArray, color='magenta',edgecolor="white",linewidth=1)
            self.widget1.canvas.axes.bar(t[i], randomArray[i], color='red')
            self.widget1.canvas.axes.bar(t[high], randomArray[high], color='black')
            self.widget1.canvas.axes.bar(t[j+1], randomArray[j+1], color='blue')
            self.widget1.canvas.draw()
            self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
            time.sleep(self.sort_speed)
            QApplication.processEvents()
              
        randomArray[i+1], randomArray[high] = randomArray[high], randomArray[i+1]
        self.textEdit_2.setText(str(self.randomArray))
        return i+1
    
        
    #%% bucket sort
    def bucket_sort(self,randomArray):
        try:
            self.disable()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
            t = np.arange(len(self.randomArray))
            max_array_value = max(self.randomArray)
            size = max_array_value/len(self.randomArray)
            B = []
            
            for x in range(len(self.randomArray)): 
                B.append([])
            
            for i in range(len(self.randomArray)):
                j = int(self.randomArray[i] / size)
                if j != len(self.randomArray): 
                    B[j].append(self.randomArray[i])
                else:
                    B[len(self.randomArray) -1].append(self.randomArray[i])
            
            for z in range(len(self.randomArray)):
                insertion.insertion_sort(B[z])
              
            
            B_output = []
            for x in range(len(self.randomArray)) :
                 B_output = B_output + B[x]
                 self.butttons()
           
            for i in range(len(self.randomArray)-1):
                 self.widget1.canvas.axes.clear()
                 self.widget1.canvas.axes.patch.set_alpha(0)
                 self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                 self.widget1.canvas.axes.bar(t[i], self.randomArray[i], color='black')
                 self.widget1.canvas.draw()
                 self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                 time.sleep(self.sort_speed)
                 QApplication.processEvents()
            for i in range(0, len(self.randomArray)): 
                self.randomArray[i] = B_output[i] 
                self.widget1.canvas.axes.clear()
                self.widget1.canvas.axes.patch.set_alpha(0)
                self.widget1.canvas.axes.set_title("Bucket Sort Animation",loc='left')
                self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)  
                self.widget1.canvas.axes.bar(t[i], self.randomArray[i], color='black')
                self.textEdit_2.setText(str(self.randomArray))
                self.widget1.canvas.draw()
                self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                time.sleep(self.sort_speed)
                QApplication.processEvents()   
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.widget1.canvas.axes.set_title("Bucket Sort Animation",loc='left')
            self.rects = self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)  
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
        except AttributeError:
            QMessageBox.critical(self,"ERROR","Please select your array:")
        self.enable()
        self.plays.pause()
                
    #%% radix sort
    def radix_sort(self):
        try:
            self.disable()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
            max1 = max(self.randomArray)
            exp = 1
            while max1 // exp > 0:
                self.countingSort(self.randomArray,exp)
                exp *= 10
                self.butttons()
            self.widget1.canvas.axes.clear() 
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.widget1.canvas.axes.set_title("Radix Sort Animation",loc='left')
            self.rects = self.widget1.canvas.axes.bar(self.x, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
            self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
            time.sleep(self.sort_speed)
            QApplication.processEvents() 
            self.textEdit_2.setText(str(self.randomArray))
        except AttributeError: 
            QMessageBox.critical(self,"ERROR","Please select your array:")
        self.enable()
        self.plays.pause()
                 
    def countingSort(self,array,place):
    
        count = []
        out = []
        j = len(array)-1
        for i in range(10):
            count.append(0)
        for i in range(j+1):
            out.append(0)
        for i in range (len(array)):
            count[(array[i] // place) %10] +=1
        for i in range(1,len(count)):
            count [i] += count[i-1]
       
        for i in range(len(array)):
            count[(array[j] // place) % 10] -=1
            out[count[(array[j] // place) % 10]] = array[j]
            j -= 1
            t = np.arange(len(out))
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.widget1.canvas.axes.bar(t, out, color='magenta')
            self.widget1.canvas.axes.bar(t[i], out[i], color='black')
            self.widget1.canvas.draw()
            self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
            time.sleep(self.sort_speed)
            QApplication.processEvents() 
        for i in range(len(array)):
            array[i] = out[i]
    
            
    #%% counting sort
    def counting_sort(self):
        try:
            self.disable()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
           
            t = np.arange(len(self.randomArray))
            max1 = int(max(self.randomArray)) 
            min1 = int(min(self.randomArray)) 
            range1 = max1 - min1 + 1
            count = []
            out = []
            for i in range(range1):
                count.append(0)
            for i in range(len(self.randomArray)):
                out.append(0) 
            for i in range (len(self.randomArray)):
                count[self.randomArray[i] - min1] += 1
            for i in range(1,len(count)):
                 count [i] += count[i-1]
            for i in range(len(self.randomArray)-1,-1,-1):
                 out[count[self.randomArray[i] - min1]-1] = self.randomArray[i]
                 count[self.randomArray[i] - min1] -=1 
                 self.butttons()
           
            for i in range(len(self.randomArray)-1):
                 self.widget1.canvas.axes.clear()
                 self.widget1.canvas.axes.patch.set_alpha(0)
                 self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                 self.widget1.canvas.axes.bar(t[i], self.randomArray[i], color='black')
                 self.widget1.canvas.draw()
                 self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                 time.sleep(self.sort_speed)
                 QApplication.processEvents()
            
            for i in range(0, len(self.randomArray)): 
                self.randomArray[i] = out[i] 
                self.widget1.canvas.axes.clear()
                self.widget1.canvas.axes.patch.set_alpha(0)
                self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)  
                self.widget1.canvas.axes.bar(t[i], self.randomArray[i], color='black')
                self.widget1.canvas.draw()
                self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                time.sleep(self.sort_speed)
                QApplication.processEvents()   
          
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.widget1.canvas.axes.set_title("Counting Sort Animation",loc='left')
            self.rects = self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)    
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
            self.textEdit_2.setText(str(self.randomArray))
            self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
            time.sleep(self.sort_speed)
            QApplication.processEvents()   
        except AttributeError:
            QMessageBox.critical(self,"ERROR","Please select your array:")
        self.enable()
        self.plays.pause()
                    
    
 #%%%% selection sort %%%%%%%####
    def selection_sort(self):
        try:
            self.disable()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
            t = np.linspace(1, len(self.randomArray), len(self.randomArray))
            for i in range(len(self.randomArray)): 
                min = i 
                for j in range(i+1, len(self.randomArray)): 
                    if self.randomArray[min] > self.randomArray[j]: 
                        min = j 

                        self.widget1.canvas.axes.clear()
                        self.widget1.canvas.axes.patch.set_alpha(0)
                        self.widget1.canvas.axes.set_title("Selection Sort Animation",loc='left')
                        self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                        self.widget1.canvas.axes.bar(t[j], self.randomArray[j], color='red')
                        self.widget1.canvas.draw()
                        self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                        time.sleep(self.sort_speed)
                        QApplication.processEvents()
                        
                self.randomArray[i], self.randomArray[min] = self.randomArray[min], self.randomArray[i]
                self.butttons()
                self.widget1.canvas.axes.clear()
                self.widget1.canvas.axes.patch.set_alpha(0)
                self.widget1.canvas.axes.set_title("Selection Sort Animation",loc='left')
                self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                self.widget1.canvas.axes.bar(t[i], self.randomArray[i], color='red')
                self.widget1.canvas.draw()
                self.textEdit_2.setText(str(self.randomArray))
                self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                time.sleep(self.sort_speed)
                QApplication.processEvents()
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.widget1.canvas.axes.set_title("Selection Sort Animation",loc='left')
            self.rects = self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
            self.textEdit_2.setText(str(self.randomArray))
        except AttributeError:
            QMessageBox.critical(self,"ERROR","Please select your array:")
        self.enable()
        self.plays.pause()
                
    #%%%%%% shell sort #%%%%%%%%
    def shell_sort(self):
        try:
             self.disable()
             self.plays = pyglet.media.Player()
             self.music = pyglet.media.load('bubble-sort.mp3')
             self.plays.queue(self.music)
             self.plays.play()
             t = np.arange(len(self.randomArray))
             n = len(self.randomArray) 
             gap = n//2
             while gap > 0: 
                    for i in range(gap,n): 
                        temp = self.randomArray[i] 
                        j = i 
                        self.widget1.canvas.axes.clear()
                        self.widget1.canvas.axes.patch.set_alpha(0)
                        self.widget1.canvas.axes.set_title("Shell Sort Animation",loc='left')
                        self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                        self.widget1.canvas.axes.bar(t[i], self.randomArray[i], color='black')
                        self.widget1.canvas.draw()
                        self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                        time.sleep(self.sort_speed)
                        QApplication.processEvents()
                        while  j >= gap and self.randomArray[j-gap] >temp: 
                             self.randomArray[j] = self.randomArray[j-gap] 
                             self.widget1.canvas.axes.clear()
                             self.widget1.canvas.axes.set_title("Shell Sort Animation",loc='left')
                             self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                             self.widget1.canvas.axes.bar(t[j], self.randomArray[j], color='red')
                             self.widget1.canvas.draw()
                             self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                             time.sleep(self.sort_speed)
                             QApplication.processEvents()
                             j -= gap 
                        self.randomArray[j] = temp 
                    gap //=2
                    self.butttons()
                    self.widget1.canvas.axes.clear()
                    self.widget1.canvas.axes.patch.set_alpha(0)
                    self.widget1.canvas.axes.set_title("Shell Sort Animation",loc='left')
                    self.rects = self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                    self.autolabel(self.rects)
                    self.widget1.canvas.draw()
                    self.textEdit_2.setText(str(self.randomArray))
                    self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                    time.sleep(self.sort_speed)
                    QApplication.processEvents()
        except AttributeError:
            QMessageBox.critical(self,"ERROR","Please select your array:")
        self.enable()
        self.plays.pause()
        
    ####%%%% coctail sort #%%%%%%%%%%%%%%%%%
    def cocktail_sort(self):
        try:
            self.disable()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
            n = len(self.randomArray)
            t = np.arange(len(self.randomArray))
            swapped = True
            start = 0
            end = n-1
            while (swapped == True):
                swapped = False
                for i in range(start, end):
                    if (self.randomArray[i] > self.randomArray[i + 1]):
                        self.widget1.canvas.axes.clear()
                        self.widget1.canvas.axes.patch.set_alpha(0)
                        self.widget1.canvas.axes.set_title("Shell Sort Animation",loc='left')
                        self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                        self.widget1.canvas.axes.bar(t[i], self.randomArray[i], color='red')
                        self.widget1.canvas.axes.bar(t[i+1], self.randomArray[i+1], color='blue')
                        self.widget1.canvas.draw()
                        self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                        time.sleep(self.sort_speed)
                        QApplication.processEvents()
                        self.randomArray[i], self.randomArray[i + 1] = self.randomArray[i + 1], self.randomArray[i]
                        swapped = True
                        
                    if (swapped == False): 
                        break
                    
                    swapped = False
                    end = end-1
                    
                for i in range(end-1, start-1, -1): 
                    if (self.randomArray[i] > self.randomArray[i + 1]):
                        self.widget1.canvas.axes.clear()
                        self.widget1.canvas.axes.patch.set_alpha(0)
                        self.widget1.canvas.axes.set_title("Coktail Sort Animation",loc='left')
                        self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                        self.widget1.canvas.axes.bar(t[i+1], self.randomArray[i+1], color='blue')
                        self.widget1.canvas.axes.bar(t[i], self.randomArray[i], color='red')
                        
                        self.widget1.canvas.draw()
                        self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                        time.sleep(self.sort_speed)
                        QApplication.processEvents()
                        self.randomArray[i], self.randomArray[i + 1] = self.randomArray[i + 1], self.randomArray[i]
                        swapped = True
                        
                start = start + 1
                self.widget1.canvas.axes.clear()
                self.widget1.canvas.axes.patch.set_alpha(0)
                self.widget1.canvas.axes.set_title("Cocktail Sort Animation",loc='left')
                self.rects = self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1) 
                self.autolabel(self.rects)
                self.widget1.canvas.draw()
                self.textEdit_2.setText(str(self.randomArray))
                self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                time.sleep(self.sort_speed)
                QApplication.processEvents()
        except AttributeError:
            QMessageBox.critical(self,"ERROR","Please select your array:")
        self.enable()
        self.plays.pause()
            
        #%%%%%%%% comb sort #%%%%%%%%%%%
    def comb_sort(self):
        try:
            self.disable()
            self.plays = pyglet.media.Player()
            self.music = pyglet.media.load('bubble-sort.mp3')
            self.plays.queue(self.music)
            self.plays.play()
            t = np.arange(len(self.randomArray))
            gap = len(self.randomArray)
            swaps = True
            while gap > 1 or swaps:
                gap = max(1, int(gap / 1.25))  # minimum gap is 1
                swaps = False
                for i in range(len(self.randomArray) - gap):
                    j = i+gap
                    if self.randomArray[i] > self.randomArray[j]:
                        self.widget1.canvas.axes.clear()
                        self.widget1.canvas.axes.patch.set_alpha(0)
                        self.widget1.canvas.axes.set_title("Comb Sort Animation",loc='left')
                        self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
                        self.widget1.canvas.axes.bar(t[i], self.randomArray[i], color='red')
                        self.widget1.canvas.axes.bar(t[j], self.randomArray[j], color='blue')
                        self.widget1.canvas.draw()
                        self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
                        time.sleep(self.sort_speed)
                        QApplication.processEvents()
                        self.randomArray[i], self.randomArray[j] = self.randomArray[j], self.randomArray[i]
                        swaps = True
            self.widget1.canvas.axes.clear()
            self.widget1.canvas.axes.patch.set_alpha(0)
            self.widget1.canvas.axes.set_title("Comb Sort Animation",loc='left')
            self.rects = self.widget1.canvas.axes.bar(t, self.randomArray, color='magenta',edgecolor="white",linewidth=1)
            self.autolabel(self.rects)
            self.widget1.canvas.draw()
            self.textEdit_2.setText(str(self.randomArray))
            self.sort_speed = 0.01 * (10 - self.verticalSlider.value())
            time.sleep(self.sort_speed)
            QApplication.processEvents()
        except AttributeError:
            QMessageBox.critical(self,"ERROR","Please select your array:")
        self.enable()
        self.plays.pause()
                

        