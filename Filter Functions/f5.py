#Python function that filters out all empty strings from a list of strings using the filter function.
def filter_non_empty_strings(strings):
    def is_non_empty_string(s):
        return s.strip() != ""
    non_empty_strings = list(filter(is_non_empty_string, strings))
    return non_empty_strings


strings = ["",  "Filter", "", "Python", ""]
print("Original list of strings:",strings)
print("\nA new list containing only non-empty strings:")
result = filter_non_empty_strings(strings)
print(result)  
