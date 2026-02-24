# Эта программа считает общую стоимость
print("Расчет общей стоимости заказа")
order = {"item1": "100", "item2": "200", "item3": "150"}
total = float(order["item1"]) + float(order["item2"]) + float(order["item3"])
print("Общая стоимость заказа:", total, "рублей")
