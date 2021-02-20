#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
#This is not perfect, but it works, and runs within the limit of time.
def whatFlavors(cost, money):
    #In this section, we create a hashmap with the costs associated to the positions. 
    costFirst = {}
    for m,c in enumerate(cost):
        if c in costFirst:
            costFirst[c].append(m)
        else:
            costFirst[c] = [m]


    #We create the res list
    res = []

    #We look for the two costs that would complete the pooled money. i is obviously in the list, so we just need to look for money -i. 
    for i in sorted(cost):
        if (money - i) in costFirst:
            if i == money - i:
                res.append(costFirst[i][0])
                res.append(costFirst[i][1])
            else: 
                res.append(costFirst[i][0])
                res.append(costFirst[money - i][0])
            break
    res.sort()
    print("{},{}".format(res[0]+1, res[1]+1))
    #return "{},{}".format(res[0]+1, res[1]+1)
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        #print(whatFlavors(cost, money))
        whatFlavors(cost, money)