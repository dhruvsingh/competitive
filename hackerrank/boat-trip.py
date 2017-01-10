# !/bin/python
# https://www.hackerrank.com/contests/w28/challenges/boat-trip

n, c, m = map(int, raw_input().strip().split(' '))
p = map(int, raw_input().strip().split(' '))
if m * c < sorted(p)[::-1][0]:
    print 'No'
else:
    print 'Yes'
