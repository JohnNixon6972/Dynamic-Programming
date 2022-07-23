#Code Written by : John Nixon
#Date: 21:07:2022  Time: 15:23:13
#Copyrights are applicable
import sys
import os
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

def allConstructs(target,wordBank,memo):
    if target in memo:
        return memo[target]

    if target == "":
        return [[]]
    
    result = []
    for word in wordBank:
        if word in target and target.index(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstructs(suffix,wordBank,memo)
            # print(suffixWays)
            targetWays = []
            for i in range(len(suffixWays)):
                suffixWays[i].insert(0,word)
                targetWays.append(suffixWays[i])
            result += targetWays
    
    memo[target] = result
    return memo[target]

# allConstructs("abcdef",["ab","abc","cd","def","abcd","ef","c"])
print(allConstructs("abcdef",["ab","abc","cd","def","abcd","ef","c"],{}))
print(allConstructs("hello",["cat","dog","mouse"],{}))
print(allConstructs("purple",["purp","p","ur","le","purpl"],{}))
print(allConstructs("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz",["a","aa","aaa","aaaa","aaaaa"],{}))