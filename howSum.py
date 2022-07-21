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

def howSum(targetSum,numbers,memo):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return -1

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder,numbers,memo)
        if remainderResult != -1:
            memo[targetSum] = remainderResult + [num] 
            return memo[targetSum]

    memo[targetSum] = -1
    return memo[targetSum] 

# m = targetSum
# n = numbers.length
# 
# Brute Force
# time : O(n^m * m)
# space : O(m)
# 
# Memoized
# time : O(n*m^2)
# space : O(m^2)

print(howSum(7,[2,3],{}))
print(howSum(7,[5,3,4,7],{}))
print(howSum(7,[2,4],{}))
print(howSum(8,[2,3,5],{}))
print(howSum(300,[7,14],{}))