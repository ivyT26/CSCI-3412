#!/usr/bin/env python
# coding: utf-8

# # Time Efficiency Function with Decorator

# In[3]:


#Name: Ivy Truong
#Class: CSCI 3412
#Date Created: 2/3/2020
#Homework 1: Simulating Algorithms

#time efficiency function with decorator
import time

#decorators add more functionality to existing code
#allows us to just call a function rather than pass a function to another function to do more stuff
def decorator(func):
    def timeEfficiency():
        startTime = time.process_time()
        
        func()
        
        endTime = time.process_time()
        
        print("Start Time:", startTime)
        print("End Time:", endTime)
        print("Time taken to execute function:", endTime - startTime)
    return timeEfficiency

#@decorator decorates the function/adds more to to the implementation of original function
@decorator
def sumUp():
    result = 0
    maxNum = int(input("Enter a large number greater than 0.\n"))
    #below will add up all the numbers between 0 and maxNum
    for number in range(maxNum + 1):
        result = result + number
    print("Sum:", result)

sumUp()

