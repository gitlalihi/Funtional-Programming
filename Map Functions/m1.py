#Python program to triple all numbers in a given list of integers. Use Python map.
def triple_number(x):
    return 3 * x


numbers = [1, 2, 3, 4, 5]


tripled_numbers = list(map(triple_number, numbers))


print("Original numbers:", numbers)
print("Tripled numbers:", tripled_numbers)