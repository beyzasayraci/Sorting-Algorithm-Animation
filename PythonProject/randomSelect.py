# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:05:49 2020

@author: pc
"""
import random


class InputArray ():
    def __init__(self):
        pass
    
    
   
    def randomArray(self):
        array = []                                                             #empty array list
        a = int(input("How many numbers do the list contain? : "))             #how many value?
        b = int(input("What value should the list not be less than? : "))      #what is the smallest value?
        c = int(input("What value should the list not be bigger than? : "))    #what is the greatest value?
        for i in range(a):
            values = random.randint(b,c)                                       #random array.
            array.append(int(values))                                          #adding given values to the list.
        return array  
            
    def inputYourArray(self):                                                  #get array from user.
        array = []                                                             #empty array list.
        element = input("Enter the values seperated by comma: ")               #enter your values.
        array_elements = element.split(",")
        for i in array_elements:
            array.append(int(i))                                               #adding given values to the list.
        return array
        
    
class SelectAlgorithm (): 
    
    def __init__ (self):
        pass    
    
    
    def partition (self,array,low,high):
        x = array [high] 
        i = low
        for j in range(low, high): 
              
            if array[j] <= x: 
                array[i], array[j] = array[j], array[i] 
                i = i + 1
                  
        array[i], array[high] = array[high], array[i] 
        return i
    
   
    def ith_smallest(self,array, low, high, k): 
        if (k > 0 and k <= high - low + 1):  
           
            index = self.partition(array, low, high) 
   
            if (index - low == k - 1): 
                return array[index] 
  
            if (index - low > k - 1): 
                return self.ith_smallest(array, low, index - 1, k) 
  
            return self.ith_smallest(array, index + 1, high,k - index + low - 1) 
           