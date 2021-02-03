#!/bin/python3
import math
import os
import random
import re
import string
import sys

# Complete the commonChild function below.

def checkPermutation(s:str, s2:str) -> bool:
    if not s or not s2:
        return False
    fm1 = [0]*100
    fm2 = [0]*100#Depending on which characters may be in the string, these may change
    for char in s:
        fm1[ord(char) - 97]+=1
    for char in s2:
        fm2[ord(char) - 97]+=1
    for i in range(len(fm1)):
        if fm1[i] < fm2[i]:
            return False
    return True


if __name__ == '__main__':
    s = input()
    s2 = input()
    result = checkPermutation(s,s2)
    print(result)
