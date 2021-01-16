#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def merge(a, lowerlimit, middle, highlimit):
    c = []
    i = lowerlimit
    j = middle + 1
    s = 0
    while i <= middle and j <= highlimit:
        if a[i] > a[j]:
            # If a[i] > a[j] the element should swap. 
            s += (middle - i + 1)
            c.append(a[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    # Appends the rest of the elements
    while i <= middle:
        c.append(a[i])
        i += 1
    while j <= highlimit:
        c.append(a[j])
        j += 1
    a[lowerlimit: highlimit + 1] = c
    return s
            

def count(a, lowerlimit, highlimit):
    if lowerlimit >= highlimit:
        return 0
    middle = lowerlimit + (highlimit - lowerlimit) // 2
    s = count(a, lowerlimit, middle)
    s += count(a, middle + 1, highlimit)
    s += merge(a, lowerlimit, middle, highlimit)
    return s

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = count(arr, 0, len(arr) - 1)

        print(result)

"""
def merge(a, l, m, h):
    c = []
    i = l
    j = m + 1
    s = 0
    
    while i <= m and j <= h:
        if a[i] > a[j]:
            # there is an inversion
            s += (m - i + 1)
            c.append(a[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
            
    # Adding remaning numbers
    while i <= m:
        c.append(a[i])
        i += 1
    while j <= h:
        c.append(a[j])
        j += 1
        
    
    a[l: h + 1] = c
    
    return s
            

def count(a, l, h):
    if l >= h:
        return 0
    #print(l, h)
    m = l + (h - l) // 2
    s = count(a, l, m)
    s += count(a, m + 1, h)
    s += merge(a, l, m, h)
    return s

def count_inversions(a):
    return count(a, 0, len(a) - 1)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))

"""