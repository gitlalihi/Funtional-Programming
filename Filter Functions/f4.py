#Python program that creates a list of names and uses the filter function to extract names that start with a vowel (A, E, I, O, U).

def starts_with_vowel(name):
    return name[0].upper() in "AEIOU"


names = ["Alice", "Bob", "Eve", "Charlie", "Olivia", "John", "Ivy", "David"]

print("Original list of names:\n", names)


vowel_starting_names = list(filter(starts_with_vowel, names))

print("\nExtract names that start with a vowel:")

print(vowel_starting_names)

