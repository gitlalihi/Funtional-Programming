#Python program to find the shortest distance from a specified character in a given string. Return the shortest distances through a list and use an itertools component to solve the problem.
from itertools import combinations

def shortest_distances(s, target_char):
    indices = [i for i, char in enumerate(s) if char == target_char]
    combinations_of_indices = combinations(indices, 2)

    distances = [abs(j - i) for i, j in combinations_of_indices]
    
    return distances


input_string = "example string with some e's"
target_character = 'e'
result = shortest_distances(input_string, target_character)

print(f"Shortest distances from '{target_character}' in the string: {result}")
