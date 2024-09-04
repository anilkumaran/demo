#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY x as parameter.
#


def permute(nums, l, r, permute_list):
    if l == r:
        print(tuple(nums))
        permute_list.append(tuple(nums))
    else:
        for i in range(l, r+1):
            # Swap the current element with the element at index l
            nums[l], nums[i] = nums[i], nums[l]
            # Recurse with the next element
            permute(nums, l+1, r, permute_list)
            # Backtrack to the original configuration
            nums[l], nums[i] = nums[i], nums[l]
    

def get_matches(x, permute_list):
    matches = {}
    indexes_to_match = [x.index(i) for i in x if int(i)]
    for (line_index, line) in enumerate(permute_list, 1):
        print(f'comparing {line_index}: {line}')
        if all(x[idx] == str(line[idx]) for idx in indexes_to_match):
            print(f'line: {line}')
            matches[line_index] = line
    return matches

def solve(x):
    # Write your code here
    input_n = len(x)
    sum_of_lines = 0

    digits = [n for n in range(1, input_n+1)]

    # Generate and print all permutations
    permute_list = []
    permute(digits, 0, len(digits) - 1, permute_list)

    permute_list = sorted(permute_list)
    matches = get_matches(x, permute_list)
    sum_of_lines = sum([line_num for line_num in matches])
    return sum_of_lines

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
