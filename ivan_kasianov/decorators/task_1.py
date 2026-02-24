def decor_1(func):

    def wrapper(*args):
        new_args = []
        for i in args:
            if "плохо" in i:
                new_args.append(i.replace("плохо", "хорошо"))
            else:
                new_args.append(i)
        return func(*new_args)
    return wrapper


@decor_1
def forbidden_word(*args):
    print(" ".join(args))


forbidden_word(
    "Привет, как у тебя дела? Привет, плохо! А твои как? Тоже плохо!",
               "Как настроение?",
               "плохо",
               "и у меня плохо"
)
