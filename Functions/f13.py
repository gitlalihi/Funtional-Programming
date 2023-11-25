#Python program to execute a string containing Python code.
code_to_execute = """
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("Result:", result)
"""

try:
    exec(code_to_execute)
except Exception as e:
    print("Error:", e)
