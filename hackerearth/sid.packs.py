# -*- coding: utf-8 -*-
# https://www.hackerearth.com/problem/algorithm/sid-packs/

T = int(input())
result = []
pi = 3.1416
for t in xrange(T):
    N = int(input())
    areas = map(int, raw_input().split())
    tot = sum(map(lambda num: 0.5 * (num/pi) ** 0.5, areas))
    result.append('{:.4f}'.format(4*pi*(tot**2)))

print '\n'.join(map(str, result))

# fails on input test case 8