# -*- coding: utf-8 -*-
"""
Beyza Sayraci
170403034
29.11.2020
insertion sort function for binary search
"""
def insertion_sort(array):                                                     #insertion algorithm start 
        for i in range (1,len(array)):                                         #the first number is sorted.skip the first number.
            key = array[i]                                                     #set a key value.
            j = i-1                                                            #run through the list of items.  
            while j >= 0 and array[j] > key:                                   #find the correct position.compare the smaller and greater of the numbers.Do this only if key is smaller than other values.  
                array[j+1] = array[j]                                          #shift the value one position to the left
                j = j -1                                                       #reposition from right to left.
            array[j+1] = key                                                   #when finish shifting the number items, our key is sorted correctly.
        return array
    
