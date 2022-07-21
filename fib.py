import sys
import os
sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass


#default recursion approach taking 2^n operations
def default_fib(n):
    if n <= 2:
        return 1
    return default_fib(n-1) + default_fib(n-2)



# Fibonicci program using dynamic programing
# memoization - store duplicates of subproblems 
# using dict keys will be arg to fn, value will be the return value
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]


print(fib(1000))