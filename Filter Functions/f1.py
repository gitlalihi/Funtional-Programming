# Python function that filters out even numbers from a list of integers using the filter function.
def filter_even_nums(nums):
    def is_odd(num):
        return num % 2 != 0
    odd_nums = list(filter(is_odd, nums))
    return odd_nums

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original numbers:",nums)
result = filter_even_nums(nums)
print("After filters out even numbers from the said list of integers ")
print(result)  # Output: [1, 3, 5, 7, 9]
