# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/array-left-rotation

n, d = map(int, raw_input().split())
a = map(str, raw_input().split())
print ' '.join(a[d:] + a[0:d])
