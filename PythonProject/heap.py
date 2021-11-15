# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:34:20 2020

@author: pc
"""
def heap(arr, n, i): 
    pivot = i     # Initialize largest as pivot
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left side of root exists and is 
    # greater than pivot 
    if l < n and arr[i] < arr[l]: 
        pivot = l 
  
    # See if right child of pivot exists and is 
    # greater than root 
    if r < n and arr[pivot] < arr[r]: 
        pivot = r 
  
    # Change root, if needed 
    if pivot != i: 
        arr[i],arr[pivot] = arr[pivot],arr[i]  # swap 
  
        # Heapify the root. 
        heap(arr, n, pivot)
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heap(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heap(arr, i, 0) 