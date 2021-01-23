#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
	prices = [x for x in prices if x <= k]
	prices = sorted(prices)
	suma = 0
	count = 0
	print(prices)
	for i in prices:
		if suma+i <= k:
			suma+=i
			count+=1
		else:
			break
	return count

if __name__ == '__main__':
	arr = [1, 12, 5, 111, 200, 1000, 10]
	k = 50
	print(maximumToys(arr, k))
	arr = [1, 2, 3, 4]
	k = 7
	print(maximumToys(arr,k))
"""
# Complete the maximumToys function below.
def maximumToys(prices, k):
	sorted(prices)
	toysToBuy = dict()
	temp = 0
	toPay = 0
	prices = [x for x in prices if x <= k]
	for price1 in range(len(prices)):
		for price2 in range(price1,len(prices)):
			#print("(price2 + toPay) <= k: ({} + {}) <= {}".format(price2, toPay, k))
			if (prices[price2] + toPay) <= k:
				toPay+=prices[price2]
				temp+=1
			else:
				break
		if toPay in toysToBuy:
			toysToBuy[toPay].append(temp)
		else:
			toysToBuy[toPay] = [temp]
		toPay = 0
		temp = 0
	maxToys = 0
	for i in range(k):
		if i in toysToBuy and max(toysToBuy[i]) > maxToys:
			maxToys = max(toysToBuy[i])
	#print(toysToBuy)
	return maxToys
"""