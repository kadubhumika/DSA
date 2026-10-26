#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # okay i undertsodd the question all now lets apply code
    pos = [0] * (n + 1)
    used = [False] * (n + 1)
    for i in range(1, n + 1):
        val1 = i - k
        val2 = i + k
        if 1 <= val1 <= n and not used[val1]:
            pos[i] = val1
            used[val1] = True
        elif 1 <= val2 <= n and not used[val2]:
            pos[i] = val2
            used[val2] = True

        else:
            return [-1]
    return pos[1:]

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
