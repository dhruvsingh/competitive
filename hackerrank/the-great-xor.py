# !/bin/python
# https://www.hackerrank.com/contests/w28/challenges/the-great-xor

for query in xrange(int(raw_input().strip())):
    x = long(raw_input().strip())
    count = 0
    for a in xrange(1, x):
        if a^x > x:
            count += 1
    print count