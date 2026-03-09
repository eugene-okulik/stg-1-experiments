class BankTerminal():
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        self.history = []

    def add_money(self, amount_for_add):
        self.balance += amount_for_add
        self.history.append(f"+{amount_for_add}: 'Пополение'")

    def get_report(self):
        self.balance -= 50
        print(f"Ваш баланс: {self.balance} руб.")
        print(f"Ваш список операций: {self.history}")

    def take_loan(self, amount_fot_take_loan):
        self.balance += (
            amount_fot_take_loan
            - (amount_fot_take_loan * 20 / 100)
        )

    def transfer(self, other_account, amount_for_transfer):
        commission = amount_for_transfer * 5 / 100
        if self.balance >= amount_for_transfer + commission:
            self.balance = self.balance - (amount_for_transfer + commission)
            other_account.add_money(amount_for_transfer)
        else:
            print("На Вашем счете недостаточно средств")


acc1_name = input("Как Вас зовут: ")

acc1 = BankTerminal(acc1_name, 1050)
acc2 = BankTerminal("Иван", 0)

while True:
    selected_number = int(
        input(""
              "Выберите услугу для Вашего счета:"
              "\n 1. Узнать баланс "
              "\n 2. Увеличить кредитный лимит "
              "\n 3. Перевести деньги"
              "\nВведите номер строки: "
              )
    )
    if selected_number == 1:
        acc1.get_report()
        print("-" * 58)

    elif selected_number == 2:
        amount = int(
            input(
                "Введите сумму, на которую хотите увеличить "
                "кредитный лимит: "))
        acc1.take_loan(amount)
        print("-" * 58)

    elif selected_number == 3:
        amount_for_transfer = int(input("Введите сумму для перевода: "))
        acc1.transfer(acc2, amount_for_transfer)
        print("-" * 58)

    else:
        print("Вы ввели некорректную цифру")
        print("-" * 58)
        break
