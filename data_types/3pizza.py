number_of_pizzas = 2
slices_per_pizza = 8

print("Мы заказали", number_of_pizzas, "пиццы.")

total_slices = slices_per_pizza * number_of_pizzas
print("Итого у нас было", total_slices, "аппетитных кусочков.")

friends = int(input("Сколько друзей пришло?"))
remaining_slices = total_slices - friends
print("После вечеринки осталось", remaining_slices, "кусочков.")
