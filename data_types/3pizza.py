print("Мы заказали две пиццы.")
slices_per_pizza = "8"
number_of_pizzas = 2

total_slices = int(slices_per_pizza) * number_of_pizzas
print("Итого у нас было", total_slices, "аппетитных кусочков.")

friends = input("Сколько друзей пришло? ")
eaten_slices = total_slices - int(friends)
print("После вечеринки осталось", eaten_slices, "кусочков.")
