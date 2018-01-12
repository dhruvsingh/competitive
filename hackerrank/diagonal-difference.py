#!/bin/python3
# https://www.hackerrank.com/challenges/diagonal-difference/problem


def diagonalDifference(a):
    # Complete this function
    # since the matrix is NxN, the length of first element will be the NxN
    n = len(a[0])
    ld = rd = 0

    for i in range(n):
        ld += a[i][i]
        rd += a[i][n - 1 - i]

    return abs(ld - rd)

if __name__ == "__main__":
    a = [list(map(int, input().strip().split(' '))) for _ in range(int(input().strip()))]
    print(diagonalDifference(a))
