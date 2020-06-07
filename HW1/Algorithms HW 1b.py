#!/usr/bin/env python
# coding: utf-8

# # Part 1: Number Guessing Game

# In[1]:


#Name: Ivy Truong
#Class: CSCI 3412
#Date Created: 2/3/2020
#Homework 1: Simulating Algorithms

#import random allows us to use functions to randomize inputs
import random

inputError = True

#user input
while inputError == True:
    myGuess = int(input("Input a number between 1 and 1000.\n"))

    #error checking for input
    if myGuess >= 1 and myGuess <= 1000:
        inputError = False
    else:
        print("Invalid number input.")

#computer input

#below are starting values 
i = 0
j = 1001
numCheck = " "
numGuess = 0

#binary search method for computer guess
while numCheck != "c":
    computerGuess = int((j + i)/2)
    print("Computer Guess:", computerGuess)
    numGuess = numGuess + 1
    numCheck = input("Type 'l' if number is larger than guess, 's' if number is smaller than guess, and 'c' if the number guessed is correct.\n")

    if numCheck == "l":
        i = computerGuess
    elif numCheck == "s":
        j = computerGuess
    elif numCheck == "c":
        print("Your number", myGuess, "was guessed!")
        print("It took", numGuess, "tries to guess the number!")
    else:
        print("Invalid input.")


# # Part 2: Time Efficiency Function

# In[2]:


import time

def sumUp():
    result = 0
    maxNum = int(input("Enter a large number greater than 0.\n"))
    #below will add up all the numbers between 0 and maxNum
    for number in range(maxNum + 1):
        result = result + number
    print("Sum:", result)

def timeEfficiency(function):
    #gets start time of the function called
    startTime = time.process_time()
    
    function()

    #gets the end time after the function is done
    endTime = time.process_time()
    
    print("Start Time:", startTime)
    print("End Time:", endTime)
    print("Time taken to execute function:", endTime - startTime)

#passes a function, if it was function(), it would not pass a function by the value returned by the function    
timeEfficiency(sumUp)
    


# # Part 3: Guessing Game testing 2 algorithms 

# In[3]:


import random

#function for number generator 
def numGen():
    result = random.randrange(0, 10)
    return result

#function for brute force algorithm
def bruteForce():
    #generate a 'random' 3 digit number to guess
    #below breaks up the numbers into the 100's, 10's and 1's place
    #will produce a number between 0-999
    myGuess = (100 * numGen()) + (10 * numGen()) + numGen() 
    computerGuess = 0
    numGuess = 1
    #the computer will continue guessing until they made the right guess
    while computerGuess != myGuess:
        if computerGuess != myGuess:
            computerGuess += 1
            numGuess += 1
    return numGuess

#function for pure random algorithm
def randGuessx3():
    #generate a 'random' 3 digit number to guess
    #below breaks up the numbers into the 100's, 10's and 1's place
    #will produce a number between 0-999
    myGuess = (100 * numGen()) + (10 * numGen()) + numGen() 
    correct = False
    numGuess = 1
    #the computer will continue guessing until they made the right guess
    while correct == False:
        computerGuess = (100 * numGen()) + (10 * numGen()) + numGen()
        if computerGuess != myGuess:
            numGuess += 1
        else:
            correct = True
    return numGuess

#function that will find statistics of a function
def algorithmStats(function, numTries):
    highestGuessCount = 0
    lowestGuessCount = numTries
    avgGuess = 0
    for tries in range(numTries):
        currGuessCount = function()
        if currGuessCount > highestGuessCount:
            highestGuessCount = currGuessCount
        if currGuessCount < lowestGuessCount:
            lowestGuessCount = currGuessCount
        avgGuess += currGuessCount
    avgGuess /= numTries
    print("Number of total tries:", numTries)
    #since the number of guesses is infinite, the computer will eventually reach the correct guess
    print("Number of correct tries:", numTries)
    print("Highest number of guesses in a try:", highestGuessCount)
    print("Lowest number of guesses in a try:", lowestGuessCount)
    print("Average number of guesses made:", avgGuess)
    
#calls to function
print("Deterministic Brute Force Algorithm:")
algorithmStats(bruteForce, 10000)
print("Complete Pure Random Algorithm:")
algorithmStats(randGuessx3, 10000)


# # Part 4: Reading Text File and Calculating Word Frequencies

# In[2]:


#reading input files and calculating the frequency of words

file = input("Type in a file name.\n")

file = open(file, "r")

wordList = dict()

for line in file:
    #line split function splits any string in between whitespace
    for word in line.split():
        #converts all words into lowercase to make comparisons case insensitive
        word = word.lower()
        for letter in word:
            #checks if there are any punctuation with the word (symbols are not words)
            #ord() is a instruction that checks the ascii value of each letter
            if ord(letter) < ord("a") or ord(letter) > ord("z"):
                #if the symbol is at the beginning of the word
                if word.index(letter) == 0:
                    word = word[1:len(word)]
                #if the symbol is at the end of the word    
                elif word.index(letter) == len(word) - 1:
                    word = word[0:len(word) - 1]  
        #adds words and frequency into a dictionary
        if word not in wordList:
            wordList[word] = 1  
            #exception case if there is no word/string is empty
            if word == "":
                wordList.pop(word)
        elif word in wordList:
            wordList[word] += 1

#sorted function sorts dictionary by value 
#first parameter is an iterable object
#lambda expression takes in a key(which is the key and value item in the dictionary) and converts it to the value associated with the key
    #for this problem, the key will be the frequencies associated with each word, so the dictionary will be sorted by value
#reverse true prints the items in descending order  
#below converts key value pair in dictionary into nested list 
nestedList = sorted(wordList.items(), key = lambda v:v[1], reverse = True)

#prints the values separately with the word first and word frequency second in descending order of the frequencies
numWords = input("Type in how many words you want to print out.\n")
print("Words that occur in text and their frequencies in descending order.")
for count in range(0, numWords):
    for group in nestedList:
        print(group[0], ":", group[1])

#close file to prevent corruption
file.close()


# In[ ]:




