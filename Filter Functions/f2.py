#Python program that uses the filter function to extract all uppercase letters from a list of mixed-case strings.

mixed_case_strings = ["Hello",  "Python", "Filter", "Learning"]

print("Original list of strings:\n", mixed_case_strings)


uppercase_letters = [char for string in mixed_case_strings for char in string if char.isupper()]

print("\nExtract all uppercase letters from the said list of mixed-case strings:")

print(uppercase_letters)

