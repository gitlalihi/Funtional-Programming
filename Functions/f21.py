#Python program that invokes a function after a specified period of time.
import time


def my_function():
    print("Function invoked!")

def invoke_after_delay(delay,my_function):
    time.sleep(delay)
    my_function()
    

delay_seconds = 5
invoke_after_delay(delay_seconds, my_function)
