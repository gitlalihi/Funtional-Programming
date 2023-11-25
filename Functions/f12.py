#Python program to create a chain of function decorators (bold, italic, underline etc.)
def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

def italic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

def underline_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<u>{result}</u>"
    return wrapper


@bold_decorator
@italic_decorator
@underline_decorator
def my_text():
    return "Hello, World!"


formatted_text = my_text()

print(formatted_text)
