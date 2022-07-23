#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for value in arr:
        if value > 0:
            positive_count += 1
        elif value < 0:
            negative_count += 1
        else:
            zero_count += 1
    total_count = positive_count + negative_count + zero_count
    print('%.6f' % (positive_count / total_count))
    print('%.6f' % (negative_count / total_count))
    print('%.6f' % (zero_count / total_count))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
