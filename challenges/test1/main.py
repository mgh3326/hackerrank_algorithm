#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'possibleChanges' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY usernames as parameter.
#

def possibleChanges(usernames):
    _result = []
    for username in usernames:
        _result.append(possible_username(username))
    return _result


def possible_username(username):
    len_username = len(username)
    for i in range(len_username):
        for j in range(len_username - i - 1):
            if username[i] > username[i + j + 1]:
                return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    usernames_count = int(input().strip())

    usernames = []

    for _ in range(usernames_count):
        usernames_item = input()
        usernames.append(usernames_item)

    result = possibleChanges(usernames)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
