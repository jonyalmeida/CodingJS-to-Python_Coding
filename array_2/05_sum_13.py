'''
Array-2 - - sum13

Return the sum of the numbers in the array, returning 0 for an
empty array. Except the number 13 is very unlucky, so it does not
count and numbers that come immediately after a 13 also do not count.

Examples

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
'''


def sum_13(lst):
    if not lst:
        return 0
    return sum(
        [
            lst[i] for i in range(len(lst))
            if lst[i] != 13 and (lst[i-1] != 13 or i == 0)
        ]
    )


print(f'{sum_13([1, 2, 2, 1])} → 6')
print(f'{sum_13([1, 1])} → 2')
print(f'{sum_13([1, 2, 2, 1, 13])} → 6')
print(f'{sum_13([1, 2, 13, 2, 1, 13])} → 4')
print(f'{sum_13([13, 1, 2, 13, 2, 1, 13])} → 3')
print(f'{sum_13([])} → 0')
print(f'{sum_13([13])} → 0')
print(f'{sum_13([13, 13])} → 0')
print(f'{sum_13([13, 0, 13])} → 0')
print(f'{sum_13([13, 1, 13])} → 0')
print(f'{sum_13([5, 7, 2])} → 14')
print(f'{sum_13([5, 13, 2])} → 5')
print(f'{sum_13([0])} → 0')
print(f'{sum_13([13, 0])} → 0')
