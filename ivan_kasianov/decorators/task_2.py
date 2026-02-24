def decor_1(func):

    def wrapper(args):
        result = func(args)
        if result is not None and result != "":
            return
        else:
            print(result.upper())
    return wrapper


@decor_1
def task_2(x):
    return x


task_2("")
