#!/usr/bin/env python
# coding: utf-8

# # Name: Ivy Truong
# # Class: CSCI 3412
# # Date Created: 2/17/2020
# # Homework 2

# # Part 1: HTML Table

# In[6]:


#functions to calculate math for each row in the table
import math
from decimal import *

#assuming base 2 for log functions
#solve using time in microseconds

#timeArray holds time in milliseconds for 1 second, 1 minute, 1 hour, 1 day, 1 month, 1 year, and 1 century
#calculations assume that there are 30 day/month and 365 days/year
#used to calculate math functions later
def setTimesMilli(numSec):
    arr = []
    #converts it into milliseconds
    numSec *= 1000
    #appends time for 1 second in milliseconds
    arr.append(int(numSec))
    #calculate 1 minute in milliseconds
    numSec *= 60
    arr.append(int(numSec))
    #calculate 1 hour in milliseconds
    numSec *= 60
    arr.append(int(numSec))
    #calculate 1 day in milliseconds
    numSec *= 24
    arr.append(int(numSec))
    #calculate 1 month in milliseconds
    numSec *= 30
    arr.append(int(numSec))
    #calculate 1 year in milliseconds
    numSec *= 24
    arr.append(int(numSec))
    #calculate 1 century in milliseconds
    numSec *= 100
    arr.append(int(numSec))
    return arr

#n = 2^(time)
def calcLog(array):
    tempArr = []
    for i in range(len(array)):
        #when trying to do the inverse of log(n) or 2^(time), the value was too big and kept giving a math range error or overflow error
        #I've tried it with numpy.float_scientific and decimal format and cutting the number of digits in the scientific notation, but it did not do anything
        #so I am recording these values as infinite to represent the extremely large numbers (my previous code for calculations will be commented out)
        #the code is replaced with recording infinite as the answer to the function problems
        
        #if math.isfinite(math.pow(2,array[i])):
        #val = numpy.format_float_scientific(math.pow(2,array[i]),precision=3,unique=True)
        #val = str("{0:.2e}".format(math.pow(2,array[i])))
        
        #writes the infinity symbol for numbers out of range of python/to indicate that the size n is very large
        #tempArr.append("&#8734")
        
        #since python does not support very large numbers, the value will be represented as 2^t, where t is the time
        tempStr = "2<sup>" + str(array[i]) + "</sup>"
        tempArr.append(tempStr)
    return tempArr

#n = (time)^2    
def calcRoot(array):
    tempArr = []
    for i in range(len(array)):
        #format function allows us to write a number in scientific notation or reduce the number of decimal places that should be printed out
        tempArr.append(str("{0:.2e}".format(math.pow(array[i],2))))
    return tempArr

def calcN(array):
    tempArr = []
    for i in range(len(array)):
        tempArr.append(str("{0:.2e}".format(array[i])))
    return tempArr

def calcNLogN(array):
    #Source for method: https://math.stackexchange.com/questions/1301343/how-to-find-the-inverse-of-n-log-n
    #used Newton's Method/linear approximation to get an approximation for each value
        #if f(n) = nlog(n), then f'(n) = log(n) + (1/ln(2)) or n = t/log(t)
    tempArr = []
    for i in range(len(array)):
        previousVal = 0 #resets value when calculating for new size n of time t
        currentVal = array[i]
        while currentVal != previousVal:
            previousVal = currentVal
            currentVal = currentVal/(math.log2(previousVal))
        tempArr.append(str(currentVal)) 
    return tempArr

#n = sqrt(time)
def calcN2(array):
    tempArr = []
    for i in range(len(array)):
        tempArr.append(str("{0:.2e}".format(math.sqrt(array[i]))))
    return tempArr

#n = (time)^(1/3)
def calcN3(array):
    tempArr = []
    for i in range(len(array)):
        tempArr.append(str("{0:.2e}".format(math.pow(array[i],(1/3)))))
    return tempArr

#n = log(time)
def calc2N(array):
    tempArr = []
    for i in range(len(array)):
        tempArr.append(str("{0:.2e}".format(math.log2(array[i]))))
    return tempArr

#n = last divisor of time
def calcFactorial(array):
    tempArr = []
    #source for inverse factorial method: https://www.quora.com/What-is-the-inverse-of-factorial
    for i in range(len(array)):
        #keep dividing by every number until it reduces to 1, last divisor becomes the value of n
        value = array[i]
        n = 2
        while value > 1:
            value = value/n
            #checks if the value is close to 1 (not all divisions will get exactly 1, so these values will give approximations, some size n will be off by + or - 1)
            if math.floor(value) == 1:
                tempArr.append(str(n))
                break;
            elif math.ceil(value) == 1:
                #usually values here are closer to zero, therefore the value of n would be larger than the time allocated, 
                #so have to subtract the size by 1 to get it closer to desired value (we want the largest size n that can run the function under the time frame) 
                tempArr.append(str(n-1))
                break;
            n += 1
    return tempArr

