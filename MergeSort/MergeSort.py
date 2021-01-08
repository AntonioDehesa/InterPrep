#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def sort_pair(arr0, arr1):
    if len(arr0) > len(arr1):
        return arr1, arr0
    else:
        return arr0, arr1
    
def merge(arr0, arr1):
    inversions = 0
    result = []
    while len(arr0) > 0 and len(arr1) > 0:
        if arr0[0] <= arr1[0]:
            result.append(arr0.pop(0))
        else:
            # count the inversion right here: add the length of left array
            inversions += len(arr0)
            result.append(arr1.pop(0))
            
    if len(arr0) == 0:
        result += arr1
    elif len(arr1) == 0:
        result += arr0
        
    return result, inversions

def sort(arr):
    length = len(arr)
    mid = length//2
    if length >= 2:
        sorted_0, counts_0 = sort(arr[:mid])
        sorted_1, counts_1 = sort(arr[mid:])
        result, counts = merge(sorted_0, sorted_1)
        return result, counts + counts_0 + counts_1
    else:
        return arr, 0

def countInversions(a):
    final_array, inversions = sort(a)
    # print(final_array)
    return inversions
      


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()

"""
# Complete the countInversions function below.
def countInversions(arr: list):
	print(arr)
	temp = []
	mergeSort(arr, temp, 0, len(arr) - 1)
	print(arr)

def mergeSort(arr: list, temp: list, leftStart: int, rightEnd: int):
	print("leftStart: {}".format(leftStart))
	print("rightEnd: {}".format(rightEnd))
	if leftStart >= rightEnd:
		return None
	middle = (leftStart + rightEnd) // 2
	mergeSort(arr, temp, leftStart, middle)
	mergeSort(arr, temp, middle + 1, rightEnd)
	mergeHalves(arr, temp, leftStart, rightEnd)

def mergeHalves(arr: list, temp: list, leftStart: int, rightEnd: int):
	leftEnd = (rightEnd + leftStart) / 2
	rightStart = leftEnd + 1
	size = rightEnd - leftStart + 1
	left = leftStart
	right = rightStart
	index = leftStart
	inversions = 0
	while (left <= leftEnd and right <= rightEnd):
		if arr[left] <= arr[right]:
			temp[index] = arr[left]
			left += 1
		else:
			temp[index] = arr[right]
			right += 1
		index += 1
		inversions+=1
	arr[left:] = temp[index:leftEnd - left + 1]
	arr[right:] = temp[index: rightEnd - right + 1]
	temp[leftStart:] = arr[leftStart: size]
	#system.arraycopy(arr, left, temp, index, leftEnd - left + 1)
	#system.arraycopy(arr, right, temp, index, rightEnd - right + 1)
	#system.arraycopy(temp, leftStart, arr, leftStart, size)
"""