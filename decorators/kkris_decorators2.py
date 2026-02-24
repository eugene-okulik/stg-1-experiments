#Task2
import random

def silent(func):

    def wrapper(*args):
        result = func(*args)
        if isinstance(result, str):
            if result is None or result == "":
                pass
            else:
                print(result.upper())
    return wrapper


@silent
def mainfunc(*randomlist):
    return random.choice(randomlist)

mainfunc(None, "", 'sun')