#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
	numSwaps = 0
	for i in range(len(a)):
		for j in range(len(a) - 1):
			if a[j] > a[j+1]:
				numSwaps+=1
				elem1, elem2 = a[j], a[j+1]
				a[j+1], a[j] = elem1, elem2
	print("Array is sorted in {} swaps.".format(numSwaps))
	print("First Element: {}".format(a[0]))
	print("Last Element: {}".format(a[len(a) - 1]))

if __name__ == '__main__':
    #n = int(input())
    #a = list(map(int, input().rstrip().split()))
    #countSwaps(a)
    arr = [6,4,1]
    countSwaps(arr)
    #print(countSwaps(arr))