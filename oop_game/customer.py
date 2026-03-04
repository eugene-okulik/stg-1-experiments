from oop_game.farmer import Farmer


class Customer:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.basket = 0

    def buy(self, seller: Farmer, amount: int, price_per_kg: int):
        total_price = amount * price_per_kg

        if total_price <= self.money:
            if seller.sell(amount, self.money):
                self.money -= total_price
                self.basket += amount
                print(f"🛒 {self.name}: Купил {amount} кг. Остаток денег: {self.money} руб.")
            else:
                print(f"🛒 {self.name}: Жалко")
        else:
            print(f"🛒 {self.name}: У меня не хватает денег!")
