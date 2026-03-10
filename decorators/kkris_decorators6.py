#Task6

results = []
def decor(func):

    def wrapper(*args):
        results.append(func(*args))
    return wrapper


@decor
def mainfunc(inpt):
    return inpt
    

mainfunc(1)
mainfunc(2)
mainfunc(3)
print(results)
