#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def dayOfProgrammer(year):
    leap_year_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    not_leap_year_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mix_year_list = [31, 28 - 13, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    developer_days = 256
    if year < 1918:  # Julian
        if year % 4 == 0:  # leap year
            current_list = leap_year_list
        else:
            current_list = not_leap_year_list
    elif year == 1918:  # Mix
        current_list = mix_year_list
    else:  # Gregorian
        if year % 400 == 0 or ((year % 4 == 0) and (year % 100 != 0)):  # leap year
            current_list = leap_year_list
        else:
            current_list = not_leap_year_list
    for i, value in enumerate(current_list):
        developer_days -= value
        if developer_days <= 0:
            break

    result_str = "%02d.%02d.%d" % (value + developer_days, i + 1, year)
    return result_str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
