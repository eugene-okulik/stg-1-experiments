#Task3

def nds(func):

    def wrapper(arg1, arg2):
        result = func(arg1, arg2)
        result = result + result * 20 / 100
        print(result)
    return wrapper


@nds
def full_amount(price, amount):
    return price * amount


@nds
def discount_amount(price, discount):
    return price - price * discount / 100


full_amount(10, 2)
discount_amount(10, 10)