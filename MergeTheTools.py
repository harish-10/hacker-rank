# Link to the problem statement : https://www.hackerrank.com/challenges/merge-the-tools/problem

from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    n= len(string)
    for i in range(0, n, k):
        t=string[i:i+k]
        print("".join(OrderedDict.fromkeys(t)))


