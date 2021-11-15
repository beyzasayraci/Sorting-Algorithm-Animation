# -*- coding: utf-8 -*-
"""
Beyza Sayraci
31.11.2020
170403034

"""
#%% main file
from PyQt5.QtWidgets import QApplication
from main_page import MainPage





app = QApplication([])
window= MainPage()
window.show()
app.exec_()         
