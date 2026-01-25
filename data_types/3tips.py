# Эта программа рассчитывает сумму счета с чаевыми

bill_amount = float(input("Введите сумму счета: "))
tip_percentage = 0.15  # 15% чаевых

total_to_pay = bill_amount + (bill_amount * tip_percentage)

print("К оплате с учетом чаевых:", total_to_pay)
