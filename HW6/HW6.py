#!/usr/bin/env python
# coding: utf-8

# # Name: Ivy Truong
# # Class: CSCI 3412
# # Date: 4/26/20
# # Homework 6

# # 1) Dijkstra's Algorithm

# In[3]:


import copy

def readFile(file):
    nestedList = []
    
    for line in file:
        temp = []
        for num in line.split():
            if num == '\n':
                break;
            temp.append(int(num))
        nestedList.append(temp)
    
    return nestedList;
    
def sortByWeight(array):
    temp = []
    newArr = []

    #copy array 
    for k in range(1, len(array)):
        temp.append(array[k])

    #sort array by weights, keeping the source nodes in order
    for i in range (1, len(array)): #iterate through all values in array
        smallest = temp[0]
        for j in range (0, len(temp)): #compare current smallest to all values in temp array
            #check that the source nodes are the same
            if smallest[0] == temp[j][0]:
                #check if the current smallest is greater than the value it is comparing
                if smallest[2] > temp[j][2]:
                    #replace old smallest with the new smallest
                    smallest = temp[j]
            elif smallest[0] != temp[j][0]: #attempts to compare in sections, where it sorts the weights for each node type (sort weights for node 1, then weights for node 2, etc.)
                break;
        newArr.append(smallest)
        temp.remove(smallest) #delete smallest
        
    print("Sorted array of edges:")
    outfile.write("\nSorted array of edges:\n")
    print(newArr)
    outfile.write(str(newArr))
    return newArr

#function to calculate indirect paths to starting node, will be used to find the minimum value of the edge that reaches a destination node
def calcPath(edges, currEdge, relaxed):
    totalLength = currEdge[2]
    smallest = 0

    for e in edges:
        #if the destination node of the current edge to be checked matches with the source node of the relaxed edge,
        #then add the weight of the relaxed edge to the total length
        #for example, if a relaxed edge is 1 2 3 and another edge to be inserted is 3 2 1, we need to add 1 to the weighted edge with a 
        #source of 1 and destination of 3. This will be used to see if this length is less that the relaxed edge 1 2 3.
        if currEdge[0] == e[1] or currEdge[0] == e[0]:
            if e[2] == -1:
                break;
            else:
                totalLength += e[2]
            break;

    #separate loop to find corresponding total path to compare to
    for e1 in edges:
        if relaxed[0] == e1[0] and relaxed[1] != e1[1]:
            continue;
        elif relaxed == e1 or relaxed[1] == e1[1]:
            corrEdge = e1
            if corrEdge[2] == -1:
                corrEdge[2] = totalLength + 1 #attempting to represent an edge that does not exist
            break;

    #compare which is bigger
    smallest = min(corrEdge[2], totalLength)
    #print(smallest)

    #update the total length of the path starting from the original node
    corrEdge[2] = smallest

    #return an indicator if there was an update or not
    if smallest == totalLength: #if the shortest path was updated, tell SSSP function
        return 1
    return 0
    
def totalPath(edges, currEdge):
    totalLength = currEdge[2]
    for i in range(len(edges)):
        #if the destination node of the current edge to be checked matches with the source node of the relaxed edge,
        #then add the weight of the relaxed edge to the total length
        #for example, if a relaxed edge is 1 2 3 and another edge to be inserted is 3 2 1, we need to add 1 to the weighted edge with a 
        #source of 1 and destination of 3. This will be used to see if this length is less that the relaxed edge 1 2 3.
        
        #if the source node of current edge matches, add the weight to the present path
        if (currEdge[0] == edges[i][0]):
            if edges[i][2] == -1:
                edges[i][2] = totalLength
            else:
                edges[i][2] += totalLength
            break;
        #if the edge is not a direct path to the source node, there will be extra modifications
        elif(currEdge[0] != edges[i][0] and currEdge[1] == edges[i][1]):
            if edges[i][2] != -1:
                edges[i][2] += totalLength
            elif edges[i][2] == -1:
                edges[i][2] = totalLength
                #adding other parts of path that connect to the original node to get total length in path
                for j in edges:
                    if currEdge[0] == j[1]:
                        totalLength += j[2]
                        edges[i][2] = totalLength
                        break;
            break;
    return edges
            


