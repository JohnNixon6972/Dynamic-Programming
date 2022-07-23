#Code Written by : John Nixon
#Date: 22:07:2022  Time: 15:01:09
#Copyrights are applicable
import sys
import os
sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass

# Write a function "fib(n)" that take in a number as an argument.
# The function should return thr n-th number of the fibonacci sequence.

# 0th number is 0
# 1th number is 1

def fib(n):
    table = [0 for _ in range(n+1)]
    table[1] = 1

    for i in range(n-1):
        table[i+1] += table[i] 
        table[i+2] += table[i] 

    table[n] = table[n-1] + table[n-2]
    return table[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50000))
