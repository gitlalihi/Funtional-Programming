#Python program to make an iterator that drops elements from the iterable as soon as an element is a positive number.
import itertools as it
def negative_num(x):
    return x < 0
def drop_while(nums):
    return it.dropwhile(negative_num, nums)
nums = [-1,-2,-3,4,-10,2,0,5,12]
print("Original list: ",nums)
result = drop_while(nums)
print("Drops elements from the iterable when a positive number arises \n",list(result))
