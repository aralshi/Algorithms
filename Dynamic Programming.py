#!/usr/bin/env python3
# DP
# Ankita Alshi
import sys
import datetime

def cost(n):
    if (n == val):
        return 1
    if (not memo[n - 1] == -1):
        return memo[n - 1]
    else:
        memo[n - 1] = 0
        for i in a:
            if (not (n + i > val)):
                memo[n - 1] += cost(n + i)  
        return memo[n - 1]

sys.setrecursionlimit(200000)
print ("Enter input number")
val = int(input())
memo = [-1 for i in range(val)]
a = [1, 3, 4]

t1 = datetime.datetime.now()
print (cost(0) % 100000)
t2 = datetime.datetime.now()
print ("Time for computation:", t2 - t1)
