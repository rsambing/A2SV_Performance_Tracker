#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a, n):
    # Write your code here
    sp = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if (a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                sp += 1
        if sp < 0:
            break
    return sp
            
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    sp = countSwaps(a, n)
    print(f"Array is sorted in {sp} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    
