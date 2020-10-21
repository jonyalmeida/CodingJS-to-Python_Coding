'''
Array-2 -- lucky13

Given an array of ints, return true if the array contains no 1's
and no 3's.

Examples:

lucky13([0, 2, 4]) → true
lucky13([1, 2, 3]) → false
lucky13([1, 2, 4]) → false
'''


def lucky_13(lst):
    return not (1 in lst) and not (3 in lst)


print(f'{lucky_13([0, 2, 4])} → true')
print(f'{lucky_13([1, 2, 3])} → false')
print(f'{lucky_13([1, 2, 4])} → false')
print(f'{lucky_13([2, 7, 2, 8])} → true')
print(f'{lucky_13([2, 7, 1, 8])} → false')
print(f'{lucky_13([3, 7, 2, 8])} → false')
print(f'{lucky_13([2, 7, 2, 1])} → false')
print(f'{lucky_13([1, 2])} → false')
print(f'{lucky_13([2, 2])} → true')
print(f'{lucky_13([2])} → true')
print(f'{lucky_13([3])} → false')
print(f'{lucky_13([])} → true')
