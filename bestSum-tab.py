#Code Written by : John Nixon
#Date: 23:07:2022  Time: 09:21:57
#Copyrights are applicable
from re import L
import sys
import os

from matplotlib.pyplot import table
sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass

# Write a function 'bestSum(targetSum,numbers)' that takes in a targetSum
# and a an array of numbers as arguments.

# The finction should retuirn an array containing the shortest
# Combination of numbers that add up to exactly the targetSum

# If there is a tie for the shortest combination,
# you may return any one of the shortest.

def bestSum(targetSum,numbers):
    table = ["null" for _ in range(targetSum+1)]
    table[0] = []
    for i in range(targetSum+1):
        if table[i] != "null":
            for num in numbers:
                if num + i <= targetSum:
                    curr = table[i] + [num]
                    if table[i+num] == "null":
                        table[i+num] = curr
                    elif len(table[i+num]) > len(curr):
                        table[i+num] = curr
    return table[targetSum]

print(bestSum(7,[5,3,4,7]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
print(bestSum(500,[1,2,100]))