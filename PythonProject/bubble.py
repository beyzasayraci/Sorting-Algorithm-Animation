# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:32:08 2020

@author: pc
"""
def bubble(list):
    for j in range(len(list)-1):
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]: #compare the number the the next number
                list[i], list[i + 1] = list[i + 1], list[i] 