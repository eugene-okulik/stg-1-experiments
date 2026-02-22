def dec_1(func):

    def wrapper(*args):
        count = 0
        for i in args:
            count +=1
        print(f'function name is {func.__name__}, number of arguments =  {count}')
    return wrapper


@dec_1
def example(*args):
    for i in args:
        print(i)


example('плохо, все плохо', 'плохо отдыхать',1, 'жизнь прекрасна!')