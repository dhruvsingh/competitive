#!/bin/python
# https://www.hackerrank.com/contests/w31/challenges/zero-one-game/problem

g = int(raw_input().strip())

for a0 in xrange(g):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    count = 0

    for i in xrange(len(arr)):
        try:
            if arr[i] == arr[i + 2] == 0:
                del(arr[i + 1])
                count += 1
        except IndexError:
            break

        if count == 0:
            print 'Bob'
        elif count % 2 == 0:
            print 'Bob'
        else:
            print 'Alice'
