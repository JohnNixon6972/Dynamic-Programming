#Code Written by : John Nixon
#Date: 21:07:2022  Time: 12:59:49
#Copyrights are applicable
import sys
import os
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

def bestSum(targetSum,numbers,memo):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return -1
    
    shortestCombination = -1

    for num in numbers:
        remainder = targetSum - num 
        remainderCombination = bestSum(remainder,numbers,memo)

        if remainderCombination != -1:
            combination = remainderCombination + [num]
            # if the combination is  shorter tha  the "shortest", update it
            if shortestCombination == -1 or len(combination) < len(shortestCombination):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return memo[targetSum]

# m= targetSum
# n = numbers.length

# Brute Force
# time : O(n^m*m)
# space : O(m^2)

# Memoized
# time : O(m^2 * n)
# space : O(m^2)

print(bestSum(7,[5,3,4,7],{}))
print(bestSum(8,[2,3,5],{}))
print(bestSum(8,[1,4,5],{}))
print(bestSum(500,[1,2,100],{}))