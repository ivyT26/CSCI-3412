#!/usr/bin/env python
# coding: utf-8

# # Name: Ivy Truong
# # Date: 4/16/20
# # CSCI 3412
# # Homework 5

# # 2a) LCS with recursion

# In[ ]:


#libraries imported
import time

#function to read file input from user
def readFile(file):
    Array = []
    for line in file:
        for val in line.split():
            #use the split function to split string
            Array.append(val)
    return Array

#function for timeEfficiency reused from Homework 1b
#*args part takes in any type of arguments and any number of arguments that are needed for the function to be called
def timeEfficiency(function, *args):
    #gets start time of the function called
    startTime = time.process_time()
    
    #writing results to a file
    outfile.write("LCS length for each string of numbers compared with '0123456789': \n")
    outfile.write(str(function(*args)))

    #gets the end time after the function is done
    endTime = time.process_time()
    
    #writing time efficiency to file and screen
    outfile.write("\n")
    outfile.write("Time efficiency for LCS recursion: \n")
    print("Start Time:", startTime)
    outfile.write("Start Time: ")
    outfile.write(str(startTime))
    outfile.write("\n")
    print("End Time:", endTime)
    outfile.write("End Time: ")
    outfile.write(str(endTime))
    outfile.write("\n")
    print("Time taken to execute function:", endTime - startTime)
    outfile.write("Time taken to execute function: ")
    outfile.write(str(endTime - startTime))
    outfile.write("\n")

#code referenced and used from Lecture 13: Dynamic Programming from course CSCI 3412
#in LCS, the goal is to find the longest subsequence when comparing two strings without altering the order of the values in the string
#the longest subsequence does not have to be continuous, but it cannot backtrack when comparing (hence keeping the values in order)
#for example, if A = fart and B = afrt, then the longest subsequence is either frt or art
def LCSrec(A, B, i, j):
    #base case: if one of the strings reaches the end, then end the comparisons because there is no more values to compare with each other
    if(i == len(A) or j == len(B)):
        return 0
    #if the value stores at the indexes of each string match, then increment the value by 1 to indicate a match
    #increment the indexes of both strings to compare the next set of values in the strings
    elif(A[i] == B[j]):
        return 1 + LCSrec(A, B, i+1, j+1)
    #if the values at those indexes of each string do not match, then find the max number of matches for the rest of the strings
    #will increment the index for array A or increment the index for array B and compare which set of comparison has the most matches
    #for example, if the two strings were CAT and BAT, it would see that the first two letters are different and would find the max matches starting from comparing
        #C in cat to A in bat or A in cat to B in bat
    elif(A[i] != B[j]):
        return max(LCSrec(A, B, i+1, j), LCSrec(A, B, i, j+1))

def compStr(A, B):
    #store the length of the longest subsequence for each string of numbers
    numMatches = []
    for i in range(0, len(A)):
        numMatches.append(LCSrec(A[i], B, 0, 0))
    return numMatches
    
userInput = input("Type in a file you want to read.\n")
file = open(userInput, "r")
#will have an array of strings, need to separate to compare each  string separately with B
A = readFile(file)
#A = [1, 2, 3, 4]
B = "0123456789"
outfile = open("outRec.txt", "w")
outfile.write("File of strings worked with: ")
outfile.write(userInput)
outfile.write("\n")
timeEfficiency(compStr, A, B)
outfile.close()
file.close()


# # 2b) LCS with memoisation

# In[1]:


#libraries imported
import time

#function to read file input from user
def readFile(file):
    Array = []
    for line in file:
        for val in line.split():
            #use the split function to split string
            Array.append(val)
    return Array

#function for timeEfficiency reused from Homework 1b
#*args part takes in any type of arguments and any number of arguments that are needed for the function to be called
def timeEfficiency(function, *args):
    #gets start time of the function called
    startTime = time.process_time()
    
    #writing results to a file
    outfile.write("LCS length for each string of numbers compared with '0123456789': \n")
    outfile.write(str(function(*args)))

    #gets the end time after the function is done
    endTime = time.process_time()
    
    #writing time efficiency to file and screen
    outfile.write("\n")
    outfile.write("Time efficiency for LCS memoisation: \n")
    print("Start Time:", startTime)
    outfile.write("Start Time: ")
    outfile.write(str(startTime))
    outfile.write("\n")
    print("End Time:", endTime)
    outfile.write("End Time: ")
    outfile.write(str(endTime))
    outfile.write("\n")
    print("Time taken to execute function:", endTime - startTime)
    outfile.write("Time taken to execute function: ")
    outfile.write(str(endTime - startTime))
    outfile.write("\n")

