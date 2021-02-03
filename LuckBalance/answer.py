#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luckCounter = 0
    contests.sort(reverse= True)
    for luck, important in contests:
        if important == 0:
            luckCounter+= luck
        elif k > 0:
            luckCounter+= luck
            k-= 1
        else:
            luckCounter-= luck
    return luckCounter
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
