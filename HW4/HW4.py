#!/usr/bin/env python
# coding: utf-8

# # Name: Ivy Truong
# # Class: CSCI 3412
# # Date Created: 3/19/20
# # Homework 4

# # Sorting Algorithm using Merge sort, Radix sort, and Bucket sort

# In[1]:


#most of the code was used from Homework 2 for merge sort

#import libraries
import math
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

#below is code to sort list using radix sort and counting sort as the underlying sort
#code referenced and used from Geeks for Geeks website: https://www.geeksforgeeks.org/radix-sort/
def countSort(array, position):
    #stores count of digits from 0-9 by creating 10 spaces in the countArr
    countArr = [0] * 10
    #stores the sorted array based on the digits compared
    output = [0] * len(array)
    #stores the index calculations/digits in the current position for each number in original array
    indexArr = [0] * len(array)
    
    #storing the number of occurrences of the digit in countArr
    for i in range(0, len(array)):
        #calculation below gets the digit at the current placeholder/position
        #took %10 because each placeholder in the number is a power of 10 (1s place, 10s place, 100s place, etc.)
        #example: if the number is 31 and we are trying to compare the 1s position digits, 
            #it would be 31/1 = 31, take 31%10 = 1, where the remainder is the digit at the 1s place of the original number
        index = int(array[i]/position)%10
        countArr[index] += 1
        indexArr[i] = index
        
    #add the previous count to the current count, calculates the positions the numbers will be put in the output array    
    for j in range(1, 10):
        #starts at j = 1 because there is no element to the left of countArr[0] to add to countArr[0]
        countArr[j] += countArr[j-1]
        
    #putting values in sorted order based on the indicies calculated from countArr
        #need to start at the end of the original array to preserve the order of the elements (so it prints in ascending order and sorting is stable)
    for k in range(0, len(array)):
        #gets the index for where the number should be placed in the output array
            #has to be the count-1 because counting starts at 0, not 1
        newIndex = countArr[indexArr[len(array)-k-1]] - 1
        #puts the number in its designated position
        output[newIndex] = array[len(array)-k-1]
        #decrements the count so nothing replaces values in the output array
        countArr[indexArr[len(array)-k-1]] -= 1
    return output
    
def radixSort(array):
    #find the max value in the array to know how many times to calculate sort
        #example: if the biggest number is 22, then the sort needs to calculate 2 times, 
            #one for the 1s place digits and one for the 10s place digits
    maxVal = max(array)
    #start at position 1 to calculate the 1s place digits first
    position = 1
    #keeps the loop going until there are no more digits to sort
    while maxVal/position > 0:
        array = countSort(array, position)
        #multiply the position by 10 because each placeholder increments by 10 digits for the range
            #example: 1s place has numbers 0-9, 10s place has 2 numbers from 0-9 so the range is 0-19, etc.
        position *= 10
    return array

#same function coded from Homework 2
#insertion sort referenced from class slides (Lecture 4-1, slide 17/18)
def insertionSort(array):
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
        #puts the next number in the sorted position after comparing the current sorted numbers to the current number to be sorted
        array[j+1] = current
    return array

def bucketSort(array):
    #find max value in array so it is easier to break up set of numbers into even buckets
    maxVal = max(array)
    #find number of buckets
    numBuckets = int(math.ceil(math.sqrt(maxVal)))
    #nested list to store values of different ranges
    bucketArr = []
    #array to store sorted array
    newArr = []
    
    #adds a list for every bucket to hold a range of values that fit in each bucket
        #example: bucket 1 has a list of values from 0-9, 2nd bucket from 11-19, etc.
    for i in range(0, numBuckets):
        bucketArr.append([])
    
    #how big the range should be for each bucket
    
    #values of the starting range and ending range for a bucket, will increment throughout loop
    a = 0 #start value in range
    b = int(maxVal/numBuckets) #end value in range
    c = 0 #current index in nested array for bucket sort
    
    #puts values into their designated buckets
    for j in array:
        while True:
            #if the value is in the range of the current bucket, place the value in the bucket
            if j >= a and j <= b:
                bucketArr[c].append(j)
                #resets values when comparing the next value to the range
                a = 0
                b = numBuckets
                c = 0
                #leave while loop after value is found
                break;
            else:
                #increments the start range and end range to get to the next bucket
                a = b + 1
                b = a + numBuckets
                #go to the next bucket range
                c += 1
    
    #sort buckets using merge sort
    for k in range(0, numBuckets):
        #combine all sorted buckets together into one array
        if len(bucketArr[k]) != 0:
            bucketArr[k] = insertionSort(bucketArr[k])
            for m in range(0, len(bucketArr[k])):
                newArr.append(bucketArr[k][m])
    return newArr

