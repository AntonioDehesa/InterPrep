#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    current = s[0]
    for i in range(1,len(s)):
        next = s[i]
        if current == next:
            count+= 1
        else:
            current = next
    return count
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)
        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()