#simulates Disjktra's Algorithm
def SSSP(array):
    #visited nodes
    visited = []
    #stores relaxed edges
    relaxedEdges = []
    #stores total length of shortest path to each node starting from original node/first node visited
    totalLen = []
    #total number of nodes
    numNodes = array[0][0]
    #print(numNodes)
    #variable to hold temporary values of original array
    temp = []

    #sort the array by source node and weight
    array = sortByWeight(array)
    #visit the first node, this will be the original node where the graph starts and where all shortest paths to other nodes will start
    visited.append(array[0][0])

    #inserting values from original array into a temporary array
    for i in range(0, len(array)):
        temp.append(copy.deepcopy(array[i]))
        #inserting all paths from the first node into totalLen array
        if array[i][0] == array[0][0]:
            totalLen.append(copy.deepcopy(array[i])) 
   

    #relaxing all edges
    while len(visited) != numNodes:
        for i in range(0, len(temp)):
            #relax any edges that are connected to the visited node(s)
            if temp[i][0] not in visited: #only goes to next node if the edge connects to any of the visited nodes
                continue;
            #makes sure that it is not 0 or -1, only wants to relax edges that exist and are not itself
            if temp[i][2] <= 0:
                continue;
            if len(relaxedEdges) == 0:
                relaxedEdges.append(temp[i])
                #makes the destination of this edge a visited node
                visited.append(temp[i][1])
                #removes first instance of edge with current source node
                temp.remove(temp[i])
                continue;
            count = 0
            #checks if an edge to another node exists
            for j in relaxedEdges:
                count += 1
                for l in relaxedEdges:
                    #in the text file, there will be two of the same entries that represent 1 edge for an undirected graph, so don'trelax the same edge twice
                    if temp[i][1] == l[0] and temp[i][0] == l[1]:
                        temp.remove(temp[i])
                #if the destination to a certain node already exists, find the shortest path out of the two edges
                if temp[i][1] == j[1]:
                    #find the shortest path to this node starting from the source edge in the relaxed edge array
                    val = calcPath(totalLen, temp[i], j)
                    #compare the edges with the same destination node and find the one with the lowest weight
                    #if the relaxed edge has the lower weight, no change in relaxed edges
                    #if the current edge being checked has the lower weight, the current edge replaces the relaxed edge it was compared to
                    #finds minimum value using relaxed edge or using current edge
                    if val == 1: #relax edge if the shortest path has updated
                        #if the destination node has not been visited, add it to visited nodes
                        if temp[i][1] not in visited: 
                            visited.append(temp[i][1])
                        #if the edge is an edge that has a smaller path weight, add to list regardless if another edge to the same destination exists 
                        relaxedEdges.append(temp[i])
                        #removes first instance of edge with current source node
                        temp.remove(temp[i])
                    break;
                elif count == len(relaxedEdges):
                    #update total weight of path
                    totalLen = totalPath(totalLen, temp[i])
                    #if the edge is a new edge and does not have a destination node that matches the exisiting relaxed edges, add to list 
                    relaxedEdges.append(temp[i])
                    #if the destination node has not been visited, add it to visited nodes
                    if temp[i][1] not in visited: 
                        visited.append(temp[i][1])
                    #removes first instance of edge with current source node
                    temp.remove(temp[i])
                    break;
            #after finding a corresponding edge, search for the next shortest edge from the beginning of list of unvisited edges
            break;
    #checking the rest of the unvisited edges list just to make sure there is no shorter path
    for m in range(len(temp)):
        if temp[m][2] <= 0:
                continue;
        for n in relaxedEdges:
            if temp[m][1] == n[1]:
                rEdge = calcPath(totalLen, temp[m], n)
                if rEdge == 1:
                    relaxedEdges.append(temp[m])
                    break;

    print("Visited nodes in order.")
    outfile.write("\nVisited nodes in order.\n")
    print(visited)
    outfile.write(str(visited))

    print("Read each nested list in big list as follows: [source node, destination node, weight].")
    outfile.write("\nRead each nested list in big list as follows: [source node, destination node, weight].\n")
    print("Total length of path starting at first node in list to all other nodes.")
    outfile.write("Total length of path starting at first node in list to all other nodes.\n")
    print(totalLen)
    outfile.write(str(totalLen))
    print("All relaxed edges of the graph.")
    outfile.write("\nAll relaxed edges of the graph.\n")
    print(relaxedEdges)
    outfile.write(str(relaxedEdges))
    