#code referenced from Lecture 13: Dynamic Programming from course CSCI 3412
#this code below is simulating an LCS using dynamic programming/memoisation
#to simulate memoisation, we need a table that records the maximum number of matches at each indices of the strings
#video used to learn about LCS recursion and memoisation: https://www.youtube.com/watch?v=sSno9rV8Rhg
def LCSmemo(A, B):
    table = []
    
    #create a frame for the table that will store the values
    for i in range(0, len(A) + 1):
        #appending [] to store as the column, list of numbers will be the rows
        table.append([])

    for i in range(0, len(A) + 1):
        for j in range(0, len(B) + 1):
            if (i == 0 or j == 0):
                table[i].append(0)
            elif(A[i - 1] == B[j - 1]): #have to offset the arrays by 1, since the table is filling in the value matches plus the 0s sections
                table[i].append(1 + table[i-1][j-1])
            elif(A[i- 1] != B[j - 1]): #have to offset arrays by 1, since table doesn't start comparing values until the next row and column of table
                table[i].append(max(table[i-1][j], table[i][j-1]))
    return table[len(A)][len(B)]
    
def compStr(A, B):
    #store the length of the longest subsequence for each string of numbers
    numMatches = []
    for i in range(0, len(A)):
        numMatches.append(LCSmemo(A[i], B))
    return numMatches

userInput = input("Type in a file you want to read.\n")
file = open(userInput, "r")
#will have an array of strings, need to separate to compare each  string separately with B
A = readFile(file)
#A = ["1234", "5629", "0032", "9876"]
#A = ["1234", "5629"]
B = "0123456789"
outfile = open("outMem.txt", "w")
outfile.write("File of strings worked with: ")
outfile.write(userInput)
outfile.write("\n")
timeEfficiency(compStr, A, B)
outfile.close()
file.close()


# # 3a) Modifying LCS Recursion to count total recusive calls for each pair of strings compared

# In[8]:


#libraries imported
import time

#function to read file input from user
def readFile(file):
    Array = []
    for line in file:
        for val in line.split():
            #use the split function to split string
            #modification: only going to do recursion on 6 digit numbers in the file, only append to array 6 digit numbers
            if(len(val) >= 6):
                Array.append(val)
    return Array

#function for timeEfficiency reused from Homework 1b
#*args part takes in any type of arguments and any number of arguments that are needed for the function to be called
def timeEfficiency(function, *args):
    #gets start time of the function called
    startTime = time.process_time()
    
    #writing results to a file
    outfile.write("LCS length for each string of numbers compared with '0123456789' and the number of recursive calls: \n")
    value = function(*args)

    #gets the end time after the function is done
    endTime = time.process_time()
    
    #writing time efficiency to file and screen
    outfile.write("\n")
    outfile.write("Time efficiency for LCS recursion: \n")
    print("Start Time:", startTime)
    outfile.write("Start Time: ")
    outfile.write(str(startTime))
    outfile.write("\n")
    print("End Time:", endTime)
    outfile.write("End Time: ")
    outfile.write(str(endTime))
    outfile.write("\n")
    print("Time taken to execute function:", endTime - startTime)
    outfile.write("Time taken to execute function: ")
    outfile.write(str(endTime - startTime))
    outfile.write("\n")

#code referenced and used from Lecture 13: Dynamic Programming from course CSCI 3412
#in LCS, the goal is to find the longest subsequence when comparing two strings without altering the order of the values in the string
#the longest subsequence does not have to be continuous, but it cannot backtrack when comparing (hence keeping the values in order)
#for example, if A = fart and B = afrt, then the longest subsequence is either frt or art
def LCSrec(A, B, i, j):
    global numCalls
    #base case: if one of the strings reaches the end, then end the comparisons because there is no more values to compare with each other
    if(i == len(A) or j == len(B)):
        return 0
    #if the value stores at the indexes of each string match, then increment the value by 1 to indicate a match
    #increment the indexes of both strings to compare the next set of values in the strings
    elif(A[i] == B[j]):
        numCalls += 1
        return 1 + LCSrec(A, B, i+1, j+1)
    #if the values at those indexes of each string do not match, then find the max number of matches for the rest of the strings
    #will increment the index for array A or increment the index for array B and compare which set of comparison has the most matches
    #for example, if the two strings were CAT and BAT, it would see that the first two letters are different and would find the max matches starting from comparing
        #C in cat to A in bat or A in cat to B in bat
    elif(A[i] != B[j]):
        numCalls += 2
        return max(LCSrec(A, B, i+1, j), LCSrec(A, B, i, j+1))

