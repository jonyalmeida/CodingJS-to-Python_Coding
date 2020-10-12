'''
Array-2 -- bigDiff

Given an array length 1 or more of ints, return the difference between
the largest and smallest values in the array. Note: the built-in
Math.min(v1, v2) and Math.max(v1, v2) methods return the smaller or larger
of two values.

Examples:

bigDiff([10, 3, 5, 6]) → 7
bigDiff([7, 2, 10, 9]) → 8
bigDiff([2, 10, 7, 2]) → 8
'''


def big_diff(lst):
    return max(lst) - min(lst)


print(f'{big_diff([10, 3, 5, 6])} → 7 ✔')
print(f'{big_diff([7, 2, 10, 9])} → 8 ✔')
print(f'{big_diff([2, 10, 7, 2])} → 8 ✔')
print(f'{big_diff([2, 10])} → 8 ✔')
print(f'{big_diff([10, 2])} → 8 ✔')
print(f'{big_diff([10, 0])} → 10 ✔')
print(f'{big_diff([2, 3])} → 1 ✔')
print(f'{big_diff([2, 2])} → 0 ✔')
print(f'{big_diff([2])} → 0	0	✔')
print(f'{big_diff([5, 1, 6, 1, 9, 9])} → 8 ✔')
print(f'{big_diff([7, 6, 8, 5])} → 3 ✔')
print(f'{big_diff([7, 7, 6, 8, 5, 5, 6])} → 3 ✔')
