# Задание 2
# Создайте декоратор @silent, который вызывает функцию, но
# ничего не выводит на экран и не возвращает результат, если
# функция вернула None или пустую строку. Если же результат есть —
# он выводится в верхнем регистре.


def silent(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            print(str(result).upper())

    return wrapper

# Всё что не False, None, пустая строка, число 0, пустая коллекция (list, tuple, dict, set)
# питоном воспринимается как True


def silent2(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result != '' and result is not None:
            print(str(result).upper())

    return wrapper


@silent2
def func1(x, y):
    return x - y

@silent2
def func2(text):
    if 5 < len(text) < 10:
        return text
    elif len(text) >= 10:
        return ''
    else:
        return None

func1(5, 3)
func1(3, 3)
func2('dddddd')
func2('ddddddehehehehehehehhe')
func2('dd')