#function to read file input from user
def readFile(file):
    numArray = []
    for line in file:
        for num in line.split():
            #since the split function splits string, use the int() function to convert all numbers in file of type string to values of integer type
            numArray.append(int(num))
    return numArray

#def sortIt(array):
    #if len(array)%2 != 0:
        #array = radixSort(array)
    #elif len(array)%2 == 0:
        #array = bucketSort(array)
    #return array

def mergeIt(array, kLen, val):

    if len(array) <= kLen:
        #array = sortIt(array)
        #left half of arrays will sort with radix sort, while right half of arrays will sort with bucket sort
        if val == 0:
            array = radixSort(array)
        elif val == 1:
            array = bucketSort(array)
        return array
    
    if len(array) > kLen:
        #used to divide the arrays and subarrays equally (start+end/2 does not always split the array in half equally)
        mid = int(len(array) / 2)
        #sets the left part of the array to the left side of the middle of passed array (creates a subarray of bigger array)
        Left = array[0:mid]
        #sets the right part of the array to the right side of the middle of passed array (subarray of bigger array)
        Right = array[mid:len(array)]
        #starts splitting the left side of the array, returns the sorted array/subarray
        Left = mergeIt(Left, kLen, 0)
        Right = mergeIt(Right, kLen, 1)
    
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
            #counter += 1
        #checks if the smallest value in the left subarray is less than the smallest value in the right subarray
        elif Left[0] < Right[0]:
            newArr.append(Left[0])
            #removes the smallest value in the left subarray and moves onto the next smallest value in this subarray
            Left.remove(Left[0])
            #counter += 1
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
kLen = int(len(array)/100)
timeEfficiency(mergeIt, array, kLen, 0)
#print(array)


# In[ ]:


#most of the code was used from Homework 2 for merge sort

#import libraries
import math
import time

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

#below is code to sort list using radix sort and counting sort as the underlying sort
#code referenced and used from Geeks for Geeks website: https://www.geeksforgeeks.org/radix-sort/
def countSort(array, position):
    #stores count of digits from 0-9 by creating 10 spaces in the countArr
    countArr = [0] * 10
    #stores the sorted array based on the digits compared
    output = [0] * len(array)
    #stores the index calculations/digits in the current position for each number in original array
    indexArr = [0] * len(array)
    
    #storing the number of occurrences of the digit in countArr
    for i in range(0, len(array)):
        #calculation below gets the digit at the current placeholder/position
        #took %10 because each placeholder in the number is a power of 10 (1s place, 10s place, 100s place, etc.)
        #example: if the number is 31 and we are trying to compare the 1s position digits, 
            #it would be 31/1 = 31, take 31%10 = 1, where the remainder is the digit at the 1s place of the original number
        index = int(array[i]/position)%10
        countArr[index] += 1
        indexArr[i] = index
        
    #add the previous count to the current count, calculates the positions the numbers will be put in the output array    
    for j in range(1, 10):
        #starts at j = 1 because there is no element to the left of countArr[0] to add to countArr[0]
        countArr[j] += countArr[j-1]
        
    #putting values in sorted order based on the indicies calculated from countArr
        #need to start at the end of the original array to preserve the order of the elements (so it prints in ascending order and sorting is stable)
    for k in range(0, len(array)):
        #gets the index for where the number should be placed in the output array
            #has to be the count-1 because counting starts at 0, not 1
        newIndex = countArr[indexArr[len(array)-k-1]] - 1
        #puts the number in its designated position
        output[newIndex] = array[len(array)-k-1]
        #decrements the count so nothing replaces values in the output array
        countArr[indexArr[len(array)-k-1]] -= 1
    return output
    
