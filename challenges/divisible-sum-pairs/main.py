#!/bin/python3
import os


#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#
def combinations(arr, n):
    if n == 0:
        return [[]]

    if len(arr) == 0:
        return []

    return [[arr[0]] + c for c in combinations(arr[1:], n - 1)] + combinations(arr[1:], n)


def divisibleSumPairs(n, k, ar):
    result_num = 0
    for pair in combinations(ar, 2):
        if sum(pair) % k == 0:
            result_num += 1
    return result_num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
