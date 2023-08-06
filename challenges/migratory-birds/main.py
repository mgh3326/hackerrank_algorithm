#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    count_dict = {}
    for val in arr:
        count_dict[val] = count_dict.get(val, 0) + 1

    max_count = 0
    result_value = None

    for key, count in count_dict.items():
        if count > max_count:
            result_value = key
            max_count = count
        elif count == max_count:
            result_value = min(result_value, key)

    return result_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