user = input("Type in a file to read in as a graph.\n")
file = open(user, "r")
outfile = open("SSSP1.txt", "w")
array = readFile(file)
print("List read from file.")
outfile.write("List read from file.\n")
print(array)
outfile.write(str(array))
SSSP(array)


# # 2a) Least Number of Changes Greedy Algorithm

# In[9]:


#getting an amount using the least number of bills and least number of coins
#with greedy algorithm, getting the highest value bill/coin then going down the list would be the most optimal
change = [100,50,20,10,5,1,0.5,0.25,0.1,0.05,0.01]
numChange = []

def moneyChange(val, change, numChange):
    for amount in change:
        check = int(val/amount)
        if (check != 0):
            numChange.append(check)
            check = check * amount
            val -= check
            val = round(val,2)
        else:
            numChange.append(0)
    return numChange
            
def printChange(change, numChange):
    for i in range(len(numChange)):
        print("Number of: $" + str(change[i]) + " --> " + str(numChange[i]))
        

user = input("Type in an amount you want to convert to change.\n")
user = float(user)
moneyChange(user, change, numChange)
printChange(change, numChange)


# # 2b) Counting total number of ways to get change for any specific amount

# In[2]:


change = [0.01,0.05,0.1,0.25,0.5,1,5,10,20,50,100]
tempChange = [0.01,0.05,0.1]               
                
#source referenced and implemented algorithm to find least number of coins/bills to make change: https://www.youtube.com/watch?v=jgiZlGzXMBw
def numWays(val, change):
    table = []
    #the number of rows represents each time we increment the amount by 0.01, so if we want to find the number of ways to
    #represent 0.12, we need to figure out the subproblems for the number of ways to represent values from 0.0 to 0.11 in order to
    #figure out the number of ways to represent 0.12
    numRows = int(val/change[0])
    #making it into an integer value to make it easier to work with
    val = val*100

    #multiply everything in change by 100 so we don't have to deal with decimals
    for i in range(len(change)):
        change[i] = int(change[i]*100)

    #append the rows and columns for the DP table
    for j in range(numRows+1): #add 1 to include making change for an amount of 0 and using 0 coins
        table.append([])

    #using dynamic programming to get the total number of ways an amount can be represented
    for k in range(numRows + 1):
        for m in range(len(change) + 1):
            #if the amount we want to make is 0 and we have the option of using coins, then there is exactly one way to make change for an amount of 0, using no coins
            if k == 0 and m >= 0:
                table[k].append(1)
            #if we have no coins and want to make an amount greater than 0, then there are no ways we can make change for that amount
            elif k != 0 and m == 0:
                table[k].append(0)
            #if the next highest coin we use is bigger than the actual amount, then we cannot use the coin
            elif change[m-1] > k:
                table[k].append(table[k][m-1])
            #if the next highest coin is smaller or equal to the actual amount, we are able to use the coin to make change for the amount
            elif change[m-1] <= k:
                leftover = k - change[m-1] #new index for k, calculating how much is leftover after using the coin
                total = table[k][m-1] + table[leftover][m] #gets the value from above the current position if we were not going to use the coin and obtains the value
                #from the position where the leftover value lies if we do use the coin
                #the total is the number ways if we don't use the coin plus the number of ways if we do use the coin
                table[k].append(total)
    return table[numRows][len(change)]

user = input("Type in an amount you want to learn the number of ways it can be represented in a combination of bills and coins.\n")
user = float(user)
ways = numWays(user, change)
print("Total number of ways to represent value: " + str(ways))


# In[ ]:




