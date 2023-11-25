#Python program to count the frequency of consecutive duplicate elements in a given list of numbers. Use the itertools module.
from itertools import groupby

def count_consecutive_duplicates(nums):
    
    grouped_nums = [(key, len(list(group))) for key, group in groupby(nums)]

    
    consecutive_duplicates = [(key, count) for key, count in grouped_nums if count > 1]

    return consecutive_duplicates


numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
result = count_consecutive_duplicates(numbers)

print("Consecutive duplicate elements and their frequencies:")
for element, frequency in result:
    print(f"{element}: {frequency} times")
