# -*- coding: utf-8 -*-

"""
Ln - n is assumed to be positive (and %2 == 0)
Assumes L1...Ln are same in length.

First iterates over the main list L to trim it down to half the size.
Next repetitively runs over the above list to trim it down untill gets the
common elements.
"""

L = [
    [0, [[1, 2], [3, 4], [2, 3]]],
    [0, [[3, 4], [2, 3]]],
    [0, [[1, 2], [3, 4], [2, 3]]],
    [0, [[3, 4], [1, 2]]]
]


def fix_my_list(my_list):
    """Add common items to a list and return the same"""
    result_list = list()
    for item in range(0, len(my_list), 2):
        result_list.append(
            [sublist for sublist in my_list[item]
                if sublist in my_list[item + 1]]
        )
    return result_list

final_list = list()

for item in range(0, len(L), 2):
    final_list.append(
        [sublist for sublist in L[item][1] if sublist in L[item + 1][1]]
    )

while len(final_list) != 1:
    final_list = fix_my_list((final_list))


print(final_list)
