# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:34:43 2020

@author: pc
"""
def merge(A): #creating function
    merge_sort(A,0,len(A)-1)

def merge_sort(A,first_ind,last_ind): #dividing the list into 2 halfes.
    if(first_ind<last_ind):
        # finding middle index.
        mid = (first_ind+last_ind)//2
        merge_sort(A,first_ind,mid)
        merge_sort(A,mid+1,last_ind)
        mergesort(A,first_ind,mid,last_ind) #combining sorted lists.

def mergesort(A,first_ind,mid,last_ind):
    L = A[first_ind:mid+1] #left side of list.
    R = A[mid+1:last_ind+1] # right side of list.
    L.append(999999999) #adding the last index almost infinite number.
    R.append(999999999) #adding the last index almost infinite number.
    i=0
    j=0

    for k in range (first_ind,last_ind+1):
         if L[i] <= R[j]: #comparison between righ and left side of lists and
             A[k] = L[i]  #ordering them.
             i = i + 1
         else:
             A[k]=R[j]
             j = j + 1
