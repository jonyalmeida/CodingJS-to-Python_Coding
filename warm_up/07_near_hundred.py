'''
Warmup-1 -- nearHundred

Given an int n, return True if it is within 10 of 100 or 200.
Note: Math.abs(num) computes the absolute value of a number.

Examples:

nearHundred(93) → true
nearHundred(90) → true
nearHundred(89) → false
'''


def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


print(f'{near_hundred(93)} → True ✔')
print(f'{near_hundred(90)} → True ✔')
print(f'{near_hundred(89)} → False ✔')
print(f'{near_hundred(110)} → True ✔')
print(f'{near_hundred(111)} → False ✔')
print(f'{near_hundred(121)} → False ✔')
print(f'{near_hundred(0)} → False ✔')
print(f'{near_hundred(5)} → False ✔')
print(f'{near_hundred(191)} → True	✔')
print(f'{near_hundred(189)} → False	✔')
