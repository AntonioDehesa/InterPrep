#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#Split the string in two like-characters string
def splitString(s):
    count = Counter(s)
    splitted = {}
    for x in count:
        splitted[x] = count[x] // 2
    rever = splitted.copy()
    return splitted, rever

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    splitted, rever = splitString(s)
    res = []
    for char in reversed(s):
        if splitted[char] > 0:
            while res and res[-1] > char and rever[res[-1]] > 0:
                # while res -> if the res array is not empty
                # while res[-1] > char -> if the last element of res is lexicographically bigger than the current char 
                # rever[res[-1]] > 0 -> if there are available chars in rever
                removed = res.pop() # the first element of res is deleted, and we increment one in the available chars, and decrease one in the used chars
                splitted[removed] += 1
                rever[removed] -= 1
            res.append(char)
            splitted[char] -= 1
        else:
            rever[char] -= 1
    return "".join(res)

if __name__ == '__main__':
    s = input()
    result = reverseShuffleMerge(s)
    print(result)