#Python program to find the first two elements of a given list whose sum is equal to a given value. Use the itertools module to solve the problem.
from itertools import combinations

def find_pair_with_sum(lst, target_sum):
    pairs = list(combinations(lst, 2))

    for pair in pairs:
        if sum(pair) == target_sum:
            return pair

    return None


given_list = [1, 2, 3, 4, 5, 6]
given_sum = 9

result = find_pair_with_sum(given_list, given_sum)

if result:
    print(f"The first two elements whose sum is {given_sum}: {result}")
else:
    print(f"No such pair found.")
