#!/bin/python3

import math
import os
import random
import re
import string
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    split_s = s.split(":")
    hour = int(split_s[0])
    minute = split_s[1]
    second = split_s[2][:2]
    am_pm = split_s[2][2:]
    if am_pm == "PM":
        if hour < 12:
            hour += 12
    else:
        if hour >= 12:
            hour -= 12
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)

    s = hour + ":" + minute + ":" + second
    return s
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
