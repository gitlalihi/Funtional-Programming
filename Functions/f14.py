#Python program to access a function inside a function.
def outer_function(x):
    def inner_function(y):
        return x + y

    result = inner_function(5)
    return result


output = outer_function(3)
print("Output:", output)
