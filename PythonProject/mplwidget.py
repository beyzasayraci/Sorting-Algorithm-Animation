# -*- coding: utf-8 -*-
"""
Beyza Sayraci
31.11.2020
170403034
Plot File
"""
#%%The file and code required to print the plot on the widget.
from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
    
class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        vertical_layout = QVBoxLayout()
        self.figure = plt.figure()
        self.figure.patch.set_facecolor('None')

        self.canvas = FigureCanvas(self.figure)
        vertical_layout.addWidget(self.canvas)
        self.canvas.setStyleSheet("background-color:transparent;")
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.patch.set_alpha(0)
        self.setLayout(vertical_layout)

