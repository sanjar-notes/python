class Account:  # keep the class name capitalized
    """ Simple account class with balance"""    # this is a doc string

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for", name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        self.show_balance()

    def withdraw(self, amount):
        if amount > 0:
            self.balance += amount

    def show_balance(self):
        print("Balance is {}".format(self.balance))

if __name__ == '__main__':
    afaq = Account('Sanjar', 0)
    # afaq.show_balance()
    afaq.deposit(1000)
