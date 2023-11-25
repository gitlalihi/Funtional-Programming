#Python program to find the factorial of a number using the itertools module.
from itertools import permutations
from functools import reduce

def multiply(x, y):
    return x * y

def factorial_using_permutations(n):
    
    perm_tuples = permutations(range(1, n + 1))
    product = 1
    for perm in perm_tuples:
        product *= reduce(multiply, perm)

    return product


num = int(input("Enter a number: "))


result = factorial_using_permutations(num)
print(f"The factorial of {num} is: {result}")
