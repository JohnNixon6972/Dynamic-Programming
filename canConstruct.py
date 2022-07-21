#Code Written by : John Nixon
#Date: 21:07:2022  Time: 14:33:49
#Copyrights are applicable
import sys
import os

sys.setrecursionlimit(10000)
try:
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')
except:
    pass

# Write a function "canConstruct(target,wordBank)" that accepts a target string
# and an array of strings.

# The function should retrun a boolean indicating wether or not the "target" can be
# constructed by concatenating elements of the "wordBank" array.

# you may reuse elements of "wordBank" as many times as needed.

def canConstruct(target,wordBank,memo):

    if target in memo:
        return memo[target]

    if target == "":
        return True 
    
    for word in wordBank:
        if word in target and target.index(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix,wordBank,memo):
                memo[target] = True
                return memo[target]
    
    memo[target] = False
    return memo[target]


print(canConstruct("abcdef",["ab","abc","cd","def","abcd"],{}))
print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"],{}))
print(canConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"],{}))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"],{}))