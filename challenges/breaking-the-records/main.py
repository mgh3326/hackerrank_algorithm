#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    previous_result = scores[0]
    min_value = previous_result
    max_value = previous_result
    min_changed_count = 0
    max_changed_count = 0
    for i in range(1, len(scores)):
        current_result = scores[i]
        if current_result > max_value:
            max_value = current_result
            max_changed_count += 1
        elif current_result < min_value:
            min_value = current_result
            min_changed_count += 1

    return [max_changed_count, min_changed_count]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
