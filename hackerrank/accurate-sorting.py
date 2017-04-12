#!/bin/python
# https://www.hackerrank.com/contests/w31/challenges/accurate-sorting

q = int(raw_input().strip())

for a0 in xrange(q):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    # Write Your Code Here

    for i, item in enumerate(a):
        try:
            if abs(item - a[i + 1]) == 1:
                item, a[i + 1] = a[i + 1], item
        except IndexError:
            pass

    if a == sorted(a):
        print 'Yes'
    else:
        print 'No'
