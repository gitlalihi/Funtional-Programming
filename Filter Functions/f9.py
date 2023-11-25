#Python function that filters out elements from a list of strings containing a specific substring using the filter function.
def filter_strings_with_substring(strings, substring):
    def contains_substring(string):
        return substring in string
    filtered_strings = list(filter(contains_substring, strings))
    return filtered_strings


strings = ["Red", "Green", "Orange", "White", "Black", "Pink", "Yellow"]
print("List of words:")
print(strings)
substring = "l"
print("Substring:",substring)
print("Filter out strings with the substring:")
result = filter_strings_with_substring(strings, substring)
print(result)  
