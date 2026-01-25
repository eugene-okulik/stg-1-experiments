# Эта программа рассчитывает сумму счета с чаевыми

bill_amount = int(input("Введите сумму счета: "))
tip_percentage = "15"  # 15% чаевых

total_to_pay = bill_amount + (bill_amount * (int(tip_percentage) / 100))

print("К оплате с учетом чаевых:", total_to_pay)
