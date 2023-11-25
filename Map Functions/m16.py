#Python program to convert a given list of strings into a list of lists using the map function.
def strings_to_listOflists(str):
    result = map(list, str)
    return list(result)

colors = ["Red", "Green", "Black", "Orange"]
print('Original list of strings:')
print(colors)
print("\nConvert the said list of strings into list of lists:")
print(strings_to_listOflists(colors))
