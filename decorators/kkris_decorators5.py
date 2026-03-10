#Task5

def name_args(func):

    def wrapper(*args):
        print('Function name:', func.__name__)
        print('Arguments number:', len(args))
        func(*args)
    return wrapper


@name_args
def mainfunc(*args):
    return args


mainfunc(1, 2, 3)
