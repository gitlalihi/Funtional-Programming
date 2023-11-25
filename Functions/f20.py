#Python function to check whether a string is a pangram or not.
def is_pangram(input_string):
    
    input_string = input_string.lower()
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    return set(input_string) >= alphabet_set

input_str = input("Enter your sentence")
if is_pangram(input_str):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")