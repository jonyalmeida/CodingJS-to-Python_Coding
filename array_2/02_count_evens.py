'''
Array-2 - - countEvens

Return the number of even ints in the given array. Note: the % "mod"
operator computes the remainder, e.g. 5 % 2 is 1.

Examples:

countEvens([2, 1, 2, 3, 4]) → 3
countEvens([2, 2, 0]) → 3
countEvens([1, 3, 5]) → 0
'''


def count_evens(lst):
    return len([n for n in lst if n % 2 == 0])


print(f'{count_evens([2, 1, 2, 3, 4])} → 3 ✔')
print(f'{count_evens([2, 2, 0])} → 3 ✔')
print(f'{count_evens([1, 3, 5])} → 0 ✔')
print(f'{count_evens([])} → 0 ✔')
print(f'{count_evens([11, 9, 0, 1])} → 1 ✔')
print(f'{count_evens([2, 11, 9, 0])} → 2 ✔')
print(f'{count_evens([2])} → 1 ✔')
print(f'{count_evens([2, 5, 12])} → 2 ✔')
