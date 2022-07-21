#Code Written by : John Nixon
#Date: 21:07:2022  Time: 15:07:23
#Copyrights are applicable
import sys
import os
sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass

# Write a function countConstruct(target,wordBank) that accepts a target
# string and an array of strings.

# The function should return the number of ways that the 'target' can
# be constructed by concatenating elements of the 'wordBank' array.

def countConstruct(target,wordBank,memo):
    if target in memo:
        return memo[target]

    if target == "":
        return 1
    
    totalCount = 0
    for word in wordBank:
        if word in target and target.index(word) == 0:
            numWaysForTheRest = countConstruct(target[len(word):],wordBank,memo)
            totalCount += numWaysForTheRest

    memo[target] = totalCount
    return memo[target]

print(countConstruct("purple",["purp","p","ur","le","purpl"],{}))
print(countConstruct("abcdef",["ab","abc","cd","def","abcd"],{}))
print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"],{}))
print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"],{}))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"],{}))