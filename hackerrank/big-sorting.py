#!/bin/python
# https://www.hackerrank.com/contests/w29/challenges/big-sorting

import sys


n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = long(raw_input().strip())
    unsorted.append(unsorted_t)
# your code goes here

print '\n'.join(map(str, sorted(unsorted)))