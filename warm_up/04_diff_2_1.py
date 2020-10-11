'''
Warmup-1 -- diff21

Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.

Examples:

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''


def diff21(n):
    if n > 21:
        return 2*(abs(n - 21))
    else:
        return abs(n-21)


'''
Manual testing.
'''

print(f'{diff21(19)}  # → 2	✔')
print(f'{diff21(10)}  # → 11 ✔')
print(f'{diff21(21)}  # → 0	✔')
print(f'{diff21(22)}  # → 2	✔')
print(f'{diff21(25)}  # → 8	✔')
print(f'{diff21(30)}  # → 18 ✔')
print(f'{diff21(0)} # → 21 ✔')
print(f'{diff21(1)} # → 20 ✔')
print(f'{diff21(2)} # → 19 ✔')
print(f'{diff21(-1)}  # → 22 ✔')
print(f'{diff21(-2)}  # → 23 ✔')
print(f'{diff21(50)}  # → 58 ✔')
