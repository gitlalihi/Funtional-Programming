#Python program that iterates the integers from 1 to a given number and prints "Fizz" for multiples of three, prints "Buzz" for multiples of five, and prints "FizzBuzz" for multiples of both three and five using the itertools module.

import itertools as it
 
def fizz_buzz(n):
    fizzes = it.cycle([""] * 2 + ["Fizz"])
    buzzes = it.cycle([""] * 4 + ["Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result = (word or n for word, n in zip(fizzes_buzzes, it.count(1)))
    for i in it.islice(result, 100):
        print(i)

n = 50
fizz_buzz(n)
