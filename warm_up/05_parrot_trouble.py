'''
Warmup-1 - - parrotTrouble

We have a loud talking parrot. The "hour" parameter is the current
hour time in the range 0..23. We are in trouble if the parrot is
talking and the hour is before 7 or after 20. Return true if we are
in trouble.

Examples:

parrotTrouble(true, 6) → true
parrotTrouble(true, 7) → false
parrotTrouble(false, 6) → false
'''


def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    return False


print(f'{parrot_trouble(True, 6)} → True ✔')
print(f'{parrot_trouble(True, 7)} → False ✔')
print(f'{parrot_trouble(False, 6) } → False ✔')
print(f'{parrot_trouble(True, 21) } → True ✔')
print(f'{parrot_trouble(False, 21)} → False ✔')
print(f'{parrot_trouble(True, 23) } → True ✔')
print(f'{parrot_trouble(False, 23)} → False ✔')
print(f'{parrot_trouble(True, 20) } → False ✔')
print(f'{parrot_trouble(False, 12)} → False ✔')