def radixSort(array):
    #find the max value in the array to know how many times to calculate sort
        #example: if the biggest number is 22, then the sort needs to calculate 2 times, 
            #one for the 1s place digits and one for the 10s place digits
    maxVal = max(array)
    #start at position 1 to calculate the 1s place digits first
    position = 1
    #keeps the loop going until there are no more digits to sort
    while maxVal/position > 0:
        array = countSort(array, position)
        #multiply the position by 10 because each placeholder increments by 10 digits for the range
            #example: 1s place has numbers 0-9, 10s place has 2 numbers from 0-9 so the range is 0-19, etc.
        position *= 10
    return array

#same function coded from Homework 2
#insertion sort referenced from class slides (Lecture 4-1, slide 17/18)
def insertionSort(array):
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
        #puts the next number in the sorted position after comparing the current sorted numbers to the current number to be sorted
        array[j+1] = current
    return array

def bucketSort(array):
    #find max value in array so it is easier to break up set of numbers into even buckets
    maxVal = max(array)
    #find number of buckets
    numBuckets = int(math.ceil(math.sqrt(maxVal)))
    #nest list to store values of different ranges
    bucketArr = []
    #array to store sorted array
    newArr = []
    
    #adds a list for every bucket to hold a range of values that fit in each bucket
        #example: bucket 1 has a list of values from 0-9, 2nd bucket from 11-19, etc.
    for i in range(0, numBuckets):
        bucketArr.append([])
    
    #how big the range should be for each bucket
    
    #values of the starting range and ending range for a bucket, will increment throughout loop
    a = 0 #start value in range
    b = int(maxVal/numBuckets) #end value in range
    c = 0 #current index in nested array for bucket sort
    
    #puts values into their designated buckets
    for j in array:
        while True:
            #if the value is in the range of the current bucket, place the value in the bucket
            if j >= a and j <= b:
                bucketArr[c].append(j)
                #resets values when comparing the next value to the range
                a = 0
                b = numBuckets
                c = 0
                #leave while loop after value is found
                break;
            else:
                #increments the start range and end range to get to the next bucket
                a = b + 1
                b = a + numBuckets
                #go to the next bucket range
                c += 1
    
    #sort buckets using insertion sort
    for k in range(0, numBuckets):
        #combine all sorted buckets together into one array
        if len(bucketArr[k]) != 0:
            bucketArr[k] = insertionSort(bucketArr[k])
            for m in range(0, len(bucketArr[k])):
                newArr.append(bucketArr[k][m])
    return newArr

#function to read file input from user
def readFile(file):
    numArray = []
    for line in file:
        for num in line.split():
            #since the split function splits string, use the int() function to convert all numbers in file of type string to values of integer type
            numArray.append(int(num))
    return numArray

def sortIt(array, kLen):
    if len(array) <= kLen:
        return array
    
    if len(array) > kLen:
        #used to divide the arrays and subarrays equally (start+end/2 does not always split the array in half equally)
        mid = int(len(array) / 2)
        #sets the left part of the array to the left side of the middle of passed array (creates a subarray of bigger array)
        Left = array[0:mid]
        #sets the right part of the array to the right side of the middle of passed array (subarray of bigger array)
        Right = array[mid:len(array)]
        #starts splitting the left side of the array, returns the sorted array/subarray
        Left = sortIt(Left, kLen)
        Right = sortIt(Right, kLen)
        #below does radix sort
        Left = radixSort(Left)
        
        #below does bucket sort
        Right = bucketSort(Right)
    
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
            #counter += 1
        #checks if the smallest value in the left subarray is less than the smallest value in the right subarray
        elif Left[0] < Right[0]:
            newArr.append(Left[0])
            #removes the smallest value in the left subarray and moves onto the next smallest value in this subarray
            Left.remove(Left[0])
            #counter += 1
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
kLen = int(len(array)/100)
timeEfficiency(sortIt, array, kLen)
#print(array)

