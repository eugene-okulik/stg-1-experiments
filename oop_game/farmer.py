class Farmer:
    def __init__(self, name, product, quantity, price):
        self.name = name
        self.product = product
        self.quantity = quantity
        self.price = price

    def sell(self, amount, money):
        total_price = amount * self.price
        if self.quantity >= amount and money >= total_price:
            self.quantity -= amount
            change = 0
            if money > total_price:
                change = money - total_price
            print(f"👩‍🌾 {self.name}: Продал {amount} кг {self.product}. Осталось: {self.quantity} кг., сдача: {change} руб.")
            return True
        else:
            print(f"👩‍🌾 {self.name}: Извините, я не могу вам продать {self.product}")
            return False