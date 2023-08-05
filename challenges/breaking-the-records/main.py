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
    previous_score = scores[0]
    min_score = previous_score
    max_score = previous_score
    min_changed_count = 0
    max_changed_count = 0

    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_changed_count += 1
        elif score < min_score:
            min_score = score
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
