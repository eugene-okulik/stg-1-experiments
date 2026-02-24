def decor_nds(func):
    def wrapper(*args):
        result = func(*args)
        return result + (result * 0.20)

    return wrapper


@decor_nds
def total_price(price, amount):
    return price * amount


@decor_nds
def discount_price(price, discount):
    return price - (price * (discount / 100))


@decor_nds
def delivery_price(price, delivery):
    return price + delivery


print(total_price(200, 10))
print(discount_price(700, 20))
print(delivery_price(300, 25))
