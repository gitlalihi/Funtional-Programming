#Python program that generates the running product of elements in an iterable.
def running_product(iterable):
    result = []
    product = 1

    for element in iterable:
        product *= element
        result.append(product)

    return result


numbers = [2, 3, 4, 5]

result = running_product(numbers)

print(f"Original Iterable: {numbers}")
print(f"Running Product: {result}")
