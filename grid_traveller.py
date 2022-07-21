import sys
import os
sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass

# Say that you are a traveller on a 2D grid. You begin in the top-left corner
# and you goal is to travel to the bottom-right corner. You may only move down or right

# In how many ways can you travel to the goal on a grid with dimensions m * n

#write a function 'gridTraveler(m,n)' that calculates this.

def gridTraveller(m,n,memo= {}):
    # are the arguments in the memo 
    if (m,n) in memo:
        return memo[(m,n)]
    elif (n,m) in memo:
        return memo[(n,m)]
        
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    
    memo[(m,n)] = gridTraveller(m-1,n,memo) + gridTraveller(m,n-1,memo) 
    return memo[(m,n)]

print(gridTraveller(1,1))
print(gridTraveller(2,3))
print(gridTraveller(3,2))
print(gridTraveller(3,3))
print(gridTraveller(1000,1000))