# Link to the problem statement : https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    minSum=0
    maxSum=0
    for i in range(4):
       minSum=minSum+arr[i]
       maxSum=maxSum+arr[len(arr)-i-1]
    
    
    print("{} {}".format(minSum,maxSum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    
    miniMaxSum(arr)
