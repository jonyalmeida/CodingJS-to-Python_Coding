'''
Array-2 -- sum67

Return the sum of the numbers in the array, except ignore sections of
numbers starting with a 6 and extending to the next 7 (every 6 will be
followed by at least one 7). Return 0 for no numbers.

Examples:

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
'''


def sum_67(lst):
    if not lst:
        return 0
    sum = 0
    add = True
    for i in range(len(lst)):
        n = lst[i]
        if n == 6:
            add = False
            continue
        elif n == 7 and add is False:
            add = True
            continue
        if add:
            sum += n
    return sum


print(f'{sum_67([1, 2, 2])} # → 5')
print(f'{sum_67([1, 2, 2, 6, 99, 99, 7])} # → 5')
print(f'{sum_67([1, 1, 6, 7, 2])} # → 4')
print(f'{sum_67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])} # → 2')
print(f'{sum_67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7])} # → 2')
print(f'{sum_67([2, 7, 6, 2, 6, 7, 2, 7])} # → 18')
print(f'{sum_67([2, 7, 6, 2, 6, 2, 7])} # → 9')
print(f'{sum_67([1, 6, 7, 7])} # → 8')
print(f'{sum_67([6, 7, 1, 6, 7, 7])} # → 8')
print(f'{sum_67([6, 8, 1, 6, 7])} # → 0')
print(f'{sum_67([])} # → 0')
print(f'{sum_67([6, 7, 11])} # → 11')
print(f'{sum_67([11, 6, 7, 11])} # → 22')
print(f'{sum_67([2, 2, 6, 7, 7])} # → 11')
