#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def findMedian(arr):
    arr = sorted(arr)

    middle = len(arr) // 2

    return arr[middle]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr = input()

    result = findMedian(arr)

    fptr.write(result + "\n")

    fptr.close()