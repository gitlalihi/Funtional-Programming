#Python program to convert a given list of tuples to a list of strings using the map function.
def tuples_to_list_string(colors):
    result = list(map(' '.join, colors))
    return result   
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples:")
print(colors)
print("\nConvert the said list of tuples to a list of strings:")
print(tuples_to_list_string(colors))