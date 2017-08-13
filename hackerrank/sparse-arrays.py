# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/sparse-arrays

N = int(raw_input())
arr, rs = []

for _ in xrange(N):
    arr.append(str(raw_input()))

Q = int(raw_input())

for _ in xrange(Q):
    rs.append(arr.count(str(raw_input())))

print '\n'.join(map(str, rs))
