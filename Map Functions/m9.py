# Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.
original_tuple = ('1', '2', '3', '4', '5')


new_list = list(map(int, original_tuple[1:4]))


print("Original tuple:", original_tuple)
print("New list with specific elements converted to integers:", new_list)