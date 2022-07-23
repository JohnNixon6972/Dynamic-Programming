#Code Written by : John Nixon
#Date: 23:07:2022  Time: 09:58:27
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

# Write a function 'allConstruct(traget,wordBank)' that accepts target string
# and an array of strings.

# The function should return a 2D array containing all of the ways 
# that the "target" can be constructed by concatenating elements of the "wordBank" array.
# Each elemenyt of the 2D array should represent one combination that constructs the "traget"

# You may reuse elements of "wordBank" as many times as needed.

def allConstructs(target,wordBank):
    table = [[] for _ in range(len(target)+1)]
    table[0] = [[]]
    
    for i in range(len(target)+1):
        if table[i] != "null":
            for word in wordBank:
                if target[i:i+len(word)] == word:
                    newCombinations = table[i].map(subArray,[*subArray,word])
                        

    return table[len(target)]

print(allConstructs("abcdef",["ab","abc","cd","def","abcd","ef","c"]))
print(allConstructs("hello",["cat","dog","mouse"]))
print(allConstructs("purple",["purp","p","ur","le","purpl"]))
print(allConstructs("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz",["a","aa","aaa","aaaa","aaaaa"]))