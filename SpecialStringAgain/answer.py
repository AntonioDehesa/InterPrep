#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    i = 0
    ans = 0
    sameCharCount = [0] * n
    while i < n:
        j= i+1
        c = 1
        while j<n and s[i]==s[j]:
            j+=1
            c+=1
        ans+= (c*(c+1))//2
        sameCharCount[i]=c
        i = j
    for j in range(1, n-1):
        if s[j] == s[j-1]:
            sameCharCount[j] = sameCharCount[j-1]
        if s[j-1] == s[j+1] and s[j] != s[j-1]:
            ans+= min(sameCharCount[j-1], sameCharCount[j+1])
    return ans
if __name__ == '__main__':
    n = int(input())
    s = input()
    result = substrCount(n, s)
    print(result)