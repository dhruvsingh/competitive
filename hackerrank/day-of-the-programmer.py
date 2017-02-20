#!/bin/python
# https://www.hackerrank.com/contests/w29/challenges/day-of-the-programmer

import calendar

y = int(raw_input().strip())
# your code goes here
sum = 0

for month in xrange(1, 13):
    days = calendar.monthrange(y, month)[1]
    if sum + days > 256:
        break
    else:
        sum += days

if len(str(month)) < 2:
    month = '0{}'.format(month)

print '{}.{}.{}'.format(256 - sum, month, y)
