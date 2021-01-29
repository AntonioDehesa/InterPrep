#!/bin/python3

import math
import re
import sys

"""
Statement
Input format
First line contains number of test cases T. 
Next, each test case contains two lines, first line contains the pattern and next line contains a text string.
All characters in both the strings are in lowercase only [a-z]

Output format
For each test case print YES or NO depending on whether any permutation of the pattern exists in the text string.
"""

# Complete the isValid function below.
def findPermutations(a,b):
    fm_a = {}
    for char in a:
        fm_a[char] = fm_a.get(char,0) + 1
    for char in b:
        fm_a[char] = fm_a.get(char,0) - 1
    return "NO" if max(list(fm_a.values())) > 0 else "YES"
    #print(s)
if __name__ == '__main__':
    s = int(input())

    #expenditure = list(map(int, input().rstrip().split()))
    for i in range(s):
        a = str(input())
        b = str(input())
        result = findPermutations(a,b)
        print(result)