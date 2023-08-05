#!/bin/python3

import functools
import os


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    a_result = functools.reduce(compute_lcm, a)
    b_result = functools.reduce(compute_gcd, b)
    result_size = 0
    i = 1
    while True:
        result_i = a_result * i
        if result_i > b_result or result_i > 100:
            break
        if b_result % result_i == 0:
            result_size += 1
        i += 1
    return result_size


def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def compute_lcm(a, b):
    return a * b // compute_gcd(a, b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    fptr.write(str(total) + '\n')
    fptr.close()
