#Code Written by : John Nixon
#Date: 23:07:2022  Time: 09:49:45
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

# Write a function countConstruct(target,wordBank) that accepts a target
# string and an array of strings.

# The function should return the number of ways that the 'target' can
# be constructed by concatenating elements of the 'wordBank' array.

def countConstruct(target,wordBank):
    table = [0 for _ in range(len(target)+1)]
    table[0] = 1
    for i in range(len(target)+1):
        if table[i] != 0:
            for word in wordBank:
                if target[i:i+len(word)] == word:
                    table[i+len(word)] += table[i]

    return table[len(target)]

print(countConstruct("purple",["purp","p","ur","le","purpl"]))
print(countConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"]))