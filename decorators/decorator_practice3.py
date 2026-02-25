# Задание 3
# Есть функции, которые просто делают вычисления цены: одна
# умножает цену на количество товара (принимает количество и
# цену, возвращает результат), другая применяет скидку к цене
# (принимает цену и процент скидки, возвращает результат), ну
# и еще какую-то можете придумать. Создайте декоратор, который
# добавляет к результату функции НДС 20%


def nds(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 1.2

    return wrapper


@nds
def total_price(price, qty):
    return price * qty

@nds
def discount(price, discount_percent):
    discount_value = price * (discount_percent / 100)
    return price - discount_value

print(total_price(2, 5)) # 12
print(discount(10, 20)) # 9.6