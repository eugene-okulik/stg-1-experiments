def dec_1(func):

    def wrapper(*args):
        updated = []
        for i in args:
            if isinstance(i, str):
                i = i.replace('плохо','хорошо')
            updated.append(i)
        result = func(*updated)
        return result
    return wrapper


@dec_1
def example(*args):
    for i in args:
        print(i)


example('плохо, все плохо', 'плохо отдыхать',1, 'жизнь прекрасна!')