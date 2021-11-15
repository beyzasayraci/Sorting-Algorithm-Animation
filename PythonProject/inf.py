# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:51:03 2020

@author: pc
"""
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
import webbrowser
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QMovie
class Information(QWidget):
    def __init__(self):
        super().__init__() 
        
        loadUi("information.ui", self)
        self.pushButton.clicked.connect(self.sort)
        self.pushButton_2.clicked.connect(self.matrix)
        self.pushButton_3.clicked.connect(self.binary)
        self.pushButton_4.clicked.connect(self.fib)
        self.pushButton_5.clicked.connect(self.rs)
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.linkedin)
        self.pushButton_7.setIcon(QIcon("icons/61109.png"))
        self.setWindowTitle("Information")
        self.pushButton.setIcon(QIcon('icons/fq0A8hx.gif'))
        self.pushButton_2.setIcon(QIcon("icons/images (4).png"))
        self.pushButton_3.setIcon(QIcon("icons/Binary-Search.png"))
        self.pushButton_4.setIcon(QIcon("icons/png.jpg"))
        self.pushButton_5.setIcon(QIcon("icons/Screenshot 2015-07-07 19.39.35.png"))
        self.pushButton_6.setIcon(QIcon("icons/exit.jpg"))
        self.setFixedSize(745, 637)


        
    def sort(self):
         webbrowser.open('https://brilliant.org/wiki/sorting-algorithms/')
         
    def matrix(self):
        webbrowser.open('https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:multiplying-matrices-by-matrices/a/multiplying-matrices')
        
    def binary(self):
        webbrowser.open('https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search')
    def fib(self):
        webbrowser.open('https://www.mathsisfun.com/numbers/fibonacci-sequence.html')
    def rs(self):
        webbrowser.open('https://people.engr.tamu.edu/andreas-klappenecker/csce411-s15/csce411-random4.pdf')
    def linkedin(self):
         webbrowser.open('https://www.linkedin.com/in/beyzasayraci/')
        
        
