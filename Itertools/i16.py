#Python program to find the sorted sequence from a set of permutations of a given input.
from itertools import permutations

def sorted_sequence(input_str):
    
    perms = permutations(input_str)

    
    perm_strings = [''.join(perm) for perm in perms]

   
    sorted_perms = sorted(perm_strings)

    return sorted_perms


user_input = input("Enter a string: ")


result = sorted_sequence(user_input)
print("Sorted sequence from permutations:", result)
