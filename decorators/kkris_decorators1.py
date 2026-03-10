#Task1


def decor(func):

    def wrapper(*args):
        new_args = []
        forbidden_word = 'bad'
        for line in args:
            if isinstance(line, str):
                new_args.append(line.replace(forbidden_word, 'good'))
            else:
                new_args.append(line)
        func(*new_args)
    return wrapper


@decor
def mainfunc(*text):
    print(text)


mainfunc('hi', 5, 'bad', 55, 'lololo', 'bad', 1)
