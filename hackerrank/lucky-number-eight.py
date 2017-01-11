#!/bin/python
# https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight
from itertools import combinations

n = int(raw_input().strip())
number = raw_input().strip()

count = 0
for i in xrange(1, n+1):
    for _ in combinations(number, i):
        if long(''.join(_)) % 8 == 0:
            count += 1
  
print count % (10 ** 9 + 7)

