#!/bin/python3

import math
#import os
#import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    #Brute Strength
    arr.sort()                                                          #We sort the array. This will make everything else so much easier. 
    #print(arr)
    results = []                                                        #The temporal results will be stored in results. we could instead calculate the minimum with an integer, but, we would need a comparison for every operation. might be too slow. 
    chunks = []                                                         #Chunks will store the temporal arrays the size of k.
    for j in range(k):
        chunks.append(arr[j])                                           #The first chunk of size k is created. then, we can simply delete the first element (chunks.pop(0)) and append the next element (chunks.append())
    #print(chunks)
    for i in range(len(arr)-k):
        #print("Current case: {}".format(chunks[k-1] - chunks[0]))
        results.append(chunks[k-1] - chunks[0])                         #Append the temporal result to the results array
        #results.append(max(chunks) - min(chunks))
        chunks.pop(0)
        chunks.append(arr[i + k])
        #print(chunks)
    results.append(chunks[k-1] - chunks[0])                             #One last result, to consider the final chunk
    return min(results)                                                 #We return the smallest of the results. 

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    result = maxMin(k, arr)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()