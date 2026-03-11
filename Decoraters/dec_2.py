def silent(func):

    def wrapper(*args):
        result = func(*args)
        if not result:
            return
        else:
            print(result.upper())
    return wrapper


@silent
def example(text=None):
        return text

example('')
