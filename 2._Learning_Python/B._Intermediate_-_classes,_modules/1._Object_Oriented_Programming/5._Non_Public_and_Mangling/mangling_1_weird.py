import datetime
import pytz

### Add the functionality of logging in account creation details when creating the object

class Account:
    """ Simple account class with balance """
    __power = 'Tow'
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]    # done
        print("Account created for " + self._name)
        self.__balance+=-2300

        # logging this as deposit

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance")

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1


if __name__ == '__main__':
    tim = Account("Tim", 0)

    # time.__balance = 99 wrong, it will make a new variable
    tim._Account__balance = 99  # we set __balance to 23
    tim.show_balance()  #but it wasn't changed
    print(tim.__dict__)
