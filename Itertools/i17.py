#Python program to read a given string character by character and compress repeated characters by storing the length of those character(s).
from itertools import groupby
def encode_str(input_str):
    return [(len(list(n)), m) for m,n in groupby(input_str)]
 
str1 = input("Enter your string") 
print("Original string:")
print(str1)
print("Result:")
print(encode_str(str1))

str1 = input("Enter your second string")
print("\nOriginal string:")
print(str1)
print("Result:")
print(encode_str(str1))
