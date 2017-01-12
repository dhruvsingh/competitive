#!/bin/python
# https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight
from itertools import combinations

n = int(raw_input().strip())
number = raw_input().strip()
count = sum(1 for num in number if int(num) % 8 == 0)

if n > 1:
    count += sum(1 for num in combinations(number, 2) if int(''.join(num)) % 8 == 0)

    if n > 2:
        rem_arr = list(combinations(number, 3))
        sub_arr = []
        sub_count = 0
        d = 0
        x = 0
        for a in xrange(n - 2, 0, -1):
            d = (a * (a + 1)) / 2
            sub_arr, rem_arr = rem_arr[:d], rem_arr[d:]
            sub_count = sum(1 for num in sub_arr if int(''.join(num)) % 8 == 0)
            x = (2 ** (n - (a + 2)))
            count = count + (sub_count * x)

print count % ((10**9) + 7)
