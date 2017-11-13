#!/bin/python3
# https://www.hackerrank.com/contests/w35/challenges/lucky-purchase/problem

n = int(input().strip())
my_result = {}
for a0 in range(n):
    s, n = input().strip().split(' ')
    s, n = [str(s), str(n)]
    count_4, count_7 = n.count('4'), n.count('7')
    if (
        count_4 == count_7 and
        count_4 > 0 and
        count_7 > 0 and
        (count_4 + count_7) == len(n)
    ):
        my_result[int(n)] = s

if len(my_result) == 0:
    print('-1')
else:
    print(my_result[min(my_result.keys())])
