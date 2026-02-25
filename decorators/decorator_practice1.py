# Задание 1
# Создайте декоратор, который проверяет содержимое всех переданных в
# функцию аргументов. Если в каком нибудь из стринговых аргументов есть
# «запрещенное» слово (пусть, запрещенным будет, "плохо"), декоратор
# заменяет его на "хорошо" перед тем, как передать в функцию.


BAD_WORD = 'плохо'
GOOD_WORD = 'хорошо'


def bad_word(func):

    def wrapper(*args, **kwargs):
        args = list(args)

        def replace_bad_word(word):
            if isinstance(word, str):
                if BAD_WORD in str(word).lower():
                    return word.replace(BAD_WORD, GOOD_WORD)
            return word

        for i, value in enumerate(args):
            args[i] = replace_bad_word(value)
        for key, value in kwargs.items():
            kwargs[key] = replace_bad_word(value)
        return func(*args, **kwargs)

    return wrapper


@bad_word
def print_text(text):
    print(text)


print_text('Плохо sal;dkjfa')
print_text('asdfasdf. Плохо sal;dkjfa')
print_text('Плохо sal;dkjfa')
print_text('asdfasdf. ПлОхо sal;dkjfa')
print_text('asdfasdf. ПЛОХО sal;dkjfa')
print_text(text='ksjjdhsjdf плохо sal;dkjfa')
