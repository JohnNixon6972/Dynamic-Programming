#Code Written by : John Nixon
#Date: 22:07:2022  Time: 15:15:31
#Copyrights are applicable
import sys
import os

from matplotlib.pyplot import table
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

def gridTraveller(m,n):
    table = [[0 for _ in  range(n+1)] for _ in range(m+1)]
    # print(table)
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            if i+1 <= m:
                 table[i+1][j] += table[i][j]
            
            if j+1 <= n:
                table[i][j+1] += table[i][j]

    return table[m][n]

print(gridTraveller(1,1))
print(gridTraveller(2,3))
print(gridTraveller(3,2))
print(gridTraveller(3,3))
print(gridTraveller(180,180))