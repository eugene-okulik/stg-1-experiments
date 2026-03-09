class BankTerminal:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        self.history = list()

    def add_money(self, amount):
        self.balance += amount
        self.history.append(f'+{amount}: Пополнение')

    def get_report(self):
        self.balance -= 50
        self.history.append('-50: Предоставление отчета')
        print(self.balance)
        for i in self.history:
            print(i)

    def take_loan(self, amount):
        self.balance = self.balance + amount - 0.2 * amount
        self.history.append(f"+{amount}: Получение кредита")
        self.history.append(f"-{0.2 * amount}: Списание 20% от размера кредита")
        print(self.balance)
        for i in self.history:
            print(i)

    def transfer(self, other_account, amount):
        commission = 0.05 * amount
        if self.balance >= amount + commission:
            self.balance = self.balance - amount - commission
            self.history.append(f"-{amount}: Перевод acc2")
            self.history.append(f"-{commission}: Комиссия за перевод 5 %")
            print(self.balance)
            for i in self.history:
                print(i)
            other_account.add_money(amount)
        else:
            print('Для перевода не достаточно средств на счете')


name = input("Ваше имя владельца первого счета: ")
acc1 = BankTerminal(name, 1000)
acc2 = BankTerminal("Иван", 0)

while True:
    action = int(input("Введите порядковый номер действия, которое хотите совершить: 1.add money, 2.get report, "
                       "3.take loan, 4.transfer, нажмите любую другую цифру для завершения работы: "))
    if action == 1:
        acc1.add_money(int(input('Введите сумму вносимых средств:')))
    elif action == 2:
        acc1.get_report()
    elif action == 3:
        acc1.take_loan(int(input('Введите сумму запрашиваемого займа:')))
    elif action == 4:
        acc1.transfer(acc2, int(input('Введите сумму перевода:')))
    else:
        break
