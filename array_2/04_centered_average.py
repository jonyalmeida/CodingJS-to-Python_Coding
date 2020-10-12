'''
Array-2 -- centeredAverage

Return the "centered" average of an array of ints, which we'll
say is the mean average of the values, except ignoring the largest
and smallest values in the array. If there are multiple copies of
the smallest value, ignore just one copy, and likewise for the
largest value. Use int division to produce the final average. You
may assume that the array is length 3 or more.

Examples

centeredAverage([1, 2, 3, 4, 100]) → 3
centeredAverage([1, 1, 5, 5, 10, 8, 7]) → 5.2
centeredAverage([-10, -4, -2, -4, -2, 0]) → -3
'''


def centered_average(lst):
    return sum(sorted(lst)[1:-1])//(len(lst)-2)


print(f'{centered_average([1, 2, 3, 4, 100])} → 3 ✔')
print(f'{centered_average([1, 1, 5, 5, 10, 8, 7])} → 5 ✔')
print(f'{centered_average([-10, -4, -2, -4, -2, 0])} → -3 ✔')
print(f'{centered_average([5, 3, 4, 6, 2])} → 4 ✔')
print(f'{centered_average([5, 3, 4, 0, 100])} → 4 ✔')
print(f'{centered_average([100, 0, 5, 3, 4])} → 4 ✔')
print(f'{centered_average([4, 0, 100])} → 4 ✔')
print(f'{centered_average([0, 2, 3, 4, 100])} → 3 ✔')
print(f'{centered_average([1, 1, 100])} → 1 ✔')
print(f'{centered_average([7, 7, 7])} → 7 ✔')
print(f'{centered_average([1, 7, 8])} → 7 ✔')
print(f'{centered_average([1, 1, 99, 99])} → 50 ✔')
print(f'{centered_average([1000, 0, 1, 99])} → 50 ✔')
print(f'{centered_average([4, 4, 4, 4, 5])} → 4	✔')
print(f'{centered_average([4, 4, 4, 1, 5])} → 4 ✔')
print(f'{centered_average([6, 4, 8, 12, 3])} → 6 ✔')