#below are arrays for the times in milliseconds and for calculating the values based on each math function performed
timeArray = setTimesMilli(1)
lognArray = calcLog(timeArray)
rootnArray = calcRoot(timeArray)
nArray = calcN(timeArray) 
nlognArray = calcNLogN(timeArray)
n2Array = calcN2(timeArray)
n3Array = calcN3(timeArray)
b2nArray = calc2N(timeArray)
nFacArray = calcFactorial(timeArray)

def writeData(array):
    for i in range(0,7):
        file.write("<td>")
        file.write(array[i])
        file.write("</td>")

        
file = open("HW2Pt1.html", "w")
file.write("<!--Table format for python calculations-->")
file.write("\n<!DOCTYPE HTML5>")
file.write("<html>")

file.write("\n<!--Below will set table styling attributes to make it look more legible-->")
file.write("<!--<style>implements formatting and decorating aspects of HTML document(makes things look pretty)-->")
file.write("<style>")
file.write("th,td{")
file.write("padding: 10px; /*Padding defines a space between the text and the border*/")
file.write("border: 1px solid black; /*Border defines a border based on thickness and the type of line the user wants to display*/")
file.write("width: 13%; /*Width defines how wide the area should be(in this case it is the cells in the table*/")
file.write("}")
file.write("</style>")

file.write("\n<!--<table> creates a table-->")
file.write("<table style = \"width:100%;\">")
file.write("<!--Caption allows us to write a title or caption for the table-->")
file.write("<!--<b> allows us to write bold text-->")
file.write("<caption style = \"font-size:150%;\"><b>Comparison of Running Times</b></caption>")
file.write("<!--<tr> creates a table row-->")
file.write("<!--This is the first row of table(headers)-->")
file.write("<tr>")
file.write("<!--<th> creates a table header-->")
file.write("<th></th>")
file.write("<th>1 Second</th>")
file.write("<th>1 Minute</th>")
file.write("<th>1 Hour</th>")
file.write("<th>1 Day</th>")
file.write("<th>1 Month</th>")
file.write("<th>1 Year</th>")
file.write("<th>1 Century</th>")
file.write("</tr>")

file.write("<!--This is the second row of the table(log(n))-->")
file.write("<tr>")
file.write("<th>log(n)</th>")
file.write("<!--<td> creates a data cell in the table-->")
writeData(lognArray)
file.write("</tr>")

file.write("<!--This is the third row of the table(sqrt(n))-->")
file.write("<tr>")
file.write("<!--&#8730 is the HTML code for the square root function-->")
file.write("<th>&#8730n</th>")
writeData(rootnArray)
file.write("</tr>")

file.write("<!--This is the fourth row of the table(n)-->")
file.write("<tr>")
file.write("<th>n</th>")
writeData(nArray)
file.write("</tr>")

file.write("<!--This is the fifth row of the table(nlog(n))-->")
file.write("<tr>")
file.write("<th>nlog(n)</th>")
writeData(nlognArray)
file.write("</tr>")

file.write("<!--This is the sixth row of the table(n^2)-->")
file.write("<tr>")
file.write("<!--&#178 is the HTML code for superscript 2-->")
file.write("<th>n&#178</th>")
writeData(n2Array)
file.write("</tr>")

file.write("<!--This is the seventh row of the table(n^3)-->")
file.write("<tr>")
file.write("<!--&#179 is the HTMl code for superscript 3-->")
file.write("<th>n&#179</th>")
writeData(n3Array)
file.write("</tr>")

file.write("<!--This is the eighth row of the table(2^n)-->")
file.write("<tr>")
file.write("<!--<sup> tag allows us to write text in superscript-->")
file.write("<th>2<sup>n</sup></th>")
writeData(b2nArray)
file.write("</tr>")

file.write("<!--This is the ninth row of the table(n!)-->")
file.write("<tr>")
file.write("<th>n!</th>")
writeData(nFacArray)
file.write("</tr>")

file.close()


# # Part 2a: Insertion Sort

# In[4]:


#time efficiency function 
import time

