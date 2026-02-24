# Эта программа рассчитывает сумму счета с чаевыми
bill_amount = float(input("Введите сумму счета: "))
tip_percentage = float("15")  # 15% чаевых
total_to_pay = bill_amount + (bill_amount * tip_percentage) / 100
print("К оплате с учетом чаевых:", total_to_pay)
