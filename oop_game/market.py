from oop_game.customer import Customer
from oop_game.farmer import Farmer

farmers = [
    Farmer("Эдик", "Помидоры", 100, 5),
    Farmer("Петр", "Арбузы", 200, 2),
    Farmer("Стёпа", "Огурцы", 5, 3)
]


name = input("Ваше имя: ")
money = int(input("Сколько у вас денег: "))

user = Customer(name, money)

while True:
    print("Выбери фермера:")
    print('\n'.join([farmer.product for farmer in farmers]))
    selected_line = int(input("Введи номер строки фермера: "))
    selected_farmer = farmers[selected_line]

    answer = int(input(f"Сколько {selected_farmer.product} ты хочешь купить? "))
    user.buy(selected_farmer, answer, selected_farmer.price)

    if answer == 0:
        break


