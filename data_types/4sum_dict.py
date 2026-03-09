# Эта программа считает общую стоимость

print("Расчет общей стоимости заказа")
order = {"item1": "100", "item2": "200", "item3": "150"}

total = int(order["item1"]) + int(order["item2"]) + int(order["item3"])

print("Общая стоимость заказа:", total, "рублей")
