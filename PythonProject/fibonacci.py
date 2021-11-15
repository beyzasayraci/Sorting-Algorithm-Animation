# -*- coding: utf-8 -*-
"""
Beyza Sayraci
170403034
29.11.2020
fibonacci main file
"""

from PyQt5.QtWidgets import *
import fib
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QMovie
class fibonacci(QMainWindow):
    
    def __init__(self):
        super().__init__() 
        
        loadUi("fibonacci.ui", self)
        
        self.pushButton_calculate.clicked.connect(self.fibonacci_calculater) #connect button.
        self.pushButton_clear.clicked.connect(self.clear) #create plot.
        #self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
        self.setFixedSize(1200, 865)
        self.setWindowTitle("FIBONACCI")
        self.MplWidget.canvas.axes.xaxis.set_visible(False)
        self.MplWidget.canvas.axes.yaxis.set_visible(False)
        self.pushButton_clear_2.clicked.connect(self.close)
        self.pushButton_clear_2.setIcon(QIcon("icons/25694 (1).png"))
        self.pushButton_clear.setIcon(QIcon("icons/img_185728.png"))
        self.pushButton_calculate_2.clicked.connect(self.golden_ratio)
        self.gif = QMovie("icons/unnamed.gif")
        self.label_4.setMovie(self.gif)
        self.gif.start()
        self.gif1 = QMovie("icons/text (10).gif")
        self.label_5.setMovie(self.gif1)
        self.gif1.start()

    #%% #fibonacci func.   
    def fibonacci_calculater(self):
        try:
            self.label_5.setVisible(False)
            self.number = self.spinBox_array.value() #input number
            self.fibonacci_result = fib.Fibonacci(self.number)  #Calling the fibonacci function.
            self.textEdit_answer.setText(str(self.fibonacci_result)) #printing text edite.
           #%%to show you the whole array.  
            fibonacciSeries = [0,1]
            if self.number>2:
                for i in range(2, self.number):
                    nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2] #to go by adding the elements together.
                    fibonacciSeries.append(nextElement) #add numbers to list.
            self.textEdit_2.setText(str(fibonacciSeries))
            self.x = []
            for i in range(len(fibonacciSeries)):
                self.x.append(i+1)    
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.patch.set_alpha(0)
            self.rects = self.MplWidget.canvas.axes.bar(self.x, fibonacciSeries, color="cyan") #create plot
            self.autolabel(self.rects)
            self.MplWidget.canvas.axes.set_title('Fibonacci Series Bar')
            self.MplWidget.canvas.draw()
        except : 
            QMessageBox.critical(self,"Error","Please select your Fibonacci Index..")
    
    def clear(self):
        self.textEdit_answer.clear()
        self.spinBox_array.setValue(0)
        self.textEdit_2.clear()
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.patch.set_alpha(0)
        self.MplWidget.canvas.draw()
        self.fibonacci_result = []
        self.golden_ratio = []
        self.widget1.canvas.axes.clear()
        self.widget1.canvas.axes.patch.set_alpha(0)
        self.widget1.canvas.draw()
        self.number = []
        fibonacciSeries = []
        self.label_4.setVisible(True)
        self.label_5.setVisible(True)
        
     
    def autolabel(self,rects):
        for rect in self.rects:
            height = rect.get_height()
            self.MplWidget.canvas.axes.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                    '%d' % int(height),
            ha='center', va='bottom',color='black', fontweight='bold')
    
    def golden_ratio(self):
        self.label_4.setVisible(False)
        n = 30
        fiblist = [0,1]
        for i in range(n - 1):
            fiblist.append(fiblist[i] + fiblist[i+1])
        
        self.golden_ratio = [fiblist[i]/float(fiblist[i-1]) for i in range(2,len(fiblist))]
        self.widget1.canvas.axes.clear()
        self.widget1.canvas.axes.patch.set_alpha(0)
        self.widget1.canvas.axes.plot(self.golden_ratio, color="black")
        self.widget1.canvas.axes.set_title('Golden Ratio')
        self.widget1.canvas.draw()
            
            
            

        
 
