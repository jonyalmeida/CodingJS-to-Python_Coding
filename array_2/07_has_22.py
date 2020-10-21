'''
Array-2 -- has22

Given an array of ints, return true if the array contains a 2 next
to a 2 somewhere.

Examples:

has22([1, 2, 2]) → true
has22([1, 2, 1, 2]) → false
has22([2, 1, 2]) → false
'''


def has_22(lst):
    for i in range(len(lst)-1):

        if lst[i] == 2 == lst[i+1] or lst[-i-1] == 2 == lst[-i-2]:
            return True
    return False


print(f'{has_22([1, 2, 2])} → true')
print(f'{has_22([1, 2, 1, 2])} → false')
print(f'{has_22([2, 1, 2])} → false')
print(f'{has_22([2, 2, 1, 2])} → true')
print(f'{has_22([1, 3, 2])} → false')
print(f'{has_22([1, 3, 2, 2])} → true')
print(f'{has_22([2, 3, 2, 2])} → true')
print(f'{has_22([4, 2, 4, 2, 2, 5])} → true')
print(f'{has_22([1, 2])} → false')
print(f'{has_22([2, 2])} → true')
print(f'{has_22([2])} → false')
print(f'{has_22([])} → false')
print(f'{has_22([3, 3, 2, 2])} → true')
print(f'{has_22([5, 2, 5, 2])} → false')
