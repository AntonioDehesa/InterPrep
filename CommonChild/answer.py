#!/bin/python3

import math
import os
import random
import re
import string
import sys

# Complete the commonChild function below.

def commonChild(s1, s2):
    """
    This one is a solution found in the discussion section, submitted by the user: ajsmith22.
    This one is much faster than my solution. 
    I understand what is going on, but still, i feel bad that i could not think about it. 
    Still, the important part is learning. 
    """
    prev = [0] * (len(s2)+1)
    curr = [0] * (len(s2)+1)
    for r in s1:
        for j, c in enumerate(s2, 1):
            curr[j] = prev[j-1] + 1 if r == c else max(prev[j], curr[j-1])
        prev, curr = curr,prev
    return prev[-1]



if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print(result)
"""
Working, but slow
# Complete the commonChild function below.
def commonChild(s1, s2):
    if not s1 or not s2:
        return 0
    maxCount = [0]*(len(s1) if len(s1) > len(s2) else len(s2))
    for i in range(len(s1)):
        j = 0
        while j < len(s2):
            print("s1[i] = {}, s2[j] = {}".format(s1[i], s2[j]))
            if s1[i] != s2[j]:
                j+=1
                continue
            found = commonChild(s1[i+1:len(s1)], s2[j+1:len(s2)])
            maxCount[i] = 1 + found
            break
    return max(maxCount)
"""