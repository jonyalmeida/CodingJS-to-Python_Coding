'''
Warmup-1 -- makes10

Given 2 ints, a and b, return true if one of them is 10 or if their
sum is 10.

Examples:

makes_10(9, 10) → true
makes_10(9, 9) → false
makes_10(1, 9) → true
'''


def makes_10(a, b):
    return (a == 10 or b == 10) or a+b == 10


print(f'{makes_10(9, 10)} → True	✔')
print(f'{makes_10(9, 9)} → False	✔')
print(f'{makes_10(1, 9)} → True ✔')
print(f'{makes_10(10, 1)} → True	✔')
print(f'{makes_10(10, 10)} → True ✔')
print(f'{makes_10(8, 2)} → True ✔')
print(f'{makes_10(8, 3)} → False	✔')
print(f'{makes_10(10, 42)} → True ✔')
print(f'{makes_10(12, -2)} → True ✔')
