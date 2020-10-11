'''
Warmup-1 - - sumDouble

Given two int values, return their sum. Unless the two values are
the same, then return double their sum.

Examples:

sumDouble(1, 2) → 3
sumDouble(3, 2) → 5
sumDouble(2, 2) → 8
'''


def sum_double(a, b):
    if a == b:
        return 2*(a+b)
    else:
        return a+b


'''
Manual testing
'''

print(f'{sum_double(1, 2)} → 3	✔')
print(f'{sum_double(3, 2)} → 5	✔')
print(f'{sum_double(2, 2)} → 8	✔')
print(f'{sum_double(-1, 0)} → -1 ✔')
print(f'{sum_double(3, 3)} → 12  ✔')
print(f'{sum_double(0, 0)} → 0	✔')
print(f'{sum_double(0, 1)} → 1	✔')
print(f'{sum_double(3, 4)} → 7   ✔')
