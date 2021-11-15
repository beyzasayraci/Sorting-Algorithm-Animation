# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 02:42:58 2020

@author: pc
"""
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

class Array(QWidget):
    def __init__(self):
        super().__init__() 
        array = [] 
        
    def load_ui(self):
         self.created_list = uic.loadUi("create_array.ui", self)
        
        
    
    def create_number(self):
        try:
                                                                       #empty array list.
            element = self.lineEdit.text()                                         #enter your values.
            array_elements = element.split(",")
            for i in array_elements:
                array.append(int(i))                                               #adding given values to the list.
            return array
        except:
            self.label.setText("Value must be int")
            
    def clear(self):
        self.lineEdit.clear()
        self.label.clear()
            
    def create_number(self):
        self.close()
        return  self.randomArray

def run():
    app = QtWidgets.QApplication(sys.argv)  # call Aplication
    window = Array()  # call window class
    window.load_ui()
    window.show()
    sys.exit(app.exec())  # enter infinity loop


if __name__ == "__main__":  # run if only script is main
    run()  # call run function