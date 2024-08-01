class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def to_deposit(self):
        to_deposit = int(input('Cuanto quieres depositar?: '))
        self.balance = self.balance + to_deposit
        return self.balance

    def check_balance(self):
        check_balance = print(f'Tienes un balance de {self.balance} dólares.')
        return check_balance

rodri_account = BankAccount(25000)
rodri_account.to_deposit()
rodri_account.check_balance()
