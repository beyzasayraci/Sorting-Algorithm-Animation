# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:33:09 2020

@author: pc
"""
import random
from time import time
import numpy as np  
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
class SortAlgorithm (): 
    
    def __init__ (self):
        pass    
   
    
   ###########insertion sort##################
    def insertion_sort(self,array):                                            #insertion algorithm start 
        for i in range (1,len(array)):                                         #the first number is sorted.skip the first number.
            key = array[i]                                                     #set a key value.
            j = i-1                                                            #run through the list of items.  
            while j >= 0 and array[j] > key:                                   #find the correct position.compare the smaller and greater of the numbers.Do this only if key is smaller than other values.  
                array[j+1] = array[j]                                          #shift the value one position to the left
                j = j -1                                                       #reposition from right to left.
                
            array[j+1] = key                                                   #when finish shifting the number items, our key is sorted correctly.
        return array
       
        
            
   
    ############merge sort####################3 
    def merge_sort(self,array):# method for merge sort
        self.recursive_merge(array,0,len(array)-1)#define a first recursive function and send array,first index and a last index as a parameter
        return array # return that to use this array on main file
    def recursive_merge(self,array,first_index,last_index):#first recursive function
        if(last_index>first_index):# if last index greater than first index we can say array has more than one element
            middle_index=(first_index+last_index)//2#floor the average of the first and last indices
            self.recursive_merge(array,first_index,middle_index)#divide the array two parts and send right of the real array send this into the our first recursive function
            self.recursive_merge(array,middle_index+1,last_index)#divide the array two parts and send left of the real array send this into the our first recursive function
            self.merge(array,first_index,middle_index,last_index)#this second recursive function will combine the sorted arrays returning from above definitions
    def merge(self,array,first_index,middle_index,last_index):#define a second function with parameters first,middle and last index besides array
        leftArray=array[first_index:middle_index+1]#left half of the array
        rightArray=array[middle_index+1:last_index+1]#right half of the array
        leftArray.append(np.inf)#add a very large number so that we know when we reach the end of the subarrays
        rightArray.append(np.inf)#add a very large number so that we know when we reach the end of the subarrays
        i=j=0#indexis for subarrays
        for k in range(first_index,last_index+1):#for loop starts with first index of the real array and ends with the last index of real array
            if(leftArray[i]<=rightArray[j]):#comparing the subarrays if the left array's ith elements is smaller than right array's jth element 
                array[k]=leftArray[i]#than insert the left array's ith element to the real array's kth index
                i+=1#increment the left index by one
            else:
                array[k]=rightArray[j]#in else situation we insert the right array's jth element to the real arrays k'th index
                j+=1#increment the right index by one
        
     
       
    ##############bubble sort##########################3  
    def bubble_sort(self,array):                                               #bubble sort algorithm start
        for i in range(len(array)-1):                                          #look at each items in the series one by one and check up how sort  
            for j in range(len(array) -1 -i):                                  
                if  array[j] >  array[j+1]:                                    
                      array [j] ,  array [j+1] = array[j+1], array[j]          #If the item is greater than its adjacent value, then swap 
        return array
                
        
     ##############heap sort#####################           
    def heap_sort(self,array):
        n=len(array)
        for i in range(n//2 - 1, -1, -1): 
            self.heapify(array, n, i)
        for i in range(n-1, 0, -1): 
            array[i],array[0] = array[0],array[i] # swap 
            self.heapify(array, i, 0)
        # return array
    def heapify(self,arr,n,i):
        largest = i # Initialize largest as root 
        left = 2 * i + 1     # left = 2*i + 1 
        right = 2 * i + 2     # right = 2*i + 2 
        if left < n and arr[i] < arr[left]: 
            largest = left
        if right < n and arr[largest] < arr[right]: 
            largest = right
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] # swap 
            self.heapify(arr, n, largest)
   
    ###################selection sort###########3         
    def selection_sort(self,array):
        for i in range(len(array)):
            min_index=i
            for j in range(i+1,len(array)):
                if(array[min_index]>array[j]):
                    min_index=j
            array[i],array[min_index]=array[min_index],array[i]
    
            
    ##########quick sort#############
    def quick_sort(self,array,first_index,last_index):
        if first_index<last_index:
            part_index=self.partition(array,first_index,last_index)
            self.quick_sort(array,first_index,part_index-1)
            self.quick_sort(array,part_index+1,last_index)
      
    def partition(self,arr,first_index,last_index):
        i=(first_index-1)
        pivot=arr[last_index]
        for j in range (first_index,last_index):
            if arr[j]<pivot:
                i+=1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[last_index] = arr[last_index],arr[i+1]
        return ( i+1 )
    
    #############bucket sort##############
    def bucket_sort(self,array):
        max_element=max(array)
        size = max_element/len(array)
        arr=[]
        for i in range(len(array)): 
            arr.append([]) 
            
        for i in range(len(array)):
            j = int (array[i] / size)
            if j != len (array):
                arr[j].append(array[i])
            else:
                arr[len(array) - 1].append(array[i])
        for z in range(len(array)):
            self.insertion_sort(arr[z])
        result = []
        for x in range(len (array)):
            result += arr[x] 
        for i in range(0, len(array)): 
            array[i] = result[i] 
       
    ##########radix sort####################
    def radix_sort(self,array):
        max1 = max(array)
        exp = 1
        while max1 // exp > 0: 
            self.counting_sort_radix(array, exp) 
            exp *= 10
        # return array
    def counting_sort_radix(self,arr,pos):
        count = []
        arr_b = []
        j = len(arr) - 1
        for i in range(10):
            count.append(0)
        for i in range(len(arr)):
            arr_b.append(0)
        for i in range(len(arr)):
            count[(arr[i] // pos) % 10] += 1
        for i in range(len(count)):
            if i > 0:
                count[i] += count[i - 1]
        for i in range(len(arr)):
            count[(arr[j] // pos) % 10] -= 1
            arr_b[count[(arr[j] // pos) % 10]] = arr[j]
            j -= 1
        for i in range(len(arr)):
            arr[i] = arr_b[i]
            
            
    #############counting sort##################
    def counting_sort(self,array):
        max_element = int(max(array)) 
        min_element = int(min(array))
        range_of_elements = max_element - min_element + 1
        count_arr = [0 for _ in range(range_of_elements)] 
        output_arr = [0 for _ in range(len(array))]
        for i in range(0, len(array)): 
            count_arr[array[i]-min_element] += 1
        for i in range(1, len(count_arr)): 
            count_arr[i] += count_arr[i-1]
        for i in range(len(array)-1, -1, -1): 
            output_arr[count_arr[array[i] - min_element] - 1] = array[i] 
            count_arr[array[i] - min_element] -= 1
        for i in range(0, len(array)): 
            array[i] = output_arr[i] 
            
class times():
    def __init__(self):# set the initializer method
        self.n=[100,200,700,2000]#define random array lengths
        
    def create_array(self,length,maximum):#define a random array creator function
        random.seed(0)
        random.sample
        self.new_array=[random.randint(0, maximum)for i in range(length)] #create a random array between -500 and maximum
        return self.new_array# return that to use this array on below
    def comparison(self,situations):
        self.times={"Bubble":[],"Insertion":[],"Merge":[],"Selection":[],"Counting":[],"Heap":[],"Bucket":[],"Radix":[],"Quick":[]}#create a dictionary that holds sorting algorithm names
        for size in self.n:#for loop for send the array's lengths as a parameters 
            if situations[0]:
                array=self.create_array(size,size)#create array
                t0=time()#take the time before the sorting
                SortAlgorithm().bubble_sort(array)#make bubble sorting
                t1=time()#take the time after the sorting
                self.times["Bubble"].append(t1-t0)#add this time to a dictionary where Bubble's location
                
            if situations[1]:
                array=self.create_array(size,size)#create array
                t0=time()#take the time before the sorting
                SortAlgorithm().insertion_sort(array)#make insertion sorting
                t1=time()#take the time after the sorting
                self.times["Insertion"].append(t1-t0)#add this time to a dictionary where Insertion's location
            
            if situations[2]:
                array=self.create_array(size,size)#create array
                t0=time()#take the time before the sorting
                SortAlgorithm().merge_sort(array)#make merge sorting
                t1=time()#take the time after the sorting
                self.times["Merge"].append(t1-t0)#add this time to a dictionary where Merge's location
            
            if situations[3]:
                array=self.create_array(size,size)#create array
                t0=time()#take the time before the sorting
                SortAlgorithm().selection_sort(array)#make merge sorting
                t1=time()#take the time after the sorting
                self.times["Selection"].append(t1-t0)#add this time to a dictionary where Selection's location
            
            if situations[4]:
                array=self.create_array(size,size)#create array
                t0=time()#take the time before the sorting
                SortAlgorithm().counting_sort(array)#make merge sorting
                t1=time()#take the time after the sorting
                self.times["Counting"].append(t1-t0)#add this time to a dictionary where Counting's location
                
            if situations[5]:
                array=self.create_array(size,size)#create array
                t0=time()#take the time before the sorting
                SortAlgorithm().heap_sort(array)#make merge sorting
                t1=time()#take the time after the sorting
                self.times["Heap"].append(t1-t0)#add this time to a dictionary where Heap's location
                
            if situations[6]:    
                array=self.create_array(size,size)#create array
                t0=time()#take the time before the sorting
                SortAlgorithm().bucket_sort(array)#make merge sorting
                t1=time()#take the time after the sorting
                self.times["Bucket"].append(t1-t0)#add this time to a dictionary where Bucket's location
                
            if situations[7]:
                array=self.create_array(size,size)#create array
                t0=time()#take the time before the sorting
                SortAlgorithm().radix_sort(array)#make merge sorting
                t1=time()#take the time after the sorting
                self.times["Radix"].append(t1-t0)#add this time to a dictionary where Radix's location
            
            if situations[8]:
                array=self.create_array(size,size)#create array
                t0=time()#take the time before the sorting
                SortAlgorithm().quick_sort(array,0,len(array)-1)#make merge sorting
                t1=time()#take the time after the sorting
                self.times["Quick"].append(t1-t0)#add this time to a dictionary where Quick's location
        return self.times
    
class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self,option,index):
         super(AlignDelegate, self).initStyleOption(option, index)
         option.displayAlignment = QtCore.Qt.AlignCenter