#function for timeEfficiency reused from Homework 1b
#*args part takes in any type of arguments and any number of arguments that are needed for the function to be called
def timeEfficiency(function, *args):
    #gets start time of the function called
    startTime = time.process_time()
    
    value = function(*args)
    print(value)

    #gets the end time after the function is done
    endTime = time.process_time()
    
    print("Start Time:", startTime)
    print("End Time:", endTime)
    print("Time taken to execute function:", endTime - startTime)

#function to read file input from user
def readFile(file):
    numArray = []
    for line in file:
        for num in line.split():
            #since the split function splits string, use the int() function to convert all numbers in file of type string to values of integer type
            numArray.append(int(num))
    return numArray

#insertion sort referenced from class slides (Lecture 4-1, slide 17/18)
def InsertionSort(array):
    #counter to keep track of the number of comparisons
    counter = 0
    for i in range(1, len(array)):
        #saves current number to be moved into a variable
        current = array[i]
        #starts checking the number to the left of the current number
        j = i-1
        
        #loop finds the correct position for the current number to be placed in the sorted part of the array
        while j >= 0 and array[j] > current:
            #shifts numbers greater than current one position to the right
            array[j+1] = array[j]
            #decrement to move to the next neighbor to the left
            j -= 1
            counter += 1
        #puts the next number in the sorted position after comparing the current sorted numbers to the current number to be sorted
        array[j+1] = current
    print("Number of comparisons:", counter)
    return array

#reads file input
file = input("Type in a file name.\n")
file = open(file, "r")
timeEfficiency(InsertionSort, readFile(file))


# # Part 2b: Merge Sort

# In[ ]:


#time efficiency function 
import time

#counter used to keep track of the number of comparisons done
global counter
counter1 = 0

#function for timeEfficiency reused from Homework 1b
#*args part takes in any type of arguments and any number of arguments that are needed for the function to be called
def timeEfficiency(function, *args):
    #gets start time of the function called
    startTime = time.process_time()
    
    value = function(*args)
    print(value)

    #gets the end time after the function is done
    endTime = time.process_time()
    
    print("Start Time:", startTime)
    print("End Time:", endTime)
    print("Time taken to execute function:", endTime - startTime)

#function to read user's input for a file
def readFile(file):
    numArray = []
    for line in file:
        for num in line.split():
            #since the split function splits string, use the int() function to convert all numbers in file of type string to values of integer type
            numArray.append(int(num))
    return numArray

#sort function is used to divide the array into smaller parts (called recursively)
#code referenced from GeeksForGeeks website (https://www.geeksforgeeks.org/merge-sort/)
def MergeSort(array):
    #keeps the recursion going (splitting the array) until the size is 1
    #if it reaches 1, return the unmodified array/do not recurse through splitting again
    if len(array) == 1:
        return array
    if len(array) > 1:
        #used to divide the arrays and subarrays equally (start+end/2 does not always split the array in half equally)
        mid = int(len(array) / 2)
        #sets the left part of the array to the left side of the middle of passed array (creates a subarray of bigger array)
        Left = array[0:mid]
        #sets the right part of the array to the right side of the middle of passed array (subarray of bigger array)
        Right = array[mid:len(array)]
        #starts splitting the left side of the array, returns the sorted array/subarray
        Left = MergeSort(Left)
        Right = MergeSort(Right)
        #after everything is sorted, the left array becomes the combined version of the two smaller subarrays
        #new array is created to merge the values in Left and Right in sorted order
        newArr = []
        #compares the two subarrays and puts the values in sorted order into a new larger array
        while (len(Left)) != 0 and len(Right) != 0:
            #checks if the smallest value in the right subarray is less than or equal to the smallest value in the left subarray
            if Right[0] <= Left[0]:
                newArr.append(Right[0])
                #removes the smallest value in the right subarray and moves on to the next smallest value in this subarray
                Right.remove(Right[0])
                counter1 += 1
            #checks if the smallest value in the left subarray is less than the smallest value in the right subarray
            elif Left[0] < Right[0]:
                newArr.append(Left[0])
                #removes the smallest value in the left subarray and moves onto the next smallest value in this subarray
                Left.remove(Left[0])
                counter1 += 1
            #if the right subarray is empty, input the rest of the values in the left subarray into the new array
            if len(Right) == 0:
                for k in range(len(Left)):
                    newArr.append(Left[k])
            #if the left subarray is empty, input the rest of the values in the right subarray into the new array
            elif len(Left) == 0:
                for l in range(len(Right)):
                    newArr.append(Right[l])
        return newArr 

#reads file input
file = input("Type in a file name.\n")
file = open(file, "r")
timeEfficiency(MergeSort, readFile(file))
print("Number of comparisons:", counter1)


# In[ ]:




