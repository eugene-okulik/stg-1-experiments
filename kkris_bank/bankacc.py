class BankTerminal:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        self.history = []

    def add_money(self, amount):
        self.balance += amount
        self.history.append(f"+{amount}: Пополнение")

    def get_report(self):
        print("За получение отчета списано 50 руб.")
        self.balance -= 50
        self.history.append(f"Получение отчета: -50 руб.")
        print(f"Ваш баланс: {self.balance} руб.")
        print(f"История операций: {self.history}")

    def take_loan(self, credit_amount):
        self.balance += credit_amount
        print(f"Вам зачислена сумма кредита: {credit_amount} руб.")
        self.history.append(f"Получение кредита: {credit_amount} руб.")
        self.balance -= credit_amount * 0.2
        print(f"Платеж в размере 20% от суммы кредита ({credit_amount * 0.2} руб.) списан.")
        self.history.append(f"Списание платежа по кредиту: -{credit_amount * 0.2} руб.")

    def transfer(self, other_acc, transfer_amount):
        fee = transfer_amount * 0.05
        if self.balance >= transfer_amount + fee:
            self.balance -= transfer_amount + fee
            other_acc.add_money(transfer_amount)
            print(f"Перевод {transfer_amount} руб. выполнен. Комиссия: {fee} руб.")
            self.history.append(f"Перевод: {transfer_amount + fee} руб.")
        else:
            print("Недостаточно средств")


name = input("Ваше имя: ")
acc1 = BankTerminal(name, 1000)
acc2 = BankTerminal('Ivan', 0)


while True:
    selected_act = input("Выберите действие (add_money, get_report, take_loan, transfer): ")
    if selected_act == "add_money":
        amount = int(input("На какую сумму хотите пополнить: "))
        acc1.add_money(amount)
    elif selected_act == "get_report":
        acc1.get_report()
    elif selected_act == "take_loan":
        credit_amount = int(input("На какую сумму нужен кредит: "))
        acc1.take_loan(credit_amount)
    elif selected_act == "transfer":
        transfer_amount = int(input("Сколько хотите перевести: "))
        acc1.transfer(acc2, transfer_amount)
    else:
        print("Действие не поддерживается")
        break
