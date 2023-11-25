#Python program to find the maximum, minimum aggregation pair in a given list of integers.
from itertools import combinations

def custom_max(pair):
    return max(pair)

def custom_min(pair):
    return min(pair)

def find_max_min_aggregation_pair(lst):
    if len(lst) < 2:
        return None  
    max_pair = max(combinations(lst, 2), key=custom_max)
    min_pair = min(combinations(lst, 2), key=custom_min)

    return max_pair, min_pair


numbers = [4, 8, 1, 6, 3, 9, 7, 2]
result = find_max_min_aggregation_pair(numbers)

if result:
    (max_value1, max_value2), (min_value1, min_value2) = result
    print(f"Maximum pair: ({max_value1}, {max_value2})")
    print(f"Minimum pair: ({min_value1}, {min_value2})")
else:
    print("Not enough elements in the list.")
