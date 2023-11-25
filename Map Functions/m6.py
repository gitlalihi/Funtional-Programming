#Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.
sequence = "Hello World"


uppercase_result = ''.join(map(str.upper, sequence))


lowercase_result = ''.join(map(str.lower, sequence))

unique_result = ''.join(set(sequence))


print("Original sequence:", sequence)
print("Uppercase result:", uppercase_result)
print("Lowercase result:", lowercase_result)
print("Unique result:", unique_result)