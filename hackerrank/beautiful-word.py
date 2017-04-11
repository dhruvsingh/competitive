#!/bin/python/
# https://www.hackerrank.com/contests/w31/challenges/beautiful-word

from itertools import permutations

print_yes = 0
w = raw_input().strip()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
vowels = ['{}{}'.format(x, y) for x, y in permutations(vowels, 2)]

for i, item in enumerate(w):
    try:
        if w[i] == w[i + 1]:
            print 'No'
            break
    except IndexError:
        print_yes = 1
else:
    print_yes = 1

if print_yes and any(([True for item in vowels if item in w])):
    print 'No'
    print_yes = 0

if print_yes:
    print 'Yes'
