#Python program to detect the number of local variables declared in a function
def example_function():
    a = 1
    b = 2
    c = "hello"
    d = [4, 5, 6]

    local_variables = locals()
    number_of_locals = len(local_variables)

    return number_of_locals

result = example_function()
print("Number of local variables in example_function:", result)
