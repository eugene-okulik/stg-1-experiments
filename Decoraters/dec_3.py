def tax(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) * 1.2
        return result
    return wrapper


@tax
def total_price(count, price):
    return (count * price)


@tax
def discount(price, discount):
    return (price * ((100 - discount) / 100))

print(total_price(2, 50))
print(discount(100, 20))