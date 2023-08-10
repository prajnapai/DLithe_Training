#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    stack = []
    maxArea = 0
    n = len(h)
    
    for index,height in enumerate(h):
        start = index
        
        while stack and stack[-1][1] > height:
            i,h = stack.pop()
            maxArea = max(maxArea,(h * (index - i)))
            start = i
        
        stack.append((start,height))
            
    for index,height in stack:
        maxArea = max(maxArea,(height * (n - index)))
                
    return maxArea

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
