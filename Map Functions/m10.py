#Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a list of the numbers.
def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]

def square(x):
    return x**2
N = int(input("Enter the value of N: "))
squared_fibonacci = list(map(square, fibonacci(N)))


print(f"Squared Fibonacci numbers for the first {N} Fibonacci numbers:")
print(squared_fibonacci)
