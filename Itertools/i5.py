#Python program to generate an infinite cycle of elements from an iterable.
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)

#List
result = cycle_data(['A','B','C','D'])
print("The said function print never-ending items:")
for i in result:
    print(i)

#String
result = cycle_data('Python itertools')
print("The said function print never-ending items:")
for i in result:
    print(i)
