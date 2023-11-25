#Python program to create an iterator that returns consecutive keys and groups from an iterable.
from itertools import groupby

def key_function(item):
    index, value = item
    return index - value

def consecutive_keys_and_groups(iterable):
    for key, group in groupby(enumerate(iterable), key_function):
        consecutive_group = [item[1] for item in group]
        yield key, consecutive_group


data = [1, 2, 3, 7, 8, 9, 10, 15, 16, 17]

result = list(consecutive_keys_and_groups(data))

print("Consecutive Keys and Groups:")
for key, group in result:
    print(f"Key: {key}, Group: {group}")
