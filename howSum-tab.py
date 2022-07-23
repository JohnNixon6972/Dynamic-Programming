#Code Written by : John Nixon
#Date: 22:07:2022  Time: 15:58:11
#Copyrights are applicable
import sys
import os
sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass

# Write a function 'howSum(targetSum,numbers)' that takes in a targetSum
# and an array of numbers as arguments.

# The function should return an array containing any combination of
# elements that add up to exactly the targetSum. If ther is no 
# combination that adds up to the targetSum, then return null.

# If there are multiple combinations possible, you may return any single one.

def howSum(targetSum,numbers):
    table = [-1 for _ in range(targetSum+1)]
    table[0] = []

    for i in range(targetSum+1):
        if table[i] != -1:
            for num in numbers:
                if i + num <= targetSum:
                    table[i+num] = table[i] + [num]
    # print(table)
    return table[targetSum]

# print(howSum(7,[2,3]))
print(howSum(7,[5,3,4]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(300,[7,14]))
