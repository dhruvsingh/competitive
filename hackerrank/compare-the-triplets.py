#!/bin/python3
# https://www.hackerrank.com/challenges/compare-the-triplets/problem


def solve(a0, a1, a2, b0, b1, b2):
    points_for_alice = 0
    points_for_bob = 0

    if a0 > b0:
        points_for_alice += 1
    elif not (a0 == b0):
        points_for_bob += 1

    if a1 > b1:
        points_for_alice += 1
    elif not (a1 == b1):
        points_for_bob += 1

    if a2 > b2:
        points_for_alice += 1
    elif not (a2 == b2):
        points_for_bob += 1

    return points_for_alice, points_for_bob


a0, a1, a2 = map(int, input().strip().split(' '))
b0, b1, b2 = map(int, input().strip().split(' '))
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
