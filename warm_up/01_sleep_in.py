'''
Warmup-1 - - sleepIn

The parameter weekday is true if it is a weekday, and the parameter
vacation is true if we are on vacation. We sleep in if it is not a
weekday or we're on vacation. Return true if we sleep in .

Examples

sleepIn(true, true) → true
sleepIn(true, false) → false
sleepIn(false, true) → true
'''


def sleepIn(weekday, vacation):
    return (not weekday) or vacation


'''
Manual testing.
'''

print(f'is{sleepIn(True, True)} # → True ✔')
print(f'is {sleepIn(True, False)} # → False ✔')
print(f'is {sleepIn(False, True)} # → True ✔')
print(f'is {sleepIn(False, False)} # → True ✔')
