#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if k >= len(c):
        return sum(c)
    c.sort(reverse=True)
    totalCost = 0
    i = 0
    counter = 0
    for flower in c:
        totalCost = (i + 1) * flower + totalCost
        counter+= 1
        if counter >= k:
            counter = 0
            i+= 1
    return totalCost
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
    #fptr.write(str(minimumCost) + '\n')
    #fptr.close()
