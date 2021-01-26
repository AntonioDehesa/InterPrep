#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    if not s:
        return "No"
    if len(s) <= 3:
        return "Yes"
    fa = [0]*26
    for char in s:
        fa[ord(char) - 97] += 1
    fa = [x for x in fa if x > 0]
    fa = sorted(fa)
    min = fa[0]
    max = fa[len(fa)-1]
    if min == max:
        return "Yes"
    if (max - min == 1) and max > fa[len(fa)-2]:
        return "Yes"
    if min == 1 and fa[1] == max:
        return "Yes"
    return "No"
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
