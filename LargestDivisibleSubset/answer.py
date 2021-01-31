#!/bin/python3

import math
import re
import sys

# Complete the isValid function below.
def lds(nums):
    result=[[ele] for ele in nums]
    for firstElement in range(len(nums)):
        for secondElement in range(firstElement): 
            if nums[firstElement]%nums[secondElement]==0 and len(result[firstElement])<(len(result[secondElement])+1): 
                result[firstElement]=result[secondElement]+[nums[firstElement]]
    return max(result,key=len)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    #arr.sort()
    result = lds(arr)
    print(result)