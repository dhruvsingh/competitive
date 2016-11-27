# -*- coding: utf-8 -*-
# http://www.spoj.com/problems/TEST/

nums = []
num = 0
while num != 42:
    num = int(input())
    if num != 42:
        nums.append(num)

print '\n'.join(map(str, nums))
