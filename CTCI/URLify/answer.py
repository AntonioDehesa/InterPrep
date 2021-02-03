#!/bin/python3
import math
import os
import random
import re
import string
import sys

# Complete the commonChild function below.

def URLify(s:str) -> str:
    if not s:
        return ""
    s = s.strip()
    arrS = s.split(" ")
    return "%20".join(arrS)   


if __name__ == '__main__':
    s = input()
    result = URLify(s)
    print(result)
