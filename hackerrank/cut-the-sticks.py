#!/bin/python/
# https://www.hackerrank.com/challenges/cut-the-sticks

n = int(raw_input().strip())
arr = sorted(map(int, raw_input().strip().split(' ')))

for num in arr:
    count = len(arr)
    if count == 0:
        break
    print count
    arr = [num - arr[0] for num in arr if num - arr[0] != 0]
