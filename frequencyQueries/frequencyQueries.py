#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries: list):
    my_dict = dict()
    frequencies = defaultdict(set)
    res = list()
    for command, value in queries:
        if(command == 1):
            frequencies[my_dict.get(value,0)].discard(value)
            my_dict[value] = my_dict.get(value,0) + 1
            frequencies[my_dict[value]].add(value)
        elif(command == 2):
            frequencies[my_dict.get(value,0)].discard(value)
            my_dict[value] = max(0,my_dict.get(value,0) - 1)
            frequencies[my_dict[value]].add(value)
        elif(command == 3):
            res.append(1 if frequencies[value] else 0)    
    return res
if __name__ == '__main__':
    fptr = open('res.txt', 'w')

    q = int(input().strip())
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
    #print(ans)
    exp = open("expectedOutput03.txt", "r")
    print(ans == exp.read())