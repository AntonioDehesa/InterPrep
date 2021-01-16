#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dictA = {}
    dictB = {}
    dictC = {}
    res = 0
    for char in a:
        dictA[char] = dictA.get(char,0) + 1
        dictC[char] = dictC.get(char,0) + 1
    for char in b:
        dictB[char] = dictB.get(char,0) + 1
    for element in dictB:
        dictC[element] = dictA.get(element, 0) - dictB[element]
    print(dictA)
    print(dictB)
    print(dictC)
    return sum(abs(dictC[i]) for i in dictC)
if __name__ == '__main__':
    a = input()

    b = input()

    res = makeAnagram(a, b)
    print(res)