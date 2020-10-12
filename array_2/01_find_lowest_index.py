'''
Array-2 - - findLowestIndex

Return the index of the minimum value in an array. The input array
will have at least one element in it.

Examples:

findLowestIndex([99, 98, 97, 96, 95]) → 4
findLowestIndex([2, 2, 0]) → 2
findLowestIndex([1, 3, 5]) → 0
'''


def find_lowest_index(lst):
    return lst.index(min(lst))


print(f'{find_lowest_index([99, 98, 97, 96, 95])} → 4	✔')
print(f'{find_lowest_index([2, 2, 0])} → 2 ✔')
print(f'{find_lowest_index([1, 3, 5])} → 0 ✔')
print(f'{find_lowest_index([5])} → 0 ✔')
print(f'{find_lowest_index([11, 9, 0, 1])} → 2 ✔')
print(f'{find_lowest_index([2, 11, 9, 0])} → 3 ✔')
print(f'{find_lowest_index([2])} → 0 ✔')
print(f'{find_lowest_index([2, 5, -12])} → 2 ✔')
