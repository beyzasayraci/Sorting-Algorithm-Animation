# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:35:23 2020

@author: pc
"""

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  

  
# Function to do Quick sort 
def quick_sort(arr,low,high): 
    if low < high: 
  
        pivot = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort(arr, low, pivot-1) 
        quick_sort(arr, pivot+1, high)