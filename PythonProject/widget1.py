# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 12:56:37 2020

@author: pc
"""
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class widget1(QWidget):

    def __init__(self, parent=None):
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


    