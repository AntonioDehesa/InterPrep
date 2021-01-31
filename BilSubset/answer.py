#!/bin/python3

import math
import re
import sys

"""
Statement
Input format
First line contains number an integer N <= 1000.
Second line contains N space separated integers where i^th integer is 1 <= A[i]<=1000

Output format
An integer which is size of largest subset with pairs i^th and j^th which are divisible by each other, and 1<= i, j <= size of subset. 
"""

# Complete the isValid function below.
def bs(arr, n):
    hm = {}
    for i in range(n-1,-1,-1):
        up = arr[i]
        for j in range(i+1,n):
            if up%arr[j] == 0 or arr[j] % up == 0:
                temp = up if up < arr[j] else arr[j]
                hm[temp] = hm.get(temp,0) + 1
    return max(list(hm.values()))
    #print(s)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    result = bs(arr,n)
    print(result)