def compStr(A, B):
    global numCalls
    #store the length of the longest subsequence for each string of numbers
    numMatches = []
    for i in range(0, len(A)):
        #reset the number of recursive calls so it can calculate the next set
        numCalls = 0
        #append nested list that will store the LCS num and the number of recursive calls
        numMatches.append([])
        numMatches[i].append(LCSrec(A[i], B, 0, 0))
        numMatches[i].append(numCalls)
        outfile.write(str(numMatches[i]))
        outfile.write(" , ")
    return numMatches
    
userInput = input("Type in a file you want to read.\n")
file = open(userInput, "r")
numCalls = 0
#will have an array of strings, need to separate to compare each  string separately with B
A = readFile(file)
#A = [1, 2, 3, 4]
B = "0123456789"
outfile = open("outModRec.txt", "w")
outfile.write("File of strings worked with: ")
outfile.write(userInput)
outfile.write("\n")
timeEfficiency(compStr, A, B)
outfile.close()
file.close()


# # 3b) Hash table to store LCS num, recursive calls tuple

# In[1]:


#linked list class created to implement separate chaining hash table
#link for linked list implementation: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
class Node(): #creating a node for each set of values with the same key
    def __init__(self, other): #each node will have the data/value, 'point' to the next value in list, and 'point' to the node in front of them in list
        self.data = other;
        self.next = None; #none means there is no specific object type that is bound to the variable
        self.previous = None;
        
class linkedList(): #creating a linked list for all values that share the same key
    #linked list is a doubly linked list
    def __init__(self): #head node that is the start of the list
        self.head = None;
    #function only works if a file to write the values is open
    def printIt(self): #will print all the nodes in the list by traversing through the linked list starting at head node
        val = self.head
        while val != None:
            outfile.write(str(val.data)) #print the value in the current node to the file
            outfile.write(", ")
            val = val.next #move to the next node
    def calLen(self):
        #the only thing I didn't include was to subtract 1 from the length, this includes the idea that if there is only
        #one value in the hash table, it means there is no collision. this function only calculates the number of values
        #in each hash key. to calculate collisions, one must subtract 1 from the total length. I also didn't want to rerun the program
        #for another few hours just because of 1 line.
        count = 0
        val = self.head
        while val != None:
            count += 1
            val = val.next
        return count

#function to read file input from user
def readFile(file):
    Array = []
    temp = []
    for line in file:
        #use the split function to split string by tuples
        for val in line.split('], '):
            chars = ""
            temp = []
            #reads each pair of integers and converts from string to list of tuples, where tuples include LCS num and num recusive calls
            for i in range(0, len(val)):
                if ord(val[i]) >= ord("0") and ord(val[i]) <= ord("9"):
                    chars += val[i]
                elif ord(val[i]) == ord(","):
                    temp.append(int(chars))
                    chars = ""
                elif val[i] == "\n":
                    continue;
                if i == len(val) - 1:
                    temp.append(int(chars))
                    Array.append(temp)
    
    return Array

def hashIt(A):
    #keys array to hold all the different keys and all the values that share the same key (will be an array of linked lists)
    keys = []
    #insert something in keys
    newList = linkedList()
    #appends the whole tuple as a node, where the tuple is stored in the data part of the node
    newList.head = Node(A[0])
    keys.append(newList)
    #first loop will traverse through the tuples in list A
    for i in range(1, len(A)):
        tracker = Node('[0, 0]');
        #second loop will organize tuples by keys and put them into a "hash table"
        for j in range(0, len(keys)):
            #if the key already exists in the hash table, append the value to the linked list
            if(keys[j].head.data[1] == A[i][1]):
                tracker = keys[j].head
                #traverse through the linked list until it has reached the end, then insert the new node
                while(tracker.next is not None):
                    tracker = tracker.next
                tracker.next = Node(A[i])
                tracker.next.previous = tracker
                break;
            #if the key is not in the hash table, insert it into the hash table
            elif(keys[j].head.data[1] != A[i][1] and j == len(keys)-1):
                newList = linkedList()
                #appends the whole tuple as a node, where the tuple is stored in the data part of the node
                newList.head = Node(A[i])
                keys.append(newList) 
    return keys

