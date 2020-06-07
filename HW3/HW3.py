#!/usr/bin/env python
# coding: utf-8

# # Name: Ivy Truong
# # Class: CSCI 3412
# # Date Created: 3/5/2020
# # Homework 3

# # 3c) Merge Sort

# In[1]:


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

#function reused from Homework 2
def MergeSort(array):
    #keeps the recursion going (splitting the array) until the size is 1
    #if it reaches 1, return the unmodified array/do not recurse through splitting again
    #counter used to keep track of the number of comparisons done
    global counter
    counter = 0
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
                counter += 1
            #checks if the smallest value in the left subarray is less than the smallest value in the right subarray
            elif Left[0] < Right[0]:
                newArr.append(Left[0])
                #removes the smallest value in the left subarray and moves onto the next smallest value in this subarray
                Left.remove(Left[0])
                counter += 1
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
print("Number of comparisons:", counter)


# # 3c) Selection Sort

# In[3]:


#time efficiency function 
import time

#function for timeEfficiency reused from Homework 1b
#*args part takes in any type of arguments and any number of arguments that are needed for the function to be called
def timeEfficiency(function, *args):
    #gets start time of the function called
    startTime = time.process_time()
    
    value = function(*args)

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

#code derived from Homework 3, question 2
def SelectionSort(array):
    counter = 0
    for i in range(len(array)):
        #sets as the minimum index so the values can be compared to find the minimum value in the array
        min_index = i 
        for j in range(i+1, len(array)):
            #compares the minimum value to an element in the array to see if it is smaller than the minimum value
            if array[min_index] > array[j]:
                min_index = j
            counter += 1
        #swaps the minimum element with the element in array[i]
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
    print(array)
    print("Number of comparisons:", counter)

#reads file input
file = input("Type in a file name.\n")
file = open(file, "r")
timeEfficiency(SelectionSort, readFile(file))
            


# # 3d) Combining Merge and Selection Sort as one algorithm

# In[4]:


#for time efficiency function 
import time
#for calculating k
import math

#function for timeEfficiency reused from Homework 1b
#*args part takes in any type of arguments and any number of arguments that are needed for the function to be called
def timeEfficiency(function, *args):
    #gets start time of the function called
    startTime = time.process_time()
    
    value = function(*args)
    #print(value)

    #gets the end time after the function is done
    endTime = time.process_time()
    
    print("Start Time:", startTime)
    print("End Time:", endTime)
    print("Time taken to execute function:", endTime - startTime)



def findK(arrayLen):
    k = int(math.log2(arrayLen))
    return k

#combination of selection sort and merge sort
def MergeSelect(array, k):
    #counter used to keep track of the number of comparisons done
    global counter
    counter = 0
    
    #if the array length is less than or equal to the ideal k, use selection sort
    if len(array) <= k:
        #selection sort
        for i in range(len(array)):
        #sets as the minimum index so the values can be compared to find the minimum value in the array
            min_index = i 
            for j in range(i+1, len(array)):
                #compares the minimum value to an element in the array to see if it is smaller than the minimum value
                if array[min_index] > array[j]:
                    min_index = j
                counter += 1
            #swaps the minimum element with the element in array[i]
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp
        return array
    
    if len(array) > k:
        #used to divide the arrays and subarrays equally (start+end/2 does not always split the array in half equally)
        mid = int(len(array) / 2)
        #sets the left part of the array to the left side of the middle of passed array (creates a subarray of bigger array)
        Left = array[0:mid]
        #sets the right part of the array to the right side of the middle of passed array (subarray of bigger array)
        Right = array[mid:len(array)]
        #starts splitting the left side of the array, returns the sorted array/subarray
        Left = MergeSelect(Left, k)
        Right = MergeSelect(Right, k)
        
        
    #if the array length is greater than the ideal k
    #using merge function in merge sort
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
            counter += 1
        #checks if the smallest value in the left subarray is less than the smallest value in the right subarray
        elif Left[0] < Right[0]:
            newArr.append(Left[0])
            #removes the smallest value in the left subarray and moves onto the next smallest value in this subarray
            Left.remove(Left[0])
            counter += 1
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
array = readFile(file)
#equation to find k (sublist length)
k = findK(len(array))
#k = k
print(k)
timeEfficiency(MergeSelect, array, k)
print("Number of comparisons:", counter)


# In[ ]:




