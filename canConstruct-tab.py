#Code Written by : John Nixon
#Date: 23:07:2022  Time: 09:33:05
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

def canConstruct(target,wordBank):
    table = [False for _ in range(len(target)+1)]
    table[0] = True

    for i in range(len(target)+1):
        if table[i]:
            for word in wordBank:
                if target[i:i+len(word)] == word:
                    table[i+len(word)] = True


    return table[len(target)]

print(canConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(canConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"]))