def printHash(A):
    outfile1.write("Size of bucket for each key (key:length)")
    outfile1.write("\n")
    for i in range(0, len(A)):
        #writes all the values stored at the hashed key
        A[i].printIt()
        outfile.write("\n")
        #calculates total values in each bucket corresponding to key
        outfile1.write(str(A[i].head.data[1]))
        outfile1.write(":")
        outfile1.write(str(A[i].calLen()))
        outfile1.write("\n")
        

userInput = input("Type in a file with the LCS num, recursive calls tuple.\n")
file = open(userInput, "r")
outfile = open("hash.txt", "w")
outfile1 = open("hashLen.txt", "w")
A = readFile(file)
B = hashIt(A)  
printHash(B)
outfile1.close()
outfile.close()
file.close()


# # 3c/d) Creating a frequency distribution graph for hash table of recursive calls

# In[ ]:


import matplotlib.pyplot as plt
#note: could not get plotly to work, so I only used matplotlib to make the graph    
    
#file we will be reading is a file after all the tuples of LCS num and recursive calls have been organized
    #into a hash table and we have calculated the frequencies of reach recursion call
#this function only works if the file was generated by the algorithm in 3b of Homework 5
def readFile(file):
    global key
    global frequency
    key = []
    frequency = []
    for val in file:
        #skip first line since it is just the header
        if(val == "Size of bucket for each key (key:length)\n" or val == "\n"):
            continue; #move on to next iteration
        temp = ""
        for digit in val:
            if digit == '\n':
                frequency.append(int(temp))
                break;
            elif digit == ":":
                key.append(int(temp))
                temp = ""
                tracker = 1
            #will collect all the digits of the recursion value or frequency of the recursion values
            else:
                temp += digit
                
def plotBar(key, frequency):
    plt.bar(key, frequency, width=0.8, color="red")
    plt.xlabel("# of recursive calls")
    plt.ylabel("frequency")
    plt.title("Collision frequency")
    #plt.show()
    plt.savefig("hashPlt.png")

key = []
frequency = []
userInput = input("Type in a file with the recursion values and their frequencies.\n")
file = open(userInput, "r")
readFile(file)
plotBar(key, frequency)

#converting image to html format
outfile = open("hashPlot.html", "w")
outfile.write("<!DOCTYPE HTML5>\n")
outfile.write("<html>")
outfile.write("<img src=\"hashPlt.png\">")
outfile.close()
file.close()


# # 3e) i. Creating secondary hash function to deal with recursion values greater than 10k

# In[ ]:


#linked list class created to implement separate chaining hash table
#link for linked list implementation: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
class Node(): #creating a node for each set of values with the same key
    def __init__(self, other): #each node will have the data/value, 'point' to the next value in list, and 'point' to the node in front of them in list
        self.data = other;
        self.next = None; #none means there is no specific object type that is bound to the variable
        self.previous = None;
        
class linkedList(): #creating a linked list for all values that share the same key
    #linked list is a doubly linked list
    def __init__(self): #head node that is the start of the list
        self.head = None;
    #function only works if a file to write the values is open
    def printIt(self): #will print all the nodes in the list by traversing through the linked list starting at head node
        val = self.head
        while val != None:
            outfile.write(str(val.data)) #print the value in the current node to the file
            outfile.write(", ")
            val = val.next #move to the next node
    def calLen(self):
        count = 0
        val = self.head
        while val != None:
            count += 1
            val = val.next
        return count

#function to read file input from user
def readFile(file):
    Array = []
    temp = []
    for line in file:
        #use the split function to split string by tuples
        for val in line.split('], '):
            chars = ""
            temp = []
            #reads each pair of integers and converts from string to list of tuples, where tuples include LCS num and num recusive calls
            for i in range(0, len(val)):
                if ord(val[i]) >= ord("0") and ord(val[i]) <= ord("9"):
                    chars += val[i]
                elif ord(val[i]) == ord(","):
                    temp.append(int(chars))
                    chars = ""
                elif val[i] == "\n":
                    continue;
                if i == len(val) - 1:
                    temp.append(int(chars))
                    Array.append(temp)
    
    return Array

