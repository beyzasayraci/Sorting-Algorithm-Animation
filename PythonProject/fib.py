# -*- coding: utf-8 -*-
"""
Beyza Sayraci
29.11.2020
fibonacci code
"""
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    
    elif n==1:#First Fibonacci number is equal to 0.
        return 0
    
    elif n==2: #Second Fibonacci number is equal to 1
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2) #fibonnacci formula  0+1=1 1+1=2 so 0 1 1 2
 