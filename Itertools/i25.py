#Python program to find the nth Hamming number. Use the itertools module.
from itertools import count
import itertools as it

def is_hamming_number(num):
  
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5
    return num == 1

def nth_hamming_number(n):
    
    hamming_numbers = filter(is_hamming_number, count(start=1))
    return next(it.islice(hamming_numbers, n-1, None))


n = 10
result = nth_hamming_number(n)
print(f"The {n}th Hamming number is: {result}")
