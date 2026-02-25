# адание 4
# Напишите декоратор, который проверяет, являются ли все переданные
# в функцию аргументы числами (int или float). Если хотя бы один
# аргумент — строка или список или еще какое-то не число, декоратор
# должен не запускать функцию, а печатать: "Ошибка: только числа!".


def only_nums(func):

    def wrapper(*args, **kwargs):
        all_args = (list(args))
        all_args.extend(kwargs.values())
        if all([isinstance(value, int) or isinstance(value, float) for value in all_args]):
            return func(*args, **kwargs)
        else:
            print("Ошибка: только числа!")
            return None

    return wrapper

@only_nums
def calc(a, b):
    return a + b

print(calc(1, 2.2))
print(calc(1, 'one'))
