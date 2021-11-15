# -*- coding: utf-8 -*-
"""
Beyza Sayraci
170403034
29.11.2020
Binary Search Function
"""
def Binary_Search(arr, low, high, x): 
    
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return Binary_Search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return Binary_Search(arr, mid + 1, high, x) 
  
    # else: 
    #     # Element is not present in the array 
    #     return -1
  
