#Code Written by : John Nixon
#Date: 22:07:2022  Time: 15:45:11
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

# Write a function 'canSum(targetSum,numbers)' that takes in a targetSum
# and an array of numbers as arguments

# The function should return boolean indicating whether or not it is possible
# to generate the targetSum using numbers from the array

# You may use an element of the array as many times as needed

# You may assume that all input numbers are non-negative

def canSum(targetSum,numbers):
    table = [False for _ in range(targetSum+1)]
    table[0] = True 
    i = 0
    while i <= targetSum:
        if table[i]:
            for num in numbers:
                if i+num <= targetSum:
                    table[i+num] = True

        i += 1
    # print(table)
    return table[targetSum]

print(canSum(7,[5,3,4]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
print(canSum(300,[7,14]))