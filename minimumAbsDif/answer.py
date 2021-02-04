#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    minNumber = abs(arr[0] - arr[1])
    for i in range(1, len(arr) - 1):
        minNumber = min(minNumber, arr[i] - arr[i+1])
        if minNumber == 0:
            break
    return minNumber

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