def hashIt(A):
    #keys array to hold all the different keys and all the values that share the same key (will be an array of linked lists)
    keys = []
    #insert something in keys
    newList = linkedList()
    #appends the whole tuple as a node, where the tuple is stored in the data part of the node
    newList.head = Node(A[0])
    keys.append(newList)
    #first loop will traverse through the tuples in list A
    for i in range(1, len(A)):
        tracker = Node('[0, 0]');
        #second loop will organize tuples by keys and put them into a "hash table"
        for j in range(0, len(keys)):
            #modification: if the key is greater than 10k, call secondary hash function to recalculate a key that is smaller than 10k
            if(A[i][1] > 10000):
                A[i][1] = secHash(A[i][1])
            #if the key already exists in the hash table, append the value to the linked list
            if(keys[j].head.data[1] == A[i][1]):
                tracker = keys[j].head
                #traverse through the linked list until it has reached the end, then insert the new node
                while(tracker.next is not None):
                    tracker = tracker.next
                tracker.next = Node(A[i])
                tracker.next.previous = tracker
                break;
            #if the key is not in the hash table, insert it into the hash table
            elif(keys[j].head.data[1] != A[i][1] and j == len(keys)-1):
                newList = linkedList()
                #appends the whole tuple as a node, where the tuple is stored in the data part of the node
                newList.head = Node(A[i])
                keys.append(newList) 
    return keys

def secHash(val):
    #second hash function will take the modulo of the original key and add it to the threshold for a new key value
    #modded value by 10000
    val = val % 10000
    #added modded value to threshold
    val = val + 4500
    return val

def printHash(A):
    outfile1.write("Size of bucket for each key (key:length)")
    outfile1.write("\n")
    for i in range(0, len(A)):
        #writes all the values stored at the hashed key
        A[i].printIt()
        outfile.write("\n")
        #calculates total values in each bucket corresponding to key
        outfile1.write(str(A[i].head.data[1]))
        outfile1.write(":")
        outfile1.write(str(A[i].calLen()))
        outfile1.write("\n")
        

userInput = input("Type in a file with the LCS num, recursive calls tuple.\n")
file = open(userInput, "r")
outfile = open("moddedhash.txt", "w")
outfile1 = open("modHashLen.txt", "w")
A = readFile(file)
B = hashIt(A)  
printHash(B)
outfile1.close()
outfile.close()
file.close()


# # 3e) ii. Creating a new graph with added secondary hash function

# In[1]:


import matplotlib.pyplot as plt
#note: could not get plotly to work, so I only used matplotlib to make the graph    
    
#file we will be reading is a file after all the tuples of LCS num and recursive calls have been organized
    #into a hash table and we have calculated the frequencies of reach recursion call
#this function only works if the file was generated by the algorithm in 3b of Homework 5
def readFile(file):
    global key
    global frequency
    key = []
    frequency = []
    for val in file:
        #skip first line since it is just the header
        if(val == "Size of bucket for each key (key:length)\n" or val == "\n"):
            continue; #move on to next iteration
        temp = ""
        for digit in val:
            if digit == '\n':
                frequency.append(int(temp))
                break;
            elif digit == ":":
                key.append(int(temp))
                temp = ""
                tracker = 1
            #will collect all the digits of the recursion value or frequency of the recursion values
            else:
                temp += digit
                
def plotBar(key, frequency):
    plt.bar(key, frequency, width=0.8, color="red")
    plt.xlabel("# of recursive calls")
    plt.ylabel("frequency")
    plt.title("Collision frequency")
    #plt.show()
    plt.savefig("modHashPlt.png")

key = []
frequency = []
userInput = input("Type in a file with the recursion values and their frequencies.\n")
file = open(userInput, "r")
readFile(file)
plotBar(key, frequency)

#converting image to html format
outfile = open("modHashPlot.html", "w")
outfile.write("<!DOCTYPE HTML5>\n")
outfile.write("<html>")
outfile.write("<img src=\"modHashPlt.png\">")
outfile.close()
file.close()


# In[ ]:




