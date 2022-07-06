import datetime
import pytz

# logging the transactions

class Account:  # keep the class name capitalized
    """ Simple account class with balance"""    # this is a doc string

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
        print("Account created for", name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            status = 'Successful'
        else:
            print('Invalid amount, should be greater than zero')
            status = 'Failed'

        # log it
        self.log('Deposit', amount, status)

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance += amount
            status = 'Successful'
        else:
            print('Withdraw amount should be greater than zero and not more than the balance')
            status = 'Failed'

        # log it
        self.log('Withdraw', amount, status)

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def log(self, transaction_type, amount, status):
        ## logging the time, type and amount
        time = pytz.utc.localize(datetime.datetime.utcnow())
        self.transactions.append((transaction_type, amount, status, time))

if __name__ == '__main__':
    afaq = Account('Sanjar', 0)
    # afaq.show_balance()
    afaq.deposit(1000)
    afaq.withdraw(50)
    print(afaq.transactions)
