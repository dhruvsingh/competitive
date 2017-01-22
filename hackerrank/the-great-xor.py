# !/bin/python
# https://www.hackerrank.com/contests/w28/challenges/the-great-xor

for query in xrange(int(raw_input().strip())):
    x = long(raw_input().strip())
    count = 0
    no_of_digits = len(str(bin(x))) - 2
    print 2 ** no_of_digits - 1 - x
