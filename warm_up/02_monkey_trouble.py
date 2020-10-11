'''
Warmup-1 - - monkeyTrouble

We have two monkeys, a and b, and the parameters aSmile and bSmile
indicate if each is smiling. We are in trouble if they are both
smiling or if neither of them is smiling. Return True if we are in
trouble.

Examples:

monkeyTrouble(True, True) → True
monkeyTrouble(False, False) → True
monkeyTrouble(True, False) → False
'''


def monkeyTrouble(a_smile, b_smile):
    return a_smile == b_smile


'''
Manual testing.
'''

print(f'{monkeyTrouble(True, True)} # → True ✔')
print(f'{monkeyTrouble(False, False)} # → True ✔')
print(f'{monkeyTrouble(True, False)} # → False	✔')
print(f'{monkeyTrouble(False, True)} # → False	✔')
