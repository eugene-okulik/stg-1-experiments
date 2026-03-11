def dec_1(func):

    def wrapper(*args):
        for i in args:
            if not isinstance(i, int) or isinstance(i, float):
                print('Ошибка: только числа!')
                return

        return func(args)
    return wrapper


@dec_1
def example(*args):
    for i in args:
        print(i)


example('плохо, все плохо', 'плохо отдыхать',1, 'жизнь прекрасна!')