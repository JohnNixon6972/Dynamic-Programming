from re import L
import sys
import os
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

def canSum(targetSum,numbers,memo={}):
    #check if solution for sub value of target sum exists 
    if targetSum in memo:
        return memo[targetSum]

    #check if target sum is achieveable
    if targetSum == 0:
        return True 
    
    #check if target sum becomes neagtive denoting not achieveable
    if targetSum < 0:
        return False
    
    # Itterate through the numbers to reduce the targetsum
    for num in numbers:
        remainder = targetSum - num 
        if canSum(remainder,numbers,memo):
            memo[targetSum] = True
            return True 

    memo[targetSum] = False
    return False

print(canSum(7,[2,3],{}))
print(canSum(7,[5,3,4,7],{}))
print(canSum(7,[2,4],{}))
print(canSum(8,[2,3,5],{}))
print(canSum(300,[7,14],{}))