# https://www.codechef.com/NOV16/problems/ALEXTASK

from itertools import permutations
from fractions import gcd

answer = []
n = int(raw_input())
while n:
    no_of_items = int(raw_input())
    numbers = map(int, raw_input().split())
    possible_lcm = []
    for i in permutations(numbers, 2):
        x, y = i
        possible_lcm.append(x*y//gcd(x, y))

    answer.append(sorted(possible_lcm)[0])
    n -= 1

print '\n'.join(map(str, answer))
