#Task4

def checkargs(func):

    def wrapper(*args):
        for i in args:
            if not isinstance(i, (int, float)):
                print('Ошибка: только числа!')
                return
        func(*args)
    return wrapper


@checkargs
def mainfunc(*inpt):
    print(inpt)


mainfunc(2, 4, 5.5)