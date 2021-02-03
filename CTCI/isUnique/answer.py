#!/bin/python3
import math
import os
import random
import re
import string
import sys

# Complete the commonChild function below.

def isUnique(s:str) -> bool:
    if not s:
        return True
    tempMap = {}
    for char in s:
        if char in tempMap:
            return False
        tempMap[char] = 1
    return True


if __name__ == '__main__':
    s = input()
    result = isUnique(s)
    print(result)
