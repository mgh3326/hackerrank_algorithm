#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'nearlySimilarRectangles' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_LONG_INTEGER_ARRAY sides as parameter.
#

def nearlySimilarRectangles(sides):
    answer = 0
    len_sides = len(sides)
    for i in range(len_sides):
        for j in range(len_sides - i - 1):
            if sides[i][0] / sides[i][1] == sides[i + j + 1][0] / sides[i + j + 1][1]:
                answer += 1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sides_rows = int(input().strip())
    sides_columns = int(input().strip())

    sides = []

    for _ in range(sides_rows):
        sides.append(list(map(int, input().rstrip().split())))

    result = nearlySimilarRectangles(sides)

    fptr.write(str(result) + '\n')

    fptr.close()
