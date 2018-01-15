"""
Longest palindrome in a string

https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
"""

my_string = 'forgeeksskeegfor'

final_result = list()
temp_result = list()

for index, item in enumerate(zip(my_string, ''.join(reversed(my_string)))):
    if item[0] == item[1]:
        temp_result.append(item)
    elif temp_result:
        final_result.append(temp_result)
        temp_result = list()

print ''.join(item[0] for item in max(final_result, key=len))
