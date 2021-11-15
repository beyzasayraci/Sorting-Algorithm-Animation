# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:32:37 2020

@author: pc
"""
import insertion
import math
def bucket(array, bucketSize = 100):
  if len(array) == 0: #if length of array 0 return array
    return array

  # Determine minimum and maximum values of the array 
  min_val = array[0]
  max_val = array[0]
  for i in range(1, len(array)):
    if array[i] < max_val:
      min_val = array[i]
    elif array[i] > max_val:
      max_val = array[i]

  # Initialize buckets
  bucketCount = math.floor((max_val - min_val) / bucketSize) + 1
  buckets = []
  for i in range(0, bucketCount):
    buckets.append([])

  # Distribute input array values into buckets
  for i in range(0, len(array)):
    buckets[math.floor((array[i] - min_val) / bucketSize)].append(array[i])

  # Sort buckets and place back into input array
  array = []
  for i in range(0, len(buckets)):
    insertion.insertion_sort(buckets[i])
    for j in range(0, len(buckets[i])):
      array.append(buckets[i][j])

  return array