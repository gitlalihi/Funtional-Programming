# Python function that filters out all elements less than or equal than a specified value from a list of numbers using the filter function.
def filter_numbers_less_than(numbers, threshold):
    
    
    def is_less_than_threshold(num):
        return num <= threshold

    
    filtered_numbers = list(filter(is_less_than_threshold, numbers))

    return filtered_numbers


numbers = [20, 15, 24, 37, 23, 11, 7]
print("Original list of numbers:",numbers)
threshold = 20
print("\nFilters out all elements less than or equal to a specified value",threshold,":")
result = filter_numbers_less_than(numbers, threshold)
print(result)
