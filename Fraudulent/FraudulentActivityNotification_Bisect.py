#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications = 0
    traExp= expenditure[:d]
    traExp.sort()
    middle = d//2
    isPair = True if (d%2 == 0) else False
    for i in range(d,len(expenditure)):
        try:
            mean = ((traExp[middle] + traExp[middle-1])/2) if isPair else traExp[middle]
            if (mean*2 <= expenditure[i]):
                notifications+=1
            del traExp[bisect.bisect_left(traExp, expenditure[i-d])]
            bisect.insort(traExp, expenditure[i])
        except IndexError as e:
            return notifications
    return notifications

if __name__ == '__main__':
    #fptr = open("res.txt", 'w')
    
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    #result = activityNotifications(expenditure, d)

    #fptr.write(str(result) + '\n')

    #fptr.close()
    print(activityNotifications(expenditure,d))
