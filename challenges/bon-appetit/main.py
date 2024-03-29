#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    actual_average_bill = (sum(bill) - bill[k]) / 2
    if b - actual_average_bill > 0:
        return str(int(b - actual_average_bill))
    else:
        return "Bon Appetit"


def print_result(bill, k, b):
    print(bonAppetit(bill, k, b))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    print_result(bill, k, b)
