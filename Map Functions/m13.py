#Python program to count the same pair in two given lists. Use map() function.


def create_pairs(x, y):
    return x, y

def count_same_pairs(pair):
    return 1 if pair[0] == pair[1] else 0

def count_same_pairs_in_lists(list1, list2):
   pairs = list(map(create_pairs, list1, list2))
   same_pairs_count = sum(map(count_same_pairs, pairs))
   return same_pairs_count


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 6]

result = count_same_pairs_in_lists(list1, list2)
print(f"Number of same pairs: {result}")
