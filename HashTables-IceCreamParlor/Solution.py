#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    myDict = {}
    for position,costUnitary in enumerate(cost,1):#we enumerate it from 1. 
        if money - costUnitary in myDict:#if the corresponding pair exists, we print both
            print(myDict[money - costUnitary], position)
            break #as it cannot happen again, we just break the loop. meaning, this 
        else:
            myDict[costUnitary] = position#if the corresponding pair does not exist yet, we just save the position in the corresponding cost